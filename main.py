from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# Configure the Gemini API
genai.configure(api_key="AIzaSyCb7e8VNQCL9XlteIqABbQX_oSfeWAfgMI")
model = genai.GenerativeModel('gemini-2.0-flash')

class InputNumber(BaseModel):
    number: str

@app.get("/")
def root():
    return {"message": "Running"}

@app.post("/isodd")
def is_odd(data: InputNumber):
    response = model.generate_content(f"Is {data.number} odd? In one word")
    return {"result": response.text}

@app.post("/iseven")
def is_even(data: InputNumber):
    response = model.generate_content(f"Is {data.number} even? In one word")
    return {"result": response.text}