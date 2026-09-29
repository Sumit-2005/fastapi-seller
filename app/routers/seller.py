from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
from ..database import get_db
from sqlalchemy import func
from .. import models
from .. import schemas

router = APIRouter(
    prefix="/seller",
    tags=['Seller']
) 

@router.get("/")
def get_listings(db: Session = Depends(get_db)):
    listings = db.query(models.Listings).all()
    return listings

@router.post("/", status_code = status.HTTP_201_CREATED)
def add_listing(listing: schemas.ListingBase, db: Session = Depends(get_db)):
    new_listing = models.Listings(**listing.model_dump())
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_listing(id: int, db: Session = Depends(get_db)):
    listing = db.query(models.Listings).filter(models.Listings.id == id)
    if listing.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"Listing with id: {id} does NOT EXIST")

    listing.delete(synchronize_session=False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.ListingBase)
def update_listing(id: int, listing: schemas.ListingBase, db: Session = Depends(get_db)):
    listing_query = db.query(models.Listings).filter(models.Listings.id == id)

    if listing_query.first()== None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Listing with id: {id} does NOT EXIST")

    listing_query.update(listing.model_dump(), synchronize_session=False)
    db.commit()
    return listing_query.first()