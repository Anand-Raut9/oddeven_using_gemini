from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

app = FastAPI()

client = genai.Client(api_key="AIzaSyCb7e8VNQCL9XlteIqABbQX_oSfeWAfgMI")


class InputNumber(BaseModel):
    number: str

@app.get("/")
def dumb():
    return {"message": "Running"}

@app.post("/isodd")
def is_odd(data: InputNumber):

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents= f"Is {data.number} odd? In one word",
    )
    return {"result": response.text}

@app.post("/iseven")
def is_even(data: InputNumber):
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents= f"Is {data.number} even? In one word",
    )
    return {"result": response.text}