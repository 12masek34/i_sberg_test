from pydantic import BaseModel


class Anagram(BaseModel):
    first: str
    second: str


class Device(BaseModel):
    device_id: int


class Endpoint(BaseModel):
    endpoint_id: int
    device_id: int
    text: str
