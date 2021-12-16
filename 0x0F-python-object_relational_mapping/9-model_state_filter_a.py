#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
that contain letter a
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

    q = session.query(State).filter(
            State.name.contains('a')).order_by(State.id)
    for state in q:
        print("{}: {}".format(state.id, state.name))
