import aioredis
from config.main import settings


def register_redis(app):
    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await aioredis.StrictRedis(host=settings.redis_host)
        print(app.state.redis)

    @app.on_event("shutdown")
    async def shutdown_event():
        await app.state.redis.close()
