from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_connect = 'mysql://root:admin@127.0.0.1:3306/ficticio'

engine = create_engine(db_connect, convert_unicode=True, pool_size=10, pool_pre_ping=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


def close_db():
    db_session.flush()
    db_session.remove()
