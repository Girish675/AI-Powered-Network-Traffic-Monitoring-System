from pydantic import BaseModel
from datetime import datetime

# Schema for creating a new log (client request)
class NetworkLogCreate(BaseModel):
    source_ip: str
    destination_ip: str
    protocol: str
    packet_size: float

# Schema for reading logs (API response)
class NetworkLog(NetworkLogCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
