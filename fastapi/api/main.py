from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello World 🌍"}

@app.get("/test")
def read_root():
    return {"Fast API running 🚀"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8000, log_level="info")