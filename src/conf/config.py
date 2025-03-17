from pydantic import  EmailStr
class Config:
    DB_URL = "postgresql+asyncpg://postgres:0967181951@localhost:5432/db_contacts"
    JWT_SECRET = "my_secret_key"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_SECONDS = 3600

    MAIL_USERNAME: EmailStr = "vlad-nova@meta.ua"
    MAIL_PASSWORD: str = "1045Nova"
    MAIL_FROM: EmailStr = "vlad-nova@meta.ua"
    MAIL_PORT: int = 465
    MAIL_SERVER: str = "smtp.meta.ua"
    MAIL_FROM_NAME: str = "Rest API Service"
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = True
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = False

    CLD_NAME: str = "dheeo8gaf"
    CLD_API_KEY: int = 489746143197361
    CLD_API_SECRET: str = "vC6iuV9cjPppbj1FdB8NxjrL__w"

config = Config