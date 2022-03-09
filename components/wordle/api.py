from imp import reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://127.0.0.1:8000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

answer = "sahil"


@app.get("/{attempt}")
def root(attempt: str):
    attempt = attempt.lower()
    d = {0: "", 1: "", 2: "", 3: "", 4: ""}
    for i in range(5):
        if attempt[i] == answer[i]:
            d[i] += "g"
        elif attempt[i] in answer:
            d[i] += "y"
        else:
            d[i] += "w"
    return d
