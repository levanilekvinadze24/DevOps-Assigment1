from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "OK", "service": "DevOps-Assigment1"}

