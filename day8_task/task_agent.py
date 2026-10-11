"""Step 5: an agentic RAG helpdesk in LangGraph - tools + loop + memory."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import ast
import operator

from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from lc_config import get_model, get_vectorstore


COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

store = get_vectorstore()

MAX_DISTANCE = 0.25


@tool
def search_handbook(query: str) -> str:
    """Search the college handbook and return relevant passages."""

    results = store.similarity_search_with_score(query, k=3)

    matches = []

    for doc, score in results:
        print(f"DEBUG score={score:.3f}, source={doc.metadata['source']}")

        if score <= MAX_DISTANCE:
            matches.append(
                f"[{doc.metadata['source']}] {doc.page_content}"
            )

    if not matches:
        return "NO_MATCH: this is not covered in the college handbook"

    return "\n\n".join(matches)


@tool
def get_course_fee(course_code: str) -> str:
    """Return the fee for a course such as CS101, AI202 or DS303."""

    course_code = course_code.strip().upper()
    fee = COURSE_FEES.get(course_code)

    if fee is None:
        return f"Unknown course code {course_code}"

    return f"{course_code} fee is Rs. {fee}"


@tool
def check_exam_eligibility(attendance_percent: float) -> str:
    """Check exam eligibility based on attendance percentage."""

    if attendance_percent < 0 or attendance_percent > 100:
        return "Invalid attendance percentage. Enter a value from 0 to 100."

    elif attendance_percent >= 75:
        return "Eligible to write the exam."

    elif attendance_percent >= 65:
        return "Eligible with condonation. Fee: Rs. 500 per course."

    else:
        return "Not eligible to write the exam."


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


@tool
def calculator(expression: str) -> str:
    """Calculate simple arithmetic expressions."""

    def ev(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value

        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](ev(n.left), ev(n.right))

        raise ValueError("Only + - * / on numbers are allowed")

    try:
        return str(ev(ast.parse(expression, mode="eval").body))

    except Exception as e:
        return f"Error: {e}"


tools = [
    search_handbook,
    get_course_fee,
    check_exam_eligibility,
    calculator
]

model = get_model().bind_tools(tools)


SYSTEM = (
    "You are the Greenfield College helpdesk. "
    "Use search_handbook for college rules, policies, and handbook questions. "
    "Use get_course_fee for course fees. "
    "Use check_exam_eligibility for exam attendance questions. "
    "Use calculator for arithmetic. "
    "For factual questions, do not answer from general knowledge. "
    "If search_handbook returns NO_MATCH, say you don't know. "
    "Do not use outside knowledge to answer questions not covered by the handbook. "
    "Answer briefly and mention the source file when using handbook information."
)


def agent(state: MessagesState):
    """Read the conversation and either answer or request a tool."""

    reply = model.invoke([("system", SYSTEM)] + state["messages"])

    return {"messages": [reply]}


builder = StateGraph(MessagesState)

builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile(checkpointer=InMemorySaver())


def ask(question, thread_id):
    config = {
        "configurable": {"thread_id": thread_id},
        "recursion_limit": 10
    }

    print(f"\n[{thread_id}] USER: {question}")

    for step in graph.stream(
        {"messages": [("user", question)]},
        config,
        stream_mode="updates"
    ):
        for node, update in step.items():
            for msg in update["messages"]:

                if getattr(msg, "tool_calls", None):
                    for c in msg.tool_calls:
                        print(
                            f"   {node:6} -> call "
                            f"{c['name']}({c['args']})"
                        )

                elif node == "tools":
                    print(
                        f"   {node:6} -> {msg.name} "
                        f"returned {msg.content[:100]!r}"
                    )

                else:
                    print(f"   {node:6} -> ANSWER: {msg.content}")


if __name__ == "__main__":

    ask(
        "What CGPA do I need to be eligible for placements?",
        "task-run"
    )

    ask(
        "My attendance is 70%. Can I write the exam?",
        "task-run"
    )

    ask(
        "What is total of CS101 fee, AI202 fee and maximum late fee?",
        "task-run"
    )

    ask(
        "And if I pay only 5 days late instead?",
        "task-run"
    )

    ask(
        "What is capital of France?",
        "task-run"
    )
