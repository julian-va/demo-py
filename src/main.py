from typing import Union

from fastapi import FastAPI

from src.config.run_server import RunServer

app = FastAPI()

RunServer(app=app)
