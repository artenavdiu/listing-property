from fastapi import HTTPException
from src.db.repo.listing_repo import *

async def get_all_listings():
    return await get_listings()

async def get_listing_by_id(id: int):
    listing = await fetch_listing_by_id(id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    return listing

async def update_listing(id: int, payload: ListingUpdate):
    listing = await get_listing_by_id(id)

    update_data = payload.dict(exclude_unset=True)
    listing_data = ListingUpdate(**listing)

    updated_movie = listing_data.copy(update=update_data)

    return await update_listing_by_id(id, updated_movie)
    
async def remove_listing(id: int):
    listing = await fetch_listing_by_id(id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    return await delete_listing_by_id(id)

async def add_listing(payload: AddListing):        
    return await create_listing(payload)