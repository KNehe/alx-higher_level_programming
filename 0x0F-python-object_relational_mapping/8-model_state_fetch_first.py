#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
via SQLAlchemy
"""
if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).order_by(State.id).first()
    if not row:
        print("Nothing")
    else:
        print("{}: {}".format(row.id, row.name))
