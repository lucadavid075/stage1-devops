from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"message": "healthy"}

@app.get("/me")
def me():
    return {
        "name": "David Luke",
        "email": "daiveedlucas049@gmail.com",
        "github": "https://github.com/lucadavid075"
    }