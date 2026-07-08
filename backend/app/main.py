from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return{
        "message":"Startup Intelligence Platform is running!"
    }

