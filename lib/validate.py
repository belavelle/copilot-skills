from __future__ import annotations
from pathlib import Path

def require_nonempty(value: str, name: str) -> str:
    if not value:
        raise ValueError(f"{name} must be non-empty")
    return value

def safe_path(path: Path) -> Path:
    if ".." in path.parts:
        raise ValueError(f"Unsafe path: {path}")
    return path
