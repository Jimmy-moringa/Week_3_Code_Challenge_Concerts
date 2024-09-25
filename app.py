# main.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert

# Create the database engine
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create instances
def main():
    band = Band(name="The Rockers", hometown="New York")
    venue = Venue(title="Big Arena", city="New York")
    concert = Concert(band=band, venue=venue, date="2024-10-01")

    # Add to session and commit
    session.add(band)
    session.add(venue)
    session.add(concert)
    session.commit()

    # Querying
    first_band = session.query(Band).first()
    print(first_band.concerts)  # Should list concerts for this band
    print(first_band.concerts[0].introduction())  # Print introduction

if __name__ == "__main__":
    main()
