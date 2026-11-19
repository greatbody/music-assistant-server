"""Resolve user-provided service credentials for this third-party build."""

import os
from typing import Any


def app_var(index: int) -> Any:
    """Return the credential provided for the requested upstream index."""
    return os.environ.get(f"MASS_APP_VAR_{index}", "")
