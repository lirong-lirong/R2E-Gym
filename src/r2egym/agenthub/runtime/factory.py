"""Factory for creating runtime instances."""

from r2egym.agenthub.runtime.base import ExecutionEnvironment


class RuntimeFactory:
    """Factory class for creating runtime instances.

    Supports multiple backends:
    - docker: Local Docker runtime
    - kubernetes: Kubernetes-based runtime
    - ags: AGS (Agent Sandbox) via E2B SDK
    """

    @staticmethod
    def create(
        backend: str,
        ds: dict,
        logger=None,
        **kwargs
    ) -> ExecutionEnvironment:
        """Create a runtime instance based on the specified backend.

        Args:
            backend: Runtime backend ("docker", "kubernetes", or "ags")
            ds: Dataset entry containing task information
            logger: Logger instance
            **kwargs: Additional arguments passed to runtime constructor
                      (e.g., command). AGS config is always loaded from
                      environment variables automatically.

        Returns:
            ExecutionEnvironment instance

        Raises:
            ValueError: If unknown backend is specified
        """
        if backend in ["docker", "kubernetes"]:
            from r2egym.agenthub.runtime.docker import DockerRuntime
            return DockerRuntime(
                ds=ds,
                backend=backend,
                logger=logger,
                **kwargs
            )
        elif backend == "ags":
            from r2egym.agenthub.runtime.ags import AGSRuntime, AGSConfig

            # AGS config is always resolved from environment variables.
            # Callers do not need to pass ags_config -- this keeps the
            # RepoEnv interface clean and avoids leaking AGS-specific
            # details to upstream consumers (e.g., rllm).
            ags_config = AGSConfig.from_env()

            return AGSRuntime(
                ds=ds,
                config=ags_config,
                logger=logger,
                **kwargs
            )
        else:
            raise ValueError(
                f"Unknown backend: {backend}. "
                f"Supported backends: docker, kubernetes, ags"
            )
