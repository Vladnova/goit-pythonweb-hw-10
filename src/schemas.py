from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import date
from typing import Optional


class ContactBase(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str
    birthday: Optional[date] = None
    additional_data: Optional[str] = None


class ContactResponse(ContactBase):
    id: int


class ContactUpdate(ContactBase):
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True  # Дозволяє конвертувати об'єкти SQLAlchemy у Pydantic


# Схема користувача
class User(BaseModel):
    id: int
    username: str
    email: str
    avatar: str

    model_config = ConfigDict(from_attributes=True)


# Схема для запиту реєстрації
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


# Схема для токену
class Token(BaseModel):
    access_token: str
    token_type: str

class RequestEmail(BaseModel):
    email: EmailStr