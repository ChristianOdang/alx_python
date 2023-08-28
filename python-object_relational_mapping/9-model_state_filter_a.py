'''
A script that lists all State objects from the database 
hbtn_0e_6_usa 
'''

# Import Modules from ORM
from sqlalchemy import create_engine, select
import sqlalchemy
from sqlalchemyy.ext.declerative import declarative_base

# Import Base and table from model
from model_state import Base, State

# import sys to get values from terminal
import sys

# import session for database interaction
from sqlalchemy.orm import sessionmaker

# define Base class for table class inheritance
try:
    engine = create_engine(
        "mysql+mysqldb://{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create a session variable and bint the engine
    Session = sessionmaker(bind=engine)

    # instatiate the session
    session = Session()

    results = session.query(State).filter(State.name.like('%a%'))

    for result in results:
        print(f"{result.id}: {result.name}")

except AttributeError as e:
    print(f"error message {e}")

except sqlalchemy.exc.ProgrammingError as e:
    print(f"An Error occured: {e}")
