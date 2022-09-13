from pydantic import BaseModel


class Listing(BaseModel):
    property_address: str
    listing_price: float

class ListingUpdate(Listing): 
    property_address: str
    listing_price: float

class AddListing(Listing):
    property_address: str
    listing_price: float
