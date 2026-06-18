from fastapi import HTTPException
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.db_models import PatientDB
from app.schemas import PatientCreate, PatientUpdate


def get_all_patients(db: Session):
    return db.query(PatientDB).all()


def get_patient(db: Session, patient_id: str):
    patient = (
        db.query(PatientDB)
        .filter(PatientDB.id == patient_id)
        .first()
    )

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


def create_patient(db: Session, patient: PatientCreate):
    existing = (
        db.query(PatientDB)
        .filter(PatientDB.id == patient.id)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Patient already exists"
        )

    db_patient = PatientDB(**patient.model_dump())

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient


def update_patient(
    db: Session,
    patient_id: str,
    patient_update: PatientUpdate
):
    patient = (
        db.query(PatientDB)
        .filter(PatientDB.id == patient_id)
        .first()
    )

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient does not exist"
        )

    updated_data = patient_update.model_dump(exclude_unset=True)

    for field, value in updated_data.items():
        setattr(patient, field, value)

    db.commit()
    db.refresh(patient)

    return patient


def delete_patient(db: Session, patient_id: str):
    patient = (
        db.query(PatientDB)
        .filter(PatientDB.id == patient_id)
        .first()
    )

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient does not exist"
        )

    db.delete(patient)
    db.commit()

    return {"message": "Patient deleted successfully"}


def sort_patients(
    db: Session,
    sort_by: str,
    order_by: str
):
    column = getattr(PatientDB, sort_by)

    ordering = desc(column) if order_by == "desc" else asc(column)

    return (
        db.query(PatientDB)
        .order_by(ordering)
        .all()
    )