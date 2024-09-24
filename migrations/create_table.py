from sqlalchemy import create_engine
from models import Base

# Database setup
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)
