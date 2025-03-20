from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.database import engine
from app.models.vehicle import Vehicle

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.get("/")
def get_vehicles():
    with Session(engine) as session:
        vehicles = session.exec(select(Vehicle)).all()
        return vehicles

@router.post("/")
def create_vehicle(vehicle: Vehicle):
    with Session(engine) as session:
        session.add(vehicle)
        session.commit()
        session.refresh(vehicle)
        return vehicle

@router.get("/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    with Session(engine) as session:
        vehicle = session.get(Vehicle, vehicle_id)
        if not vehicle:
            raise HTTPException(status_code=404, detail="Vehicle not found")
        return vehicle

@router.put("/{vehicle_id}")
def update_vehicle(vehicle_id: int, updated: Vehicle):
    with Session(engine) as session:
        vehicle = session.get(Vehicle, vehicle_id)
        if not vehicle:
            raise HTTPException(status_code=404, detail="Vehicle not found")
        updated.id = vehicle_id
        session.merge(updated)
        session.commit()
        return updated

@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    with Session(engine) as session:
        vehicle = session.get(Vehicle, vehicle_id)
        if not vehicle:
            raise HTTPException(status_code=404, detail="Vehicle not found")
        session.delete(vehicle)
        session.commit()
        return {"ok": True}
