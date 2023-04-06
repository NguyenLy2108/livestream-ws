import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from load_route import ROUTE_LIST

app = FastAPI(
    title="Log Service"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for route in ROUTE_LIST:
    app.include_router(route['route'], tags=route['tags'], prefix=route['prefix'])

@app.get("/",tags = ["Welcome"])
async def welcome():
    return {"message":"Welcome to logs service "}
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)