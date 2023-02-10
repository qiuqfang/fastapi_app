def ok(code=200, data=None, message="请求成功"):
    return {"code": code, "data": data, "message": message}


def failure(code=500, data=None, message="请求失败"):
    return {"code": code, "data": data, "message": message}
