from databases import Database
import sqlalchemy

DATABASE_URL = "sqlite:///mentors.db"

database = Database(DATABASE_URL)

sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


def get_database() -> Database:
    return database
