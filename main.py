from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome(): 
    return {
        'message':'hello every body'
    }

