from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

# Database setup
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example usage
def main():
    # Create some bands and venues
    band1 = Band(name="The Beatles", hometown="Liverpool")
    venue1 = Venue(title="Royal Albert Hall", city="London")
    
    session.add(band1)
    session.add(venue1)
    session.commit()

    # Create a concert
    concert = Concert(band_id=band1.id, venue_id=venue1.id, date="2024-10-01")
    session.add(concert)
    session.commit()

    # Fetch and print introduction
    fetched_concert = session.query(Concert).first()
    print(fetched_concert.introduction())

if __name__ == '__main__':
    main()
