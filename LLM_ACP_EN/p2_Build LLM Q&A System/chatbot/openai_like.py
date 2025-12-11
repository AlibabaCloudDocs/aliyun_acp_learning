from typing import List, Dict, Any, Optional
from openai import OpenAI
from pydantic import Field
from llama_index.core.postprocessor.types import BaseNodePostprocessor
from llama_index.core.schema import NodeWithScore
from llama_index.core import QueryBundle


class OpenAILikeRerank:
    """
    A simple client for an OpenAI-compatible rerank endpoint.

    It assumes your server exposes a /rerank endpoint that accepts:
      - model: model name
      - query: query string
      - documents: list of document strings
      - top_n: number of results to return

    and returns a JSON with a "results" field like:
      [
          {"index": 2, "score": 0.98},
          {"index": 0, "score": 0.85},
          ...
      ]
    """

    def __init__(self, api_base: str, api_key: str, model_name: str):
        self.client = OpenAI(
            base_url=api_base,
            api_key=api_key,
        )
        self.model_name = model_name

    def rerank(self, query: str, documents: List[str], top_n: int) -> List[Dict[str, Any]]:
        """
        Call the OpenAI-compatible rerank endpoint.

        Args:
            query: query string
            documents: list of document texts
            top_n: number of items to keep

        Returns:
            A list of dicts with at least:
                - index: original document index
                - score: relevance score
        """
        response = self.client.post(
            "/rerank",
            json={
                "model": self.model_name,
                "query": query,
                "documents": documents,
                "top_n": top_n,
            },
        )
        data = response.json()
        return data["results"]


class OpenAILikeRerankPostprocessor(BaseNodePostprocessor):
    """
    LlamaIndex node postprocessor that uses an OpenAI-compatible rerank service
    to reorder retrieved nodes.
    """

    # Declare fields explicitly for Pydantic compatibility
    rerank_client: OpenAILikeRerank = Field(...)
    top_n: int = Field(default=3)

    def _postprocess_nodes(
        self,
        nodes: List[NodeWithScore],
        query_bundle: Optional[QueryBundle] = None,
    ) -> List[NodeWithScore]:
        if not nodes:
            return nodes
        if query_bundle is None or not query_bundle.query_str:
            return nodes

        query = query_bundle.query_str
        texts = [n.node.get_content() for n in nodes]

        try:
            rerank_results = self.rerank_client.rerank(
                query=query,
                documents=texts,
                top_n=min(self.top_n, len(texts)),
            )
        except Exception as e:
            print(f"[OpenAILikeRerankPostprocessor] rerank failed, skip. Error: {e}")
            return nodes

        # rerank_results: [{"index": i, "score": s}, ...]
        index_to_score = {
            r["index"]: r.get("score", r.get("relevance_score", 0.0))
            for r in rerank_results
        }

        new_nodes: List[NodeWithScore] = []
        for idx, score in sorted(index_to_score.items(), key=lambda x: x[1], reverse=True):
            if 0 <= idx < len(nodes):
                n = nodes[idx]
                new_nodes.append(NodeWithScore(node=n.node, score=score))

        return new_nodes
