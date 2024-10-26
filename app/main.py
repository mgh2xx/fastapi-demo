#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get("/square/{e}")
def square(e: int):
    return {"square": e**2}

@app.get("/subtract/{f}/{g}")
def subtract(f: int, g: int):
    return {"difference": f-g}

@app.get("/diff_squares/{h}/{i}")
def diff_squares(h :int, i: int):
    return {"difference of squares": (h**2) - (i**2)}
