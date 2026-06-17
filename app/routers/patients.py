from fastapi import APIRouter,Path,Query,HTTPException,status
from fastapi.responses import JSONResponse
from app.models import Patient,PatientUpdate
from typing import Literal
from app.database import load_data,save_data

router=APIRouter()

#now we will define the route to view all patient records and also to view a specific patient record by id
@router.get("/patients")
def view_patients():
    return load_data()


#now we will be using path parameter which identifies specific patient using patient id
@router.get("/patients/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="Id of the patient",
        examples=["P001"]
    )
):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "id": patient_id,
        **data[patient_id]
    }


#now we will define the route to create a new patient record in the patients.json file
#for that we will use pydantic model


@router.post("/patients", status_code=status.HTTP_201_CREATED)
def create(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=409,
            detail="Patient already exists"
        )

    data[patient.id] = patient.model_dump(exclude={"id"})
    save_data(data)

    return {
        "message": "Patient created successfully",
        "patient": {
            "id": patient.id,
            **data[patient.id]
        }
    }






@router.put("/patients/{patient_id}")
def update_patient(
    patient_update: PatientUpdate,
    patient_id: str = Path(
        ...,
        description="Id of the patient",
        examples=["P001"]
    )
):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient does not exist"
        )

    existing_patient_data = data[patient_id]

    updated_patient_data = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_data.items():
        existing_patient_data[key] = value

    existing_patient_data["id"] = patient_id

    pydantic_patient_update = Patient(**existing_patient_data)

    data[patient_id] = pydantic_patient_update.model_dump(exclude={"id"})

    save_data(data)

    return {
        "message": "Patient updated successfully",
        "patient": {
            "id": patient_id,
            **data[patient_id]
        }
    }


#now we will create an api endpoint for delete operation
@router.delete("/patients/{patient_id}")
def delete_patient(
    patient_id: str = Path(
        ...,
        description="Id of the patient",
        examples=["P001"]
    )
):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient does not exist"
        )

    del data[patient_id]

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={"message": "Patient deleted successfully"}
    )


#also an endpoint which provides sorted data according to user enter field and order
@router.get("/sort")
def sort_patients(
    sort_by: Literal["age", "height", "weight", "bmi"] = Query(
        ...,
        description="The field to sort by (age, height, weight, bmi)",
        examples=["bmi"]
    ),
    order_by: Literal["asc", "desc"] = Query(
        "asc",
        description="Sort order (asc or desc)",
        examples=["asc"]
    )
):
    data = load_data()

    sorted_patients = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=(order_by == "desc")
    )

    return sorted_patients
