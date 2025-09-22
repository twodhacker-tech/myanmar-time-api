from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def get_myanmar_time():
    # မြန်မာစံတော်ချိန်
    myanmar_tz = pytz.timezone("Asia/Yangon")
    now = datetime.now(myanmar_tz)
    
    return {
        "timezone": "Asia/Yangon",
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "hour": now.strftime("%H"),
        "minutes": now.strftime("%M"),
        "seconds": now.strftime("%S")
        "utc_offset": "+06:30"
    }
