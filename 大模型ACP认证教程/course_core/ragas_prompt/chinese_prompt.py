class AnswerRelavency:
    question_generation_prompt = {
        "instruction": "生成一个与给定答案相关的问题，并识别该答案是否模棱两可。如果答案模棱两可，则给它标记为 1；如果答案明确，则标记为 0。模棱两可的答案是指那些含糊其辞、回避或不明确的回答。例如，“我不知道”或“我不确定”都是模棱两可的答案。",
        "output_format_instruction": "输出应为符合以下 JSON schema 的格式良好的 JSON 实例。\n\n例如，对于 schema {\"properties\": {\"foo\": {\"title\": \"Foo\", \"description\": \"a list of strings\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"foo\"]}\n，对象 {\"foo\": [\"bar\", \"baz\"]} 是符合此 schema 的格式良好的实例。对象  {\"properties\": {\"foo\": [\"bar\", \"baz\"]}} 则不符合格式。\n\n以下是输出的 JSON schema：\n```\n{\"type\": \"object\", \"properties\": {\"question\": {\"title\": \"Question\", \"type\": \"string\"}, \"noncommittal\": {\"title\": \"Noncommittal\", \"type\": \"integer\"}}, \"required\": [\"question\", \"noncommittal\"]}\n```\n\n不要返回任何前言或解释，只返回用三个反引号（```）包围的纯 JSON 字符串。",
        "examples": [
            {
                "answer": "阿尔伯特·爱因斯坦出生在德国。",
                "context": "阿尔伯特·爱因斯坦是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的科学家之一。",
                "output": {
                    "question": "阿尔伯特·爱因斯坦出生在哪里？",
                    "noncommittal": 0
                }
            },
            {
                "answer": "它可以根据环境温度改变皮肤颜色。",
                "context": "最近的一项科学研究在亚马逊雨林中发现了一种新物种的青蛙，这种青蛙具有根据环境温度改变皮肤颜色的独特能力。",
                "output": {
                    "question": "新发现的青蛙物种有什么独特的能力？",
                    "noncommittal": 0
                }
            },
            {
                "answer": "珠穆朗玛峰",
                "context": "地球上从海平面计算的最高山峰，是位于喜马拉雅山脉的一座著名山峰。",
                "output": {
                    "question": "地球上最高的山是什么？",
                    "noncommittal": 0
                }
            },
            {
                "answer": "我不知道2023年发明的智能手机的突破性功能，因为我对2022年之后的信息不了解。",
                "context": "在2023年，一项突破性的发明被宣布：一款电池续航时间为一个月的智能手机，彻底改变了人们使用移动技术的方式。",
                "output": {
                    "question": "2023年发明的智能手机的突破性功能是什么？",
                    "noncommittal": 1
                }
            }
        ]
    }

