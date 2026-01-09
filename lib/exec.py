from __future__ import annotations
import subprocess
from typing import Sequence

def run_cmd(cmd: Sequence[str], *, check: bool = True) -> subprocess.CompletedProcess:
    """Run a command safely without shell=True."""
    return subprocess.run(cmd, check=check, text=True, capture_output=True)
