# main.py
from fastapi import FastAPI
from app.db.database import init_db

app = FastAPI()
init_db()

# Health check endpoint to verify if the app is active
@app.get("/test")
def read_test():
    return {"status": "active"}



# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
