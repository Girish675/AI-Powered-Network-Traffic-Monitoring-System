from sqlalchemy.orm import Session
from . import models, schemas

# CREATE: Add a new network log
def create_network_log(db: Session, log: schemas.NetworkLogCreate):
    db_log = models.NetworkLog(
        source_ip=log.source_ip,
        destination_ip=log.destination_ip,
        protocol=log.protocol,
        packet_size=log.packet_size
    )
    db.add(db_log)  # Add to database session
    db.commit()  # Save changes
    db.refresh(db_log)  # Refresh instance
    return db_log  # Return the created log

# READ: Retrieve all network logs
def get_network_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.NetworkLog).offset(skip).limit(limit).all()

# READ: Get a single network log by ID
def get_network_log(db: Session, log_id: int):
    return db.query(models.NetworkLog).filter(models.NetworkLog.id == log_id).first()

# DELETE: Remove a network log by ID
def delete_network_log(db: Session, log_id: int):
    db_log = db.query(models.NetworkLog).filter(models.NetworkLog.id == log_id).first()
    if db_log:
        db.delete(db_log)
        db.commit()
    return db_log
