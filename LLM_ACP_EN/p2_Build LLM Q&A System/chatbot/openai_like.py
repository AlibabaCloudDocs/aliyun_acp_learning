import os
import requests
from typing import List, Dict, Any, Optional
from llama_index.core.postprocessor.types import BaseNodePostprocessor 
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core.schema import NodeWithScore, QueryBundle

class OpenAILikeRerank:
    """
    使用 requests 调用 DashScope OpenAI 兼容的 Rerank 接口。
    """

    def __init__(self, api_base: str, api_key: str, model_name: str):
        self.api_base = api_base.rstrip("/")
        self.api_key = api_key
        self.model_name = model_name
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

    def rerank(self, query: str, documents: List[str], top_n: int) -> List[Dict[str, Any]]:
        url = f"{self.api_base}/reranks"

        payload = {
            "model": self.model_name,
            "query": query,
            "documents": documents,
            "top_n": top_n,
        }

        try:
            resp = self.session.post(url, json=payload)
            resp.raise_for_status()
            data = resp.json()

            # 兼容接口：results 在根目录
            results = data.get("results") 
            if not results:
                results = data.get("output", {}).get("results", [])
            
            if not results:
                return []

            return [{
                "index": item.get("index", i),
                "score": item.get("relevance_score", item.get("score", 0.0))
            } for i, item in enumerate(results)]

        except Exception as e:
            print(f"[OpenAILikeRerank] API Request Failed: {e}")
            if 'resp' in locals():
                print(f"Response Text: {resp.text}")
            raise RuntimeError(f"Rerank API error: {str(e)}")


class OpenAILikeRerankPostprocessor(BaseNodePostprocessor):
    """
    LlamaIndex node postprocessor that uses the fixed Rerank client.
    """
    rerank_client: OpenAILikeRerank
    top_n: int = 3

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

        index_to_score = {
            r["index"]: r.get("score", 0.0)
            for r in rerank_results
        }

        new_nodes: List[NodeWithScore] = []
        sorted_indices = sorted(index_to_score.items(), key=lambda x: x[1], reverse=True)
        
        for idx, score in sorted_indices:
            if 0 <= idx < len(nodes):
                n = nodes[idx]
                new_nodes.append(NodeWithScore(node=n.node, score=score))

        return new_nodes