from lab.config import make_llm
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition


def add_numbers(a: int, b: int) -> int:
    """두 정수 a와 b를 더합니다."""
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """두 정수 a와 b를 곱합니다."""
    return a * b


llm = make_llm()

tools = [add_numbers, multiply_numbers]
tool_llm = llm.bind_tools(
    tools,
    parallel_tool_calls=False,
)


system = SystemMessage(
    content=(
        "계산은 제공된 도구를 사용하세요. "
        "도구 결과를 확인하고 필요한 계산을 이어서 수행하세요. "
        "계산이 끝나면 한국어로 답하세요. "
        "이전 결과를 모르면 추측하지 말고 물어보세요."
    )
)


def assistant(state: MessagesState):
    messages = [system] + state["messages"]
    response = tool_llm.invoke(messages)

    return {"messages": [response]}


builder = StateGraph(MessagesState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)

# 도구 결과를 모델에게 돌려보냅니다.
builder.add_edge("tools", "assistant")


# 서버가 상태 저장을 관리합니다.
graph = builder.compile()
