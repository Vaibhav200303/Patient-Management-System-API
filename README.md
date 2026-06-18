# Patient Management API

A RESTful API built with FastAPI, PostgreSQL, SQLAlchemy, and Alembic for managing patient records and calculating health metrics such as BMI.

## Features

* Create, retrieve, update, and delete patient records
* Automatic BMI calculation and health verdict generation
* PostgreSQL database integration
* Database schema versioning with Alembic
* Request and response validation using Pydantic
* Layered project structure with routers and services
* Interactive API documentation with Swagger UI and ReDoc

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* Uvicorn

## Project Structure

```text
patient-management-api/
├── alembic/
│   └── versions/
├── app/
│   ├── routers/
│   │   └── patients.py
│   ├── services/
│   │   └── patient_service.py
│   ├── db.py
│   ├── db_models.py
│   ├── schemas.py
│   └── main.py
├── .env.example
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

## Patient Data Model

Each patient record contains:

* `id`
* `name`
* `city`
* `age`
* `gender`
* `height`
* `weight`
* `bmi`
* `verdict`

## Installation

### Clone the repository

```bash
git clone https://github.com/Vaibhav200303/Patient-Management-System-API.git 
cd Patient-Management-System-API
```

### Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/patient_db
```

Create a `.env.example` file containing:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/patient_db
```

## Database Setup

Create the database in PostgreSQL:

```sql
CREATE DATABASE patient_db;
```

Apply migrations:

```bash
alembic upgrade head
```

Whenever you modify a database model:

```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Example Endpoints

| Method | Endpoint                 | Description              |
| ------ | ------------------------ | ------------------------ |
| GET    | `/patients`              | Retrieve all patients    |
| GET    | `/patients/{patient_id}` | Retrieve a patient by ID |
| POST   | `/patients`              | Create a patient         |
| PUT    | `/patients/{patient_id}` | Update patient details   |
| DELETE | `/patients/{patient_id}` | Delete a patient         |

## API Screenshots

```markdown
![Swagger UI](docs/images/swagger-home.png)

![Create Patient](docs/images/create-patient.png)

![Get Patients](docs/images/get-patients.png)
```

## Future Improvements

* Authentication and authorization
* Unit and integration tests
* Docker support
* CI/CD pipeline
* API versioning

## License

This project is licensed under the MIT License.
