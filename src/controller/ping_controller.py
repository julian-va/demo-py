from dataclasses import dataclass
from fastapi import APIRouter, Depends, responses, status


@dataclass
class PingController:
    """docstring for ClassName."""

    ping_router: APIRouter = APIRouter(tags=["Ping"])

    @ping_router.get(path="/ping", status_code=status.HTTP_200_OK)
    def ping():
        return responses.JSONResponse(
            content={"message": "funciona si!!!"}, status_code=status.HTTP_200_OK
        )
