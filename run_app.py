from app.main import app
import uvicorn  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

#uvicorn run_app:app --reload