import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/employees")
def get_employees():
    with open("data/employees.json") as file:
        return json.load(file)


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {"employee_id": employee_id}
