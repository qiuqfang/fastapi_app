import aioredis


def register_redis(app):
    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await aioredis.StrictRedis(host="redis")
        print(f"redis成功---》》{app.state.redis}")

    @app.on_event("shutdown")
    async def shutdown_event():
        app.state.redis.close()
        await app.state.redis.wait_closed()
