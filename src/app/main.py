from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.users import router as users_router
import app.db 

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     await engine.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await engine.disconnect()

@app.get("/")
def read_root():
    return "web server is running" 

app.include_router(users_router)
