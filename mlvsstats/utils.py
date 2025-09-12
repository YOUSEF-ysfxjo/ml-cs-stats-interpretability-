import json
import os
from joblib import dump, load
import numpy as np
from sklearn.ensemble import RandomForestClassifier
def load_config():
    """Load configuration from JSON file."""
    with open("configs/config.json", "r") as f:
        config = json.load(f)
    return config

def ensure_dir(dir_path):
    """Ensure directory exists."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

def save_artifacts(obj, dir_path):
    """Save artifacts."""
    ensure_dir(dir_path)
    