from fastapi import FastAPI

from backend.api.healthcheck import router_healthcheck

app = FastAPI()

app.include_router(router_healthcheck)
