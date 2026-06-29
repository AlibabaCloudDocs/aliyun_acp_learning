import os
import getpass
from langchain_community.llms.tongyi import Tongyi
from langchain_community.embeddings import DashScopeEmbeddings
from datasets import Dataset 
from ragas import evaluate
from ragas.metrics import faithfulness,answer_relevancy,context_recall,context_precision,answer_correctness
import pandas as pd
from utils.custom_llm import CustomLLM
from ragas_prompt.chinese_prompt import *

# 适配到中文prompt中，prompt的内容请参考docs/P2.构造大模型问答系统/ragas_prompt/chinese_prompt.py
answer_relevancy.question_generation.instruction = AnswerRelavency.question_generation_prompt["instruction"]
answer_relevancy.question_generation.output_format_instruction = AnswerRelavency.question_generation_prompt["output_format_instruction"]
answer_relevancy.question_generation.examples = AnswerRelavency.question_generation_prompt["examples"]

faithfulness.nli_statements_message.instruction = Faithfulness.nli_statements_message_prompt["instruction"]
faithfulness.nli_statements_message.output_format_instruction = Faithfulness.nli_statements_message_prompt["output_format_instruction"]
faithfulness.nli_statements_message.examples = Faithfulness.nli_statements_message_prompt["examples"]
faithfulness.statement_prompt.instruction = Faithfulness.statement_prompt["instruction"]
faithfulness.statement_prompt.output_format_instruction = Faithfulness.statement_prompt["output_format_instruction"]
faithfulness.statement_prompt.examples = Faithfulness.statement_prompt["examples"]

context_recall.context_recall_prompt.instruction = ContextRecall.context_recall_prompt["instruction"]
context_recall.context_recall_prompt.output_format_instruction = ContextRecall.context_recall_prompt["output_format_instruction"]
context_recall.context_recall_prompt.examples = ContextRecall.context_recall_prompt["examples"]

context_precision.context_precision_prompt.instruction = ContextPrecision.context_precision_prompt["instruction"]
context_precision.context_precision_prompt.output_format_instruction = ContextPrecision.context_precision_prompt["output_format_instruction"]
context_precision.context_precision_prompt.examples = ContextPrecision.context_precision_prompt["examples"]

answer_correctness.correctness_prompt.instruction = AnswerCorrectness.correctness_prompt["instruction"]
answer_correctness.correctness_prompt.output_format_instruction = AnswerCorrectness.correctness_prompt["output_format_instruction"]
answer_correctness.correctness_prompt.examples = AnswerCorrectness.correctness_prompt["examples"]

# 定义大模型与embedding模型
llm = CustomLLM()
embedding = DashScopeEmbeddings(model="text-embedding-v3")

def ragas_evaluate(question:list[str],answer:list[str],contexts:list[list[str]],ground_truth:list[str]):
    data_samples = {
        'question': question,
        'answer': answer,
        'contexts' : contexts,
        'ground_truth': ground_truth
        }
    dataset = Dataset.from_dict(data_samples)
    score = evaluate(
        dataset = dataset,
        metrics=[answer_correctness,answer_relevancy, context_recall,context_precision,faithfulness],
        embeddings=embedding,
        llm=llm)
    df = score.to_pandas()
    return df
   