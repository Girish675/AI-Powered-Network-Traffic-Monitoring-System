from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base  # Import Base from database.py

# Define a database model for storing network logs
class NetworkLog(Base):
    __tablename__ = "network_logs"  # Table name in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)  # Unique ID
    source_ip = Column(String, nullable=False)  # Source IP address
    destination_ip = Column(String, nullable=False)  # Destination IP
    protocol = Column(String, nullable=False)  # Protocol (TCP, UDP, etc.)
    packet_size = Column(Float, nullable=False)  # Packet size
    timestamp = Column(DateTime, server_default=func.now())  # Auto timestamp

print("models.py is being executed...")  # Debug print statement
