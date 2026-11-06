from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

def start():
    pass

def end():
    pass

@asynccontextmanager
async def lifespan():

    start()
    yield
    end()

app = FastAPI(lifespan=lifespan)