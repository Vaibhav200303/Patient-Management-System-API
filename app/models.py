from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
#now we will define the route to create a new patient record in the patients.json file
#for that we will use pydantic model

class Patient(BaseModel):
    id: Annotated[
        str,
        Field(
            description="The unique identifier for the patient",
            examples=["P001"]
        )
    ]

    name: Annotated[
        str,
        Field(
            description="Name of the patient",
            examples=["Shubham"]
        )
    ]

    city: Annotated[
        str,
        Field(
            description="Name of the city where patient is currently living",
            examples=["Delhi"]
        )
    ]

    age: Annotated[
        int,
        Field(
            gt=0,
            le=120,
            description="Age of the patient in years",
            examples=[30]
        )
    ]

    gender: Annotated[
        Literal["male", "female", "other"],
        Field(
            description="Gender of the patient",
            examples=["male"]
        )
    ]

    height: Annotated[
        float,
        Field(
            gt=0,
            description="Height of the patient in metres",
            examples=[1.75]
        )
    ]

    weight: Annotated[
        float,
        Field(
            gt=0,
            description="Weight of the patient in kilograms",
            examples=[70.5]
        )
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / self.height ** 2, 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal weight"
        elif self.bmi < 30:
            return "Overweight"
        return "Obese"



#now we have to create an endpoint for update operation
#for that we need another patient model because in that model we will keep fields optional as user can enter only the field required to update
class PatientUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        description="Name of the patient",
        examples=["Shubham"]
    )

    city: str | None = Field(
        default=None,
        description="Name of the city where patient is currently living",
        examples=["Delhi"]
    )

    age: int | None = Field(
        default=None,
        gt=0,
        le=120,
        description="Age of the patient in years",
        examples=[30]
    )

    gender: Literal["male", "female", "other"] | None = Field(
        default=None,
        description="Gender of the patient",
        examples=["male"]
    )

    height: float | None = Field(
        default=None,
        gt=0,
        description="Height of the patient in metres",
        examples=[1.75]
    )

    weight: float | None = Field(
        default=None,
        gt=0,
        description="Weight of the patient in kilograms",
        examples=[70.5]
    )
