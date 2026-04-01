from fastapi import FastAPI
import httpx
app = FastAPI()

@app.get("/ok") 
async def root(): 
		return {"message": "Hello World"}