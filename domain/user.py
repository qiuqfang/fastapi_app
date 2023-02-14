from pydantic import BaseModel, EmailStr, validator


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: bool

    @validator("name")
    def validator_name(cls, value, values, config, field):
        print(cls, value, values, config, field)
        if len(value) < 2 or len(value) > 10:
            raise ValueError("姓名长度应不小于2且不大于10")
        return value

    @validator("password")
    def validator_password(cls, value, values, config, field):
        print(cls, value, values, config, field)
        if len(value) < 6 or len(value) > 20:
            raise ValueError("密码长度应不小于6且不大于10")
        return value
