from fastapi import APIRouter

router_healthcheck = APIRouter()


@router_healthcheck.get("/healthcheck")
async def healthcheck() -> dict:
    """
    Проверяет состояние работы ресурса

    Returns
    -------
    dict
        Возращает "ok" при работе сервиса
    """
    return {"message": "ok"}
