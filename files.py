import os
from pathlib import Path

#creates needed dir if not exist
try:
    os.makedirs(Path(__file__).parent / "youtube/data")
    youtubeData = Path(__file__).parent / "youtube/data"
except:
    youtubeData = Path(__file__).parent / "youtube/data"
    
try:
    os.makedirs(Path(__file__).parent / "twitter/data")
    twitterData = Path(__file__).parent / "twitter/data"
except:
    twitterData = Path(__file__).parent / "twitter/data"

try:
    os.makedirs(Path(__file__).parent / "chicago/data")
    chicagoData = Path(__file__).parent / "chicago/data"
except:
    chicagoData = Path(__file__).parent / "chicago/data"