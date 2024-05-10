import uvicorn
from fastapi import FastAPI
from responses import TrendItem
from service import get_trends_mongo, save_trends








# This method can only be used with a basic access level account,
# which is a paid service


app = FastAPI()

@app.get("/trends", response_model=list[TrendItem])
def get_trends_route():
    return get_trends_mongo()
if __name__ == "__main__":
    trends = get_trends_mongo()
    if not trends:
        save_trends()
    uvicorn.run(app, host="0.0.0.0", port=8000)