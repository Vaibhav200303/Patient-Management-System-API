#i have to create an api for patient management system
#it will have four main operations:
#create a patient record
#retrieve a patient record/or retrieve all patient records
#update a patient record
#delete a patient record

#lets start

#this is where we will import all the neccessary libraries and modules

from fastapi import FastAPI
from app.routers import patients

#now we will define our api routes for the four main operations
app = FastAPI(
    title="Patient Management System API",
    description="A fully functional API to manage patient records",
    version="1.0.0"
)

app.include_router(patients.router)


#toy api
@app.get("/")
def read_root():
    return {"message": "Patient Management System API"}


@app.get("/about")
def read_about():
    return {
        "message": "A fully functional API to manage patient records"
    }


