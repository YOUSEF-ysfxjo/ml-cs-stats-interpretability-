import json
import os
import pathlib
from joblib import dump, load

def load_config(config_path: str = "configs/config.json") -> dict:
    """Load configuration from JSON file."""
    with open(config_path, "r") as f:
        config = json.load(f)
    return config

def ensure_dir(full_path: str ):
    """Ensure directory exists."""
    dir_path = os.path.dirname(full_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

def save_artifact(obj: object, full_path: str = "artifact.joblib"):
    """Save artifact."""
    ensure_dir(full_path)
    dump(obj, pathlib.Path(full_path))

def load_artifact(full_path: str = "artifact.joblib") -> object:
    """Load artifact."""
    return load(pathlib.Path(full_path))
