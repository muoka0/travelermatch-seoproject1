from sqlalchemy.orm import Session
from db.schema import Interest, Destination, DestinationInterest, CachedSearch

def insert_interest(session: Session, interest_name: str):
    """Insert a new interest into the interests table during database initialization"""
    
    interest = Interest(interest=interest_name)
    session.add(interest)
    session.commit()    

    return interest

def insert_destination(session: Session, destination_data: dict):
    """Insert a new destination into the destinations table during database initialization"""
    
    destination = Destination(**destination_data)
    session.add(destination)
    session.commit()

    return destination

def link_destination_interest(session: Session, destination_id: int, interest_id: int):
    """Create a many-to-many relationship between a destination and an interest"""
    
    link = DestinationInterest(
        destination_id = destination_id,
        interest_id = interest_id
    )
    session.add(link)
    session.commit()

def insert_cached_search(session: Session, cache_data: dict):
    """ Insert a completed Gemini recommendation result into the cache"""
    
    cached = CachedSearch(**cache_data)
    session.add(cached)
    session.commit()

    return cached