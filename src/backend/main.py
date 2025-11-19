from api.healthcheck import router_healthcheck
from fastapi import FastAPI

app = FastAPI()

app.include_router(router_healthcheck)
