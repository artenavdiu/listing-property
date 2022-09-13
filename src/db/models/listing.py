from sqlalchemy import (Column, Integer, MetaData, Identity, Table,
                        String, Sequence, DECIMAL)

metadata = MetaData()

listing = Table(
    'listings',
    metadata,
    Column('id', Integer, Sequence('listings_id_seq'), primary_key=True),
    Column('property_address', String(200)),
    Column('listing_price', DECIMAL(12, 2))
)