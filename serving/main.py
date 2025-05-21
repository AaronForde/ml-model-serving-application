from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Literal
from enum import Enum

# scehmas for request bodies, responses bodies and error responses.
class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class CompletionRequest(BaseModel):
    messages: List[Message]

class ModelGetResponse(BaseModel):
    model_id: str 

class getStatusResponse(BaseModel):
    status: Literal["NOT_DEPLOYED", "PENDING", "DEPLOYING", "RUNNING"]

class ModelPostResponse(BaseModel):
    status: Literal["success"]
    model_id: str 
class CompletionResponse(BaseModel):
    status: Literal["success"]
    response: List[dict]
class ErrorResponse(BaseModel):
    status: Literal["error"]
    message: str

app = FastAPI()


@app.post("/completion", response_model=CompletionResponse, responses={
    200: {"model": CompletionResponse},
    400: {"model": ErrorResponse},
})
async def completion(request: CompletionRequest):
    if not request.messages:
        raise HTTPException(status_code=400, detail="No messages provided")
    
    return CompletionResponse(status="success", response=response)


@app.get("/status", response_model=getStatusResponse, responses={
    200: {"model": getStatusResponse},
    400: {"model": ErrorResponse},})
async def getStatus():
    return getStatusResponse 


@app.get("/model", response_model=ModelGetResponse, responses={
    200: {"model": ModelGetResponse},
    400: {"model": ErrorResponse},})
async def getModel():
    return ModelGetResponse

@app.post("/model", response_model=ModelPostResponse, responses={
    200: {"model": ModelPostResponse} ,
    400: {"model": ErrorResponse}
    })
async def postModel():
    return ModelPostResponse

