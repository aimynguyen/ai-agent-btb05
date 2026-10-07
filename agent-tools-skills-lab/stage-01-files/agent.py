"""LangChain agent của stage 01: read_file, write_file."""

from urllib.parse import urlparse

from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware, ToolCallLimitMiddleware
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from config import MODEL_CALL_LIMIT, TOOL_CALL_LIMIT, Settings
from observer import ObserverMiddleware
from prompts import build_system_prompt
from tools import list_files, read_file, write_file

TOOLS = [list_files, read_file, write_file]


def build_model(settings: Settings) -> BaseChatModel:
    if settings.base_url:
        endpoint = urlparse(settings.base_url)
        if endpoint.hostname == "generativelanguage.googleapis.com" and endpoint.path.rstrip("/").endswith("/openai"):
            return ChatGoogleGenerativeAI(model=settings.model_name, api_key=settings.api_key)

    kwargs = {"model": settings.model_name, "api_key": settings.api_key}
    if settings.base_url:
        kwargs["base_url"] = settings.base_url
    return ChatOpenAI(**kwargs)


def system_prompt() -> str:
    return build_system_prompt()


def capabilities() -> dict:
    return {"tools": [t.name for t in TOOLS], "skills": [], "skill_diagnostics": []}


def build_agent(model):
    return create_agent(
        model=model,
        tools=TOOLS,
        system_prompt=system_prompt(),
        middleware=[
            ModelCallLimitMiddleware(run_limit=MODEL_CALL_LIMIT, exit_behavior="end"),
            ToolCallLimitMiddleware(run_limit=TOOL_CALL_LIMIT),
            ObserverMiddleware(),  # cuối danh sách = sát model/tool invocation nhất
        ],
    )
