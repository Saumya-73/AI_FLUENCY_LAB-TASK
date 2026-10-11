# Day 5 - Model Comparison

## Objective

To compare two cloud-hosted language models using the same prompts and observe their response time, instruction following, and answer quality.

## Provider

Groq Cloud API

## Models Compared

1. `openai/gpt-oss-20b`
2. `openai/gpt-oss-120b`

## Prompt 1 - Exact Instruction

**Prompt:**

Reply with exactly: OK

### gpt-oss-20b

- Time: 0.77 seconds
- Answer: OK

### gpt-oss-120b

- Time: 0.41 seconds
- Answer: OK

**Observation:** Both models followed the exact instruction correctly. The 120B model was faster for this prompt.

## Prompt 2 - AI Agent Explanation

**Prompt:**

In two sentences, what is an AI agent?

### gpt-oss-20b

- Time: 0.61 seconds

The model explained that an AI agent perceives its environment, processes information, takes actions toward goals, and can adapt its behavior.

### gpt-oss-120b

- Time: 0.61 seconds

The model explained that an AI agent receives data, processes it using models or algorithms, takes actions toward specific goals, and can operate autonomously or semi-autonomously.

**Observation:** Both models provided relevant explanations and followed the two-sentence instruction. Both recorded the same response time in this run.

## Prompt 3 - Scholarship Calculation

**Prompt:**

A course costs Rs. 18,000 with a 15% scholarship. What is payable? Show the steps.

### gpt-oss-20b

- Time: 0.72 seconds
- Scholarship amount: Rs. 2,700
- Final payable amount: Rs. 15,300

### gpt-oss-120b

- Time: 1.23 seconds
- Scholarship amount: Rs. 2,700
- Final payable amount: Rs. 15,300

**Calculation:**

Scholarship = 15% × Rs. 18,000 = Rs. 2,700

Payable amount = Rs. 18,000 − Rs. 2,700 = **Rs. 15,300**

**Observation:** Both models correctly calculated the scholarship and final payable amount. The 20B model was faster for this prompt.

## Overall Comparison

| Test prompt | GPT-OSS-20B | GPT-OSS-120B | Faster model |
|---|---:|---:|---|
| Exact instruction | 0.77 s | 0.41 s | 120B |
| AI agent explanation | 0.61 s | 0.61 s | Same recorded time |
| Scholarship calculation | 0.72 s | 1.23 s | 20B |

Both models followed the instructions and produced relevant answers. The response times varied by prompt, so the larger model was not always faster.

These measurements represent one benchmark run. Response times may vary between runs.

## Important Note

This Day 5 implementation uses the Groq Cloud API instead of local Ollama because