class Faithfulness:
    nli_statements_message_prompt = {
        "instruction": "你的任务是根据给定的上下文判断一系列陈述的真实性。对于每个陈述，如果可以根据上下文直接推断出该陈述，则必须返回判定结果 1；如果不能根据上下文直接推断出该陈述，则必须返回判定结果 0。",
        "output_format_instruction": "输出应为符合以下 JSON 模式的格式良好的 JSON 实例。\n\n例如，对于模式 {\"properties\": {\"foo\": {\"title\": \"Foo\", \"description\": \"a list of strings\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"foo\"]}\n对象 {\"foo\": [\"bar\", \"baz\"]} 是该模式的格式良好的实例。对象 {\"properties\": {\"foo\": [\"bar\", \"baz\"]}} 格式不正确。\n\n输出的 JSON 模式如下：\n```\n{\"type\": \"array\", \"items\": {\"$ref\": \"#/definitions/StatementFaithfulnessAnswer\"}, \"definitions\": {\"StatementFaithfulnessAnswer\": {\"title\": \"StatementFaithfulnessAnswer\", \"type\": \"object\", \"properties\": {\"statement\": {\"title\": \"Statement\", \"description\": \"the original statement, word-by-word\", \"type\": \"string\"}, \"reason\": {\"title\": \"Reason\", \"description\": \"verdict理由\", \"type\": \"string\"}, \"verdict\": {\"title\": \"Verdict\", \"description\": \"faithfulness的verdict(0/1)。\", \"type\": \"integer\"}}, \"required\": [\"statement\", \"reason\", \"verdict\"]}}}\n```\n\n不返回任何前言或解释，仅返回由三个反引号（“```”）包围的纯 JSON 字符串。",
        "examples": [
            {
                "context": "John 是 XYZ 大学的一名学生。他正在攻读计算机科学学位。这个学期他选修了几门课程，包括数据结构、算法和数据库管理。John 是一个勤奋的学生，他花费了大量时间来学习和完成作业。他经常在图书馆熬夜做项目。",
                "statements": [
                    "John 主修生物学。",
                    "John 正在上人工智能课程。",
                    "John 是一个敬业的学生。",
                    "John 有一份兼职工作。"
                ],
                "answer": [
                    {
                        "statement": "John 主修生物学。",
                        "reason": "John 的专业明确提到是计算机科学。没有任何信息表明他主修生物学。",
                        "verdict": 0
                    },
                    {
                        "statement": "John 正在上人工智能课程。",
                        "reason": "上下文提到了 John 当前选修的课程，但没有提到人工智能。因此，不能推断出 John 正在上人工智能课程。",
                        "verdict": 0
                    },
                    {
                        "statement": "John 是一个敬业的学生。",
                        "reason": "上下文提到他花费了大量时间来学习和完成作业。此外，还提到他经常在图书馆熬夜做项目，这表明他很敬业。",
                        "verdict": 1
                    },
                    {
                        "statement": "John 有一份兼职工作。",
                        "reason": "上下文并没有提供有关 John 有兼职工作的任何信息。",
                        "verdict": 0
                    }
                ]
            },
            {
                "context": "光合作用是植物、藻类和某些细菌将光能转化为化学能的过程。",
                "statements": [
                    "阿尔伯特·爱因斯坦是个天才。"
                ],
                "answer": [
                    {
                        "statement": "阿尔伯特·爱因斯坦是个天才。",
                        "reason": "上下文和陈述是无关的",
                        "verdict": 0
                    }
                ]
            }
        ]
    }

    statement_prompt = {
        "instruction": "给定一个问题、一个答案和答案中的句子，分析在'sentences'中给出的每个句子的复杂性，并将每个句子分解成一个或多个完全可理解的陈述，同时确保每个陈述中不使用代词。将输出格式化为JSON。",
        "output_format_instruction": "输出应为符合以下 JSON 模式的格式良好的 JSON 实例。\n\n例如，对于模式 {\"properties\": {\"foo\": {\"title\": \"Foo\", \"description\": \"a list of strings\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"foo\"]}\n对象 {\"foo\": [\"bar\", \"baz\"]} 是该模式的格式良好的实例。对象 {\"properties\": {\"foo\": [\"bar\", \"baz\"]}} 格式不正确。\n\n输出的 JSON 模式如下：\n```\n{\"type\": \"array\", \"items\": {\"$ref\": \"#/definitions/Statements\"}, \"definitions\": {\"Statements\": {\"title\": \"Statements\", \"type\": \"object\", \"properties\": {\"sentence_index\": {\"title\": \"Sentence Index\", \"description\": \"Index of the sentence from the statement list\", \"type\": \"integer\"}, \"simpler_statements\": {\"title\": \"Simpler Statements\", \"description\": \"the simpler statements\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"sentence_index\", \"simpler_statements\"]}}}\n```\n\n不返回任何前言或解释，只返回一个由三重反引号（“```”）包围的纯 JSON 字符串。",
        "examples": [
            {
                "question": "阿尔伯特·爱因斯坦是谁，他以什么闻名？",
                "answer": "他是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的物理学家之一。他最出名的是发展了相对论理论，他还为量子力学理论的发展做出了重要贡献。",
                "sentences": "\n        0:他是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的物理学家之一。\n        1:他最出名的是发展了相对论理论，他还为量子力学理论的发展做出了重要贡献。\n        ",
                "analysis": [
                    {
                        "sentence_index": 0,
                        "simpler_statements": [
                            "阿尔伯特·爱因斯坦是一位德国出生的理论物理学家。",
                            "阿尔伯特·爱因斯坦被认为是有史以来最伟大和最有影响力的物理学家之一。"
                        ]
                    },
                    {
                        "sentence_index": 1,
                        "simpler_statements": [
                            "阿尔伯特·爱因斯坦最出名的是发展了相对论理论。",
                            "阿尔伯特·爱因斯坦还为量子力学理论的发展做出了重要贡献。"
                        ]
                    }
                ]
            }
        ]
    }




