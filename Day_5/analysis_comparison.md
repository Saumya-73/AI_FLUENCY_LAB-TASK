# Day 5 - Analysis Comparison

## Objective

To compare two cloud-hosted language models using the same prompts and observe their response time, instruction following, and answer quality.

## Provider

Groq Cloud API

## Models Compared

1. `openai/gpt-oss-20b`
2. `openai/gpt-oss-120b`

## Prompt 1 - Exact Instruction

**Prompt:** Reply with exactly: OK

### gpt-oss-20b

- Time: 0.77 seconds
- Answer: OK

### gpt-oss-120b

- Time: 0.41 seconds
- Answer: OK

**Observation:** Both models followed the exact instruction correctly. The 120B model was faster in this run.

## Prompt 2 - AI Agent Explanation

**Prompt:** In two sentences, what is an AI agent?

### gpt-oss-20b

- Time: 0.61 seconds

The model explained how an AI agent perceives its environment, processes information, takes actions toward goals, and adapts its behavior.

### gpt-oss-120b

- Time: 0.61 seconds

The model explained how an AI agent receives data, processes information, takes actions toward goals, and can operate autonomously or semi-autonomously.

**Observation:** Both models provided relevant explanations. Their recorded response times were equal in this run.

## Prompt 3 - Scholarship Calculation

**Prompt:** A course costs Rs. 18,000 with a 15% scholarship. What is payable? Show the steps.

### gpt-oss-20b

- Time: 0.72 seconds
- Scholarship amount: Rs. 2,700
- Payable amount: Rs. 15,300

### gpt-oss-120b

- Time: 1.23 seconds
- Scholarship amount: Rs. 2,700
- Payable amount: Rs. 15,300

**Calculation:**

Scholarship = 15% × Rs. 18,000 = Rs. 2,700

Payable amount = Rs. 18,000 − Rs. 2,700 = **Rs. 15,300**

**Observation:** Both models calculated the scholarship and final payable amount correctly. The 20B model was faster in this run.

## Overall Comparison

| Prompt | GPT-OSS-20B | GPT-OSS-120B | Faster model |
|---|---:|---:|---|
| Exact instruction | 0.77 s | 0.41 s | 120B |
| AI agent explanation | 0.61 s | 0.61 s | Same recorded time |
| Scholarship calculation | 0.72 s | 1.23 s | 20B |

Both models followed the instructions and produced relevant answers. Response times varied by prompt. These results represent one benchmark run, and timings may vary between runs.

## Important Note

This implementation uses the Groq Cloud API instead of local Ollama because Ollama was not installed.

Local Ollama measurements, including model loading time, model size on disk, and local memory usage, were not collected.

The recorded times are cloud API response times, not local inference times.

## Conclusion

The comparison demonstrated how two cloud-hosted language models can be evaluated using identical prompts. Both models answered the three test prompts correctly, but their response times differed across tasks.

These results describe the observed run and should not be treated as a universal ranking of model performance.