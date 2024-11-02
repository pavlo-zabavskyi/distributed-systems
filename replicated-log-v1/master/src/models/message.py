from pydantic import BaseModel, conint, constr


class MessageRequest(BaseModel):
    message: constr(min_length=3, max_length=20)
    write_concern: conint(ge=1, le=4)  # TODO: le = number of secondaries + master