class ContextRecall:
    context_recall_prompt = {
        "instruction": "给定一个上下文和一个答案，分析答案中的每个句子，并判断该句子是否可以归因于给定的上下文。 仅使用 \"Yes\" (1) 或者 \"No\" (0) 作为二元分类。输出带理由的 json。",
        "output_format_instruction": "输出应该是格式良好的 JSON 实例，符合下面的 JSON 模式。\n\n例如，对于架构 {\"properties\": {\"foo\": {\"title\": \"Foo\", \"description\": \"a list of strings\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"foo\"]}\n对象 {\"foo\": [\"bar\", \"baz\"]} 是格式良好的架构实例。 对象 {\"properties\": {\"foo\": [\"bar\", \"baz\"]}} 格式不正确。\n\n以下是输出 JSON 模式：\n```\n{\"type\": \"array\", \"items\": {\"$ref\": \"#/definitions/ContextRecallClassificationAnswer\"}, \"definitions\": {\"ContextRecallClassificationAnswer\": {\"title\": \"ContextRecallClassificationAnswer\", \"type\": \"object\", \"properties\": {\"statement\": {\"title\": \"Statement\", \"type\": \"string\"}, \"attributed\": {\"title\": \"Attributed\", \"type\": \"integer\"}, \"reason\": {\"title\": \"Reason\", \"type\": \"string\"}}, \"required\": [\"statement\", \"attributed\", \"reason\"]}}}\n```\n\n不要返回任何前言或解释，只返回一个由三重反引号（```）包围的纯 JSON 字符串。",
        "examples": [
            {
                "question": "你能告诉我关于阿尔伯特·爱因斯坦的什么信息吗？",
                "context": "阿尔伯特·爱因斯坦（1879年3月14日 - 1955年4月18日）是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的科学家之一。他最出名的是发展了相对论理论，他还为量子力学做出了重要贡献，因此在20世纪前几十年现代物理学完成的科学理解自然的革命性重塑中，他是一个核心人物。他的质能等效公式E = mc²，源自相对论理论，被称为‘世界上最著名的方程’。他因‘对理论物理的贡献，特别是发现光电效应定律’而获得了1921年诺贝尔物理学奖，这是量子理论发展的关键一步。他的工作也因其对科学哲学的影响而闻名。在1999年英国《物理世界》杂志对世界130位顶级物理学家的民意调查中，爱因斯坦被评为有史以来最伟大的物理学家。他的智力成就和原创性使得爱因斯坦成为天才的代名词。",
                "answer": "阿尔伯特·爱因斯坦出生于1879年3月14日，是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的科学家之一。他因对理论物理的贡献而获得了1921年诺贝尔物理学奖。他在1905年发表了4篇论文。爱因斯坦于1895年搬到了瑞士。",
                "classification": [
                    {
                        "statement": "阿尔伯特·爱因斯坦出生于1879年3月14日，是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的科学家之一。",
                        "attributed": 1,
                        "reason": "爱因斯坦的出生日期在上下文中明确提到。"
                    },
                    {
                        "statement": "他因对理论物理的贡献而获得了1921年诺贝尔物理学奖。",
                        "attributed": 1,
                        "reason": "上下文中有确切的句子提到这一点。"
                    },
                    {
                        "statement": "他在1905年发表了4篇论文。",
                        "attributed": 0,
                        "reason": "上下文中没有提到他写的论文。"
                    },
                    {
                        "statement": "爱因斯坦于1895年搬到了瑞士。",
                        "attributed": 0,
                        "reason": "上下文中没有支持这一点的证据。"
                    }
                ]
            },
            {
                "question": "谁赢得了2020年国际板球理事会世界杯？",
                "context": "2022年国际板球理事会男子T20世界杯于2022年10月16日至11月13日在澳大利亚举行，这是该赛事的第八届比赛。原计划于2020年举行，但由于COVID-19疫情被推迟。英格兰队在决赛中击败巴基斯坦队，以五个小门的优势赢得了他们的第二个国际板球理事会男子T20世界杯冠军。",
                "answer": "英格兰",
                "classification": [
                    {
                        "statement": "英格兰赢得了2022年国际板球理事会男子T20世界杯。",
                        "attributed": 1,
                        "reason": "从上下文中可以清楚地看出英格兰击败了巴基斯坦赢得了世界杯。"
                    }
                ]
            },
            {
                "question": "太阳的主要燃料是什么？",
                "context": "NULL",
                "answer": "氢",
                "classification": [
                    {
                        "statement": "太阳的主要燃料是氢。",
                        "attributed": 0,
                        "reason": "上下文中没有任何信息。"
                    }
                ]
            }
        ]
    }


