# Agentic AI: Foundations and Open-Source Practice – Day 2

## 1. Scenario

For this task, I chose a course-fee and scholarship scenario.

The first question asks which option is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship. The course fees are obtained using tools in the ReAct agent. The other questions involve calculations and logical reasoning using information already given in the question.

This scenario allows direct prompting, Chain-of-Thought prompting, and ReAct to be compared on reasoning, tool use, reliability, transparency, speed, and consistency.

## 2. Direct Prompting

Direct prompting asks the model for an answer without explicitly requesting step-by-step reasoning. The model gives a final answer directly.

For this task, direct prompting worked well for questions where all the required information was already provided. For example, the instalment question, the computer-sittings question, and the height-ordering question were answered correctly.

However, direct prompting does not use the course-fee tool. When information must be obtained from an external source or tool, direct prompting by itself cannot perform that lookup in this setup.

The main limitation in this scenario is therefore the lack of external tool access. It can answer from the information supplied in the prompt, but it cannot independently retrieve course fees from the tool.

## 3. Chain-of-Thought Prompting

Chain-of-Thought prompting asks the model to solve a problem step by step before giving the final answer.

In my experiment, all three reasoning questions were answered correctly both with and without the step-by-step prompt. With CoT, the model showed intermediate calculations or logical steps before the final answer.

For example, for the scholarship instalment question, the model first calculated the total course cost, then calculated the scholarship amount, then calculated the remaining amount, and finally divided it into four instalments.

CoT can therefore make multi-step reasoning easier to follow and can help organize calculations. However, CoT still does not provide external tool access. It cannot obtain missing course fees from the course-fee tool on its own.

## 4. ReAct Agent

ReAct combines reasoning with actions and observations. The agent first determines what information or operation is needed, then calls a tool, receives the result, and continues until it can produce a final answer.

In my experiment, the ReAct agent called the course-fee tool for CS101, AI202, and DS303. It then used the available information to calculate the discounted totals and compare the two options.

The agent produced the correct final answer: CS101 and AI202 with a 10% scholarship are cheaper by ₹6,750.

The main advantage of ReAct in this scenario is that it can obtain information through tools before answering. Its limitation is that tool use adds additional steps and can make the process slower and more complex than direct prompting.

## 5. Comparison Table

| Basis for comparison | Direct prompting | Chain-of-Thought | ReAct agent |
|---|---|---|---|
| Reasoning depth | Basic/direct answer | More structured step-by-step reasoning | Reasoning combined with actions and observations |
| Tool usage | No tool usage | No tool usage in this experiment | Uses tools when external information is needed |
| Reliability on multi-step questions | Can work, but may make calculation mistakes | Better structured for multi-step reasoning | Can combine reasoning with verified tool results |
| Transparency | Final answer is visible, but reasoning is not shown | Intermediate steps are shown in the response | Actions and tool observations can be observed |
| Speed / cost | Usually fastest and shortest | Longer response and more tokens | Extra tool calls make it slower and more costly |
| Consistency across repeated runs | Depends on temperature and prompting | Can vary at non-zero temperature | Can also vary depending on model and tool calls |

## 6. Self-Consistency Observation

I used the course-instalment question for the self-consistency experiment.

At temperature 0.8, all five runs produced the mathematically correct answer of ₹9,562.50, but the wording and formatting were different. Because my program compared the exact answer strings, the majority count was only 1 out of 5 even though all five answers represented the same numerical answer.

When I changed the temperature to 0, all five runs produced the same output. The majority was therefore 5 out of 5.

This experiment shows that non-zero temperature can produce different answer variations, while temperature 0 produced a much more repeatable result in this experiment.

## 7. Suitability Analysis

For this particular scenario, the ReAct approach is the most suitable because one part of the problem requires external course-fee information. ReAct can call the course-fee tool, use the returned observations, and then calculate the final comparison.

Direct prompting is suitable when the required information is already available and only a short answer is needed. Chain-of-Thought is useful when a problem mainly requires careful multi-step reasoning but does not require external information.

The self-consistency experiment also showed that repeated sampling at a non-zero temperature can produce different forms of the same answer. Therefore, when consistency is important, the final answers should ideally be normalized before voting rather than compared only as exact strings.

## 8. Conclusion

Direct prompting is appropriate for simple questions where the required information is already available and a quick final answer is sufficient.

Chain-of-Thought is useful for problems that require several reasoning or calculation steps and where explaining the intermediate process is useful.

ReAct is appropriate for problems that require both reasoning and interaction with external tools or information sources. It combines Thought, Action, and Observation so that the agent can obtain information and use it before producing a final answer.

The experiments in this task demonstrated that the three approaches have different strengths. Direct prompting was concise, Chain-of-Thought provided structured reasoning, and ReAct was able to use tools to solve a scenario involving external information.