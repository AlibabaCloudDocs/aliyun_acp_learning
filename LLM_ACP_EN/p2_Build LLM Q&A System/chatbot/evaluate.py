from langchain_community.llms.tongyi import Tongyi
from langchain_community.embeddings import DashScopeEmbeddings
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import context_recall, context_precision, answer_correctness

def evaluate_result(question, response, ground_truth):
    answer = response.response_txt
    context = [source_node.get_content() for source_node in response.source_nodes]

    data_samples = {
        'question': [question],
        'answer': [answer],
        'ground_truth': [ground_truth],
        'contexts': [context],
    }
    dataset = Dataset.from_dict(data_samples)
    score = evaluate(
        dataset=dataset,
        metrics=[answer_correctness, context_recall, context_precision],
        llm=Tongyi(model_name="qwen-plus"),
        embeddings=DashScopeEmbeddings(model="text-embedding-v3")
    )
    return score.to_pandas()


from typing import List
from openai import OpenAI
from ragas.embeddings.base import BaseRagasEmbeddings

class RagasOpenAICompatibleEmbeddings(BaseRagasEmbeddings):
    def __init__(self, model: str, base_url: str, api_key: str):
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def embed_texts(self, texts: List[str]):
        resp = self.client.embeddings.create(
            model=self.model,
            input=texts,
        )
        return [d.embedding for d in resp.data]

    def embed_documents(self, texts: List[str]):
        return self.embed_texts(texts)

    def embed_query(self, text: str):
        return self.embed_texts([text])[0]
