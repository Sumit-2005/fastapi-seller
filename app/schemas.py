from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated
from datetime import datetime

class ListingBase(BaseModel):
    title: str
    description: str
    category: str
    price: int
    stock: int
    shipping_info: str
