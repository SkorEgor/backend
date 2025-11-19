from fastapi import APIRouter

router_healthcheck = APIRouter()


@router_healthcheck.get("/healthcheck")
async def healthcheck() -> dict:
    """Проверяем состояние работы ресурса

    Returns
    -------
    dict
        Крактое сообщение, подтверждающие работу сайта
    """
    return {"message": "ok"}
