from fastapi import APIRouter

from src.service.listing_service import add_listing as add_new_listing, get_all_listings, get_listing_by_id, remove_listing
from src.db.schemas.listing import AddListing, ListingUpdate

listing = APIRouter()

@listing.get('/')
async def get_listings():
    return await get_all_listings()

@listing.get('/{id}')
async def get_listing(id: int):
    return await get_listing_by_id(id)

@listing.put('/{id}')
async def update_listing(id: int, payload: ListingUpdate):
    await update_listing(id, payload)
    return await get_listing_by_id(id)

@listing.delete('/{id}')
async def delete_listing(id: int):
    return await remove_listing(id)

@listing.post('/', status_code=201)
async def add_listing(payload: AddListing):
    return await add_new_listing(payload)