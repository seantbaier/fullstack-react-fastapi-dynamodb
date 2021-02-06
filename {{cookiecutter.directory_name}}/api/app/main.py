from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/ping")
def pong():
    return {"message": "pong"}


handler = Mangum(app)
