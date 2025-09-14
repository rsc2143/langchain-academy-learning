import getpass
import os

def _set_var(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_var("OPENAI_API_KEY")
_set_var("LANGSMITH_API_KEY")
_set_var("LANGSMITH_PROJECT")
_set_var("LANGSMITH_TRACING")

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "langchain-academy"
os.environ["LANGSMITH_TRACING"] = "true"