from fastapi import FastAPI


app = FastAPI()



@app.get("/hello")
def ping():
    return {"message": "pong"}