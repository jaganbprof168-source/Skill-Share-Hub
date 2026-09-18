import Execution
import Table
from DataBase import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

Table.Base.metadata.create_all(bind=engine)
app.include_router(Execution.router)
