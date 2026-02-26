from r2egym.agenthub.runtime.base import ExecutionEnvironment
from r2egym.agenthub.runtime.docker import DockerRuntime
from r2egym.agenthub.runtime.factory import RuntimeFactory


def get_ags_runtime():
    from r2egym.agenthub.runtime.ags import AGSRuntime
    return AGSRuntime


def get_ags_config():
    from r2egym.agenthub.runtime.ags import AGSConfig
    return AGSConfig


__all__ = [
    "ExecutionEnvironment",
    "DockerRuntime",
    "RuntimeFactory",
    "get_ags_runtime",
    "get_ags_config",
]
