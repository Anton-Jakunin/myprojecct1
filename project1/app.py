from fastapi import FastAPI
app = FastAPI()
@app.get("/sergey")
def read_root():
    return{"Hello":"World"}