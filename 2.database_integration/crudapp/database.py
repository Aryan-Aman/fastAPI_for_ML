from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL (for local development)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# For PostgreSQL (uncomment if needed):
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

# For MySQL (uncomment if needed):
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()