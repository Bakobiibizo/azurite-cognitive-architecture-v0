from fastapi import FastAPI, jsonify, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5001",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("localhost:5001/tts", methods=["POST"])
async def root():
    response = await app.post(
        "localhost:5001/tts", json={"text": "hello, how are you?"}
    )
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
