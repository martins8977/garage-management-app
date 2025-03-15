from fastapi import FastAPI
from app.routers import auth, customers, vehicles, jobs

app = FastAPI()

app.include_router(auth.router)
app.include_router(customers.router)
app.include_router(vehicles.router)
app.include_router(jobs.router)
