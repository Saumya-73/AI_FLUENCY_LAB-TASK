# Day 6 Task – Reliable Tool Calling

## 1. Scenario

I created a simple **College Canteen Assistant**.

The assistant can:

- Get the price of a food item.
- Calculate a canteen bill.

The tools used are:

1. `get_food_price`
2. `calculate_bill`

Food data used:

| Food | Price |
|---|---:|
| idly | ₹30 |
| dosa | ₹50 |
| fried_rice | ₹80 |

The `meal_type` argument uses an enum:

- breakfast
- lunch
- dinner

---

# 2. Chat Completions Request and Response

A Chat Completions request contains important fields such as:

- `model` – specifies the model.
- `messages` – contains the conversation.
- `tools` – describes the functions available to the model.
- `tool_choice` – controls whether the model can choose tools.
- `max_tokens` – controls the maximum output length.

A response contains information such as:

- `choices`
- `message`
- `content`
- `tool_calls`
- `finish_reason`

Important `finish_reason` values include:

- `stop` – the model finished normally.
- `length` – the response was truncated.
- `tool_calls` – the model requested tool calls.

When the model requests a tool, the `content` can be empty because the important information is inside `tool_calls`.

---

# 3. OpenAI-Compatible Servers

OpenAI-compatible servers provide an API interface that follows a similar request and response format.

Examples include:

- Groq
- Ollama
- vLLM
- Hugging Face

In this project I used **Groq**.

The main provider-specific change was the API configuration:

```python
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)