from pydantic import BaseModel, Field

class UserOutput(BaseModel):
    id: int = Field(...)
    login: str = Field(...)
    email: str = Field(None)
    twitter_username: str = Field(None)
