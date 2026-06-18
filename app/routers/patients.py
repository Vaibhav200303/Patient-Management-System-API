from typing import Literal

from fastapi import APIRouter, Depends, Path, Query, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import (
    PatientCreate,
    PatientResponse,
    PatientUpdate,
)
from app.services import patient_service

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# Retrieve all patient records
@router.get(
    "",
    response_model=list[PatientResponse]
)
def get_all_patients(
    db: Session = Depends(get_db)
):
    return patient_service.get_all_patients(db)


# Retrieve patient records sorted by a selected field
# NOTE: This route must be declared before "/{patient_id}"
@router.get(
    "/sort",
    response_model=list[PatientResponse]
)
def sort_patients(
    sort_by: Literal["age", "height", "weight", "bmi"] = Query(
        ...,
        description="Field to sort by",
        examples=["bmi"]
    ),
    order_by: Literal["asc", "desc"] = Query(
        "asc",
        description="Sort order",
        examples=["desc"]
    ),
    db: Session = Depends(get_db)
):
    return patient_service.sort_patients(
        db,
        sort_by,
        order_by
    )


# Retrieve a specific patient by ID
@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def get_patient(
    patient_id: str = Path(
        ...,
        description="ID of the patient",
        examples=["P001"]
    ),
    db: Session = Depends(get_db)
):
    return patient_service.get_patient(
        db,
        patient_id
    )


# Create a new patient record
@router.post(
    "",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return patient_service.create_patient(
        db,
        patient
    )


# Update an existing patient record
@router.put(
    "/{patient_id}",
    response_model=PatientResponse
)
def update_patient(
    patient_update:PatientUpdate,
    patient_id: str = Path(
        ...,
        description="ID of the patient",
        examples=["P001"]
    ),
    db: Session = Depends(get_db)
):
    return patient_service.update_patient(
        db,
        patient_id,
        patient_update
    )


# Delete a patient record
@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_200_OK
)
def delete_patient(
    patient_id: str = Path(
        ...,
        description="ID of the patient",
        examples=["P001"]
    ),
    db: Session = Depends(get_db)
):
    return patient_service.delete_patient(
        db,
        patient_id
    )