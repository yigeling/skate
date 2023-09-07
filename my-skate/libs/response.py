def generate_response(data=None, message="success!", code=0):
    #  约定返回的数据格式
    if data is None:
        data = []

    return {
        "code": code,
        "message": message,
        "data": data
    }
