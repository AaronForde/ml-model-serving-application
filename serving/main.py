from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/dashboard", response_class=JSONResponse)
def dashboard():
    # Pass data to template
    return templates.TemplateResponse("dashboard.html", {
        
    })

@app.post("/completion", response_class=JSONResponse, responses={
    200: { "status": "success", "response": [ {"role": "assistant", "message": "response"} ] } ,
    400: { "status": "error", "message": "error message" }})
async def completion():
    return {"message": "post Completion"}

@app.get("/status", response_class=JSONResponse)
async def getStatus():
    return { "status": "NOT_DEPLOYED" | "PENDING" | "DEPLOYING" | "RUNNING" } 

@app.get("/model", response_class=JSONResponse)
async def getModel():
    return { "model_id": "model name" } 

@app.post("/model", response_class=JSONResponse, responses={
    200: { "status": "success", "model_id": "model name"} ,
    400: { "status": "success", "model_id": "model name"}})
async def postModel():
    return {"message": "postModel"}

