from pydantic import BaseModel, Field, validator

class UserBase(BaseModel):
    # user_name: str;
    # email: str TODO
    name: str;
    role: str;

class UserLogin(BaseModel):
    name: str

class UserCreate(UserBase):
    password: str = Field(..., min_length=12, max_length=128);

    @validator("password")
    def password_strength(cls, value):
        has_digit = False;
        has_upper = False;

        for char in value:
            if char.isdigit():
                has_digit = True;
            if char.isupper():
                has_upper = True;
        if not has_digit:
            raise ValueError("Password must include at least one number");
        if not has_upper:
            raise ValueError("Password must have at least one uppercase character");
        return value;

class User(UserBase):
    id: int;    
    
    class Config:
        orm_mode = True