class ContextPrecision:
    context_precision_prompt = {
        "instruction": "给定问题、答案和上下文，验证上下文是否有助于得出给定的答案。 如果有 JSON 输出，则判定为 \"1\"，如果没有，则判定为 \"0\"",
        "output_format_instruction": "输出应该是格式良好的 JSON 实例，符合下面的 JSON 模式。\n\n例如，对于架构 {\"properties\": {\"foo\": {\"title\": \"Foo\", \"description\": \"a list of strings\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"foo\"]}\n对象 {\"foo\": [\"bar\", \"baz\"]} 是格式良好的架构实例。 对象 {\"properties\": {\"foo\": [\"bar\", \"baz\"]}} 格式不正确。\n\n以下是输出 JSON 模式：\n```\n{\"description\": \"Answer for the verification task wether the context was useful.\", \"type\": \"object\", \"properties\": {\"reason\": {\"title\": \"Reason\", \"description\": \"Reason for verification\", \"type\": \"string\"}, \"verdict\": {\"title\": \"Verdict\", \"description\": \"Binary (0/1) verdict of verification\", \"type\": \"integer\"}}, \"required\": [\"reason\", \"verdict\"]}\n```\n\n不要返回任何前言或解释，只返回一个由三重反引号（```）包围的纯 JSON 字符串。",
        "examples": [
            {
                "question": "你能告诉我关于阿尔伯特·爱因斯坦的什么信息吗？",
                "context": "阿尔伯特·爱因斯坦（1879年3月14日 – 1955年4月18日）是一位德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的科学家之一。他最出名的是发展了相对论理论，他还为量子力学做出了重要贡献，因此在20世纪前几十年现代物理学完成的科学理解自然的革命性重塑中，他是一个核心人物。他的质能等效公式E = mc²，源自相对论理论，被称为“世界上最著名的方程”。他因“对理论物理的贡献，特别是发现光电效应定律”而获得了1921年诺贝尔物理学奖，这是量子理论发展的关键一步。他的工作也因其对科学哲学的影响而闻名。在1999年英国《物理世界》杂志对世界130位顶级物理学家的民意调查中，爱因斯坦被评为有史以来最伟大的物理学家。他的智力成就和原创性使得爱因斯坦成为天才的代名词。",
                "answer": "阿尔伯特·爱因斯坦出生于1879年3月14日，是德国出生的理论物理学家，被广泛认为是有史以来最伟大和最有影响力的科学家之一。他因对理论物理的贡献获得了1921年诺贝尔物理学奖。他在1905年发表了4篇论文。爱因斯坦于1895年搬到了瑞士。",
                "verification": {
                    "reason": "提供的上下文确实有助于得出给定的回答。上下文包括关于阿尔伯特·爱因斯坦的生活和贡献的关键信息，这些信息在回答中得以体现。",
                    "verdict": 1
                }
            },
            {
                "question": "谁赢得了2020年国际板球理事会世界杯？",
                "context": "2022年国际板球理事会男子T20世界杯于2022年10月16日至11月13日在澳大利亚举行，这是该赛事的第八届比赛。原计划于2020年举行，但由于COVID-19疫情被推迟。英格兰队在决赛中击败巴基斯坦队，以五个小门的优势赢得了他们的第二个国际板球理事会男子T20世界杯冠军。",
                "answer": "英格兰",
                "verification": {
                    "reason": "上下文有助于澄清2020年国际板球理事会世界杯的情况，并指出英格兰是原定于2020年举行但实际在2022年进行的比赛的冠军。",
                    "verdict": 1
                }
            },
            {
                "question": "世界上最高的山是什么？",
                "context": "安第斯山脉是世界上最长的大陆山脉，位于南美洲。它横跨七个国家，拥有西半球许多最高的山峰。该山脉以其多样的生态系统而闻名，包括高海拔的安第斯高原和亚马逊雨林。",
                "answer": "珠穆朗玛峰。",
                "verification": {
                    "reason": "提供的上下文讨论了安第斯山脉，虽然令人印象深刻，但不包括珠穆朗玛峰或直接与关于世界最高山峰的问题相关。",
                    "verdict": 0
                }
            }
        ]
    }


