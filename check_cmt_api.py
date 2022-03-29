from sys import prefix
import uvicorn
import time
from database.redisdb import redis
from fastapi import FastAPI, Request
from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from services.toxic_comments.route import router as ToxicComments
from services.check_toxic_comment.route import router as CheckToxiComments
app = FastAPI(
    title="Check Toxic Comment"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(ToxicComments, tags = ['Toxic Comments'], prefix = "/toxic_comments")
app.include_router(CheckToxiComments, tags = ['Check Toxic Comments'], prefix = "/check_toxic_comments")

@app.get("/",tags = ["Welcome"])
async def welcome():
    return {"message":"welcome to my app "}
if __name__ == "__main__":
    uvicorn.run("check_cmt_api:app", reload=True)