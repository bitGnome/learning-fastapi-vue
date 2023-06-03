from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from tortoise import Tortoise

# from database.register import register_tortoise
# from database.config import TORTOISE_ORM

# enable schemas to read relationships between models
# Tortoise.init_models(["database.models"], "models")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello, world, you here?"