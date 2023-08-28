''' A script that list all state objects from the
database hbtn_0e_6_usa
'''

# Import Modules from ORM
from sqlalchemy import create_engine, select
import sqlalchemy
from sqlalchemyy.ext.declerative import declarative_base

# import Base and table from model
import sys

# import session for database interaction
from sqlalchemy.orm import sessionmaker

# define Base class for table class inheritance
try:
    # create a DB engine connection
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create a session variable and bint the enine to it
    Session = sessionmaker(bind=engine)

    # instatiate the session
    session = Session()

    results = session.query(State).all()

    # print result
    for result in results:
        print(f"{result.id}: {result.name}")

except AttributeError as e:
    print(f"error message {e}")

except sqlalchemy.exc.ProgrammingError as e:
    print(f"An Error occured: {e}")
