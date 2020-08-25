import os
from pathlib import Path

try:
    os.makedirs(Path(__file__).parent / "data")
    chicagoData = Path(__file__).parent / "data"
except:
    chicagoData = Path(__file__).parent / "data"