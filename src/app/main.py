from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.users import router as users_router
from app.routers.schemas import HealthResponse

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="OK")

app.include_router(users_router)
