from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import BOOLEAN, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import DeclarativeMeta

__all__ = ["Client", "TokenBlacklist"]

db = SQLAlchemy()
# mypy workaround, see https://github.com/dropbox/sqlalchemy-stubs/issues/76#issuecomment-595839159
BaseModel: DeclarativeMeta = db.Model


class Client(BaseModel):
    __tablename__ = "public.clients"

    id = db.Column("Id", INTEGER, primary_key=True)
    client_id = db.Column("ClientId", VARCHAR(128), unique=True, nullable=False)
    client_secret = db.Column("ClientSecret", VARCHAR(256), nullable=False)
    is_admin = db.Column("IsAdmin", BOOLEAN, nullable=False)


class TokenBlacklist(BaseModel):
    __tablename__ = "public.blacklist"

    token = db.Column("token", VARCHAR(256), primary_key=True)
