"""
Main entrypoint for the rustarium package.

This module provides the executable routine when the package is run directly
via the command line (e.g., ``python -m rustarium``). It initializes the logger
and settings, outputting the current version and configuration to verify
the installation and environment setup.
"""

from __future__ import annotations

import click

from rustarium import (
    LoggingSettings,
    Settings,
    __version__,
    configure_logger,
    logger,
)

__all__ = ["main"]


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="rustarium")
def main() -> None:
    """
    Execute the main routine.

    Initializes application settings and logging, demonstrating the basic startup
    flow of the application. It logs the current version and the loaded configuration
    settings.

    Example:
        .. code-block:: python

            from rustarium.__main__ import main

            main()
    """
    configure_logger(
        LoggingSettings(
            enabled=True,
            level="INFO",
            clear_loggers=True,
            filter=("rustarium", "__main__"),
        )
    )
    logger.info("Hello from rustarium v{}!", __version__)
    settings = Settings()
    logger.info("Settings: {}", settings)


if __name__ == "__main__":
    main()
