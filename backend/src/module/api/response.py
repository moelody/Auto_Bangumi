from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from module.models.response import ResponseModel


def u_response(response_model: ResponseModel):
    return JSONResponse(
        status_code=response_model.status_code,
        content={
            "status": response_model.status,
            "msg_en": response_model.msg_en,
            "msg_zh": response_model.msg_zh,
        },
    )