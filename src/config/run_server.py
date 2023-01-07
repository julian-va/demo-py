from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.controller.ping_controller import PingController


class RunServer:
    def __init__(self, app: FastAPI):
        load_dotenv()
        self._BASE_URL: str = "/api/v1"
        self.middleware_cors(app=app)
        self.routers(app=app)

    def middleware_cors(self, app: FastAPI) -> None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def routers(self, app: FastAPI) -> None:
        app.include_router(prefix=self._BASE_URL, router=PingController.ping_router)
