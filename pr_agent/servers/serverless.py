import logging

from fastapi import FastAPI
from mangum import Mangum

from starlette.middleware import Middleware
from starlette_context.middleware import RawContextMiddleware

from pr_agent.servers.github_app import router

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

middleware = [Middleware(RawContextMiddleware)]
app = FastAPI(middleware=middleware)

# app = FastAPI()
app.include_router(router)

handler = Mangum(app, lifespan="off")


def serverless(event, context):
    return handler(event, context)
