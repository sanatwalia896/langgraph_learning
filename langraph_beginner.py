## this is the begginer part of learning langgraph , make sure to be well versed with langchain

# LangGraph is built on top of LangChain and completely interoperable with the LangChain ecosystem. It adds new value primarily through the introduction of an easy way to create cyclical graphs. This is often useful when creating agent runtimes.
# One of the common patterns we see when people are creating more complex LLM applications is the introduction of cycles into the runtime. These cycles often use the LLM to reason about what to do next in the cycle. A big unlock of LLMs is the ability to use them for these reasoning tasks. This can essentially be thought of as running an LLM in a for-loop. These types of systems are often called agents.

from typing import TypedDict
from langgraph.graph import StateGraph


class State(TypedDict):
    messages: list
    user_input: str
    current_task: str


# Nodes are the functions that operate on the state
def greet_user(state: State) -> State:
    state["messages"].append("Hello, how can I help you?")
    return state


graph_builder = StateGraph(State)
# Add edges to define flow like
graph_builder.add_edge("start", "greet_user")
graph_builder.add_conditional_edge(
    "handle_input", lambda state: "end" if state["user_input"] == "exit" else "next"
)
