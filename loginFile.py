import os
from pathlib import Path

#creates needed dir if not exist
try:
    os.makedirs(Path(__file__).parent / "")
    homeDir = Path(__file__).parent / ""
except:
    homeDir = Path(__file__).parent / ""