class AnswerCorrectness:
    correctness_prompt = {
        "instruction": "给定ground_truth和answer分解后的陈述，分析每个陈述并将它们归类为以下类别之一：\n\n- TP（真正例）：answer中存在的陈述，并且直接得到ground_truth中的一个或多个陈述的支持，\n- FP（假正例）：answer中存在但未得到ground_truth中任何陈述直接支持的陈述，\n- FN（假负例）：在ground_truth中存在但answer中不存在的陈述。\n\n每个陈述只能属于TP、FP、FN其中一个类别。请提供你分类的原因。",
        "output_format_instruction": "输出应该是格式正确的 JSON 实例，符合下面的 JSON 模式。\n\n例如，对于架构 {\"properties\": {\"foo\": {\"title\": \"Foo\", \"description\": \"a list of strings\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"foo\"]}\n对象 {\"foo\": [\"bar\", \"baz\"]} 是格式良好的架构实例。 对象 {\"properties\": {\"foo\": [\"bar\", \"baz\"]}} 格式不正确。\n\n以下是输出 JSON 模式：\n```\n{\"type\": \"object\", \"properties\": {\"TP\": {\"title\": \"Tp\", \"type\": \"array\", \"items\": {\"type\": \"object\"}}, \"FP\": {\"title\": \"Fp\", \"type\": \"array\", \"items\": {\"type\": \"object\"}}, \"FN\": {\"title\": \"Fn\", \"type\": \"array\", \"items\": {\"type\": \"object\"}}}, \"required\": [\"TP\", \"FP\", \"FN\"]}\n```\n\n不要返回任何前言或解释，只返回一个由三重反引号（```）包围的纯 JSON 字符串。",
        "examples": [
            {
                "question": "太阳的动力来源是什么，它的主要功能是什么？",
                "answer": ["太阳的动力来源是核裂变，类似于地球上的核反应堆。", "太阳的主要功能是为太阳系提供光。"],
                "ground_truth": ["太阳的动力来源是核聚变，氢原子聚变形成氦。", "太阳核心的这种聚变过程释放出巨大的能量。", "太阳的能量提供了热和光，这是地球生命必需的。", "太阳的光在地球的气候系统中起着关键作用。", "阳光有助于驱动天气和海洋洋流。"],
                "classification": {
                    "TP": [
                        {
                            "statement": "太阳的主要功能是为太阳系提供光。",
                            "reason": "这个陈述在某种程度上得到了地面真相的支持，地面真相提到了太阳提供光及其作用，尽管它更广泛地关注太阳的能量。"
                        }
                    ],
                    "FP": [
                        {
                            "statement": "太阳的动力来源是核裂变，类似于地球上的核反应堆。",
                            "reason": "该陈述是不正确的，与地面真相相矛盾，地面真相表明太阳的动力来源是核聚变。"
                        }
                    ],
                    "FN": [
                        {
                            "statement": "太阳的动力来源是核聚变，氢原子聚变形成氦。",
                            "reason": "这个对太阳动力来源的准确描述没有包含在答案中。"
                        },
                        {
                            "statement": "太阳核心的这种聚变过程释放出巨大的能量。",
                            "reason": "这个过程及其重要性没有在答案中提到。"
                        },
                        {
                            "statement": "太阳的能量提供了热和光，这是地球生命必需的。",
                            "reason": "答案中只提到光，忽略了热及其对生命的必要性，这是地面真相涵盖的内容。"
                        },
                        {
                            "statement": "太阳的光在地球的气候系统中起着关键作用。",
                            "reason": "太阳光对地球气候系统的更广泛影响没有在答案中提到。"
                        },
                        {
                            "statement": "阳光有助于驱动天气和海洋洋流。",
                            "reason": "阳光对天气模式和海洋洋流的影响在答案中被遗漏了。"
                        }
                    ]
                }
            },
            {
                "question": "水的沸点是多少？",
                "answer": ["水的沸点是在海平面上100摄氏度。"],
                "ground_truth": ["水的沸点是在海平面上100摄氏度（212华氏度）。", "水的沸点会随着海拔的变化而改变。"],
                "classification": {
                    "TP": [
                        {
                            "statement": "水的沸点是在海平面上100摄氏度。",
                            "reason": "这个陈述直接得到了地面真相的支持，地面真相明确指出水的沸点是在海平面上100摄氏度。"
                        }
                    ],
                    "FP": [],
                    "FN": [
                        {
                            "statement": "水的沸点会随着海拔的变化而改变。",
                            "reason": "关于水的沸点会随着海拔变化而改变的附加信息没有在答案中提到。"
                        }
                    ]
                }
            }
        ]
    }

