
from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="X337 Generated API"
)


app.include_router(router)
