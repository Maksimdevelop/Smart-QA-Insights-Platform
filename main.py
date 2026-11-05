from contextlib import asynccontextmanager
from fastapi import FastAPI

def start():
    pass

def end():
    pass

@asynccontextmanager
async def lifespan():

    start()
    yield
    end()