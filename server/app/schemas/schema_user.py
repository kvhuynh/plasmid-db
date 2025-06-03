from pydantic import BaseModel, Field, validator, EmailStr;

class UserBase(BaseModel):
    name: str;
    email: EmailStr;
    role: str;

class UserLogin(BaseModel):
    email: EmailStr;
    password: str;

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