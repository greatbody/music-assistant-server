"""Resolve user-provided service credentials for this third-party build."""

import os


def app_var(index: int) -> str:
    """Return the credential provided for the requested upstream index."""
    return os.environ.get(f"MASS_APP_VAR_{index}", "")
