from pydantic import BaseModel, EmailStr, validator


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: bool

    @validator("name")
    def validator_name(cls, value, values, config, field):
        print(cls, value, values, config, field)
        if '2' == value:
            raise ValueError("参数有误")
        return value
