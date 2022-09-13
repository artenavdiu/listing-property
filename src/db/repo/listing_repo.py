from src.db.config import database    
from src.db.models.listing import listing
from src.db.schemas.listing import AddListing, ListingUpdate

async def get_listings():
    query = listing.select()
    return await database.fetch_all(query=query)

async def update_listing_by_id(id: int, payload: ListingUpdate):
    query = (
        listing
        .update()
        .where(listing.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)

async def fetch_listing_by_id(id: int):
    query = listing.select(listing.c.id==id)
    return await database.fetch_one(query=query)

async def delete_listing_by_id(id: int):
    return await database.execute(query=listing.delete().where(listing.c.id==id))

async def create_listing(payload: AddListing):
    query = listing.insert().values(**payload.dict())
    return await database.execute(query=query)