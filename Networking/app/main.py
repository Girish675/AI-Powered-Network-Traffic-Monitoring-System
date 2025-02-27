from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import crud, schemas, models
from app.models import NetworkLog
from typing import List

# Create tables when the app starts
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new network log
@app.post("/logs/", response_model=schemas.NetworkLog)
def create_log(log: schemas.NetworkLogCreate, db: Session = Depends(get_db)):
    return crud.create_network_log(db=db, log=log)

# Get all network logs
@app.get("/logs/", response_model=list[schemas.NetworkLog])
def get_logs(
    source_ip: str = Query(None, description="Filter by source IP"),
    destination_ip: str = Query(None, description="Filter by destination IP"),
    protocol: str = Query(None, description="Filter by protocol"),
    db: Session = Depends(get_db)
):
    query = db.query(NetworkLog)

    if source_ip:
        query = query.filter(NetworkLog.source_ip == source_ip)
    if destination_ip:
        query = query.filter(NetworkLog.destination_ip == destination_ip)
    if protocol:
        query = query.filter(NetworkLog.protocol == protocol)

    return query.all()

# Get a specific network log by ID
@app.get("/logs/{log_id}", response_model=schemas.NetworkLog)
def get_log(log_id: int, db: Session = Depends(get_db)):
    log = crud.get_network_log(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return log

# Delete a log by ID
@app.delete("/logs/{log_id}")
def delete_log(log_id: int, db: Session = Depends(get_db)):
    log = crud.delete_network_log(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return {"message": "Log deleted"}
