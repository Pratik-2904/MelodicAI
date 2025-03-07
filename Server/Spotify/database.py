from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


POST_USERNAME = "postgres"
POST_PASS = "7373"
PORT_NO = "5432"
NAME_OF_PROJECT = "Melodic_AI"
db_URL = f"postgresql://{POST_USERNAME}:{POST_PASS}@localhost:{PORT_NO}/{NAME_OF_PROJECT}"  # this is the format of url that needs to be passed down to the engine to bind with database

# DB_URL = 'postgresql://postgres:7373@localhost:5432/Melodic_AI'
DB_URL = db_URL

engine = create_engine(DB_URL)

# engine = create_engine(db_URL)
sessionLocal = sessionmaker(
    autocommit=False,  # autocommit false sets the sesion from doing the transactional commits automatically
    autoflush=False,  # Setting autoflush to false makes sure session does not flush any pending changes to the db
    bind=engine,  # binds the session with the engine
)  # this is provideing the inetface throgh which you can interact with the daata base in transectional manner

def get_db():
    db = sessionLocal()
    try:
        yield db    # using return only will return the db bu the issue srises when closing the same at the same time its called
        # thus to solve this issue yield is used
        #The yield keyword is used to turn a function into a generator. When the yield statement is executed, it returns a value to the caller and pauses the function's execution, saving its state. When the function is called again, it resumes execution from where it left off. In this context, yield db provides the database session to the caller.
    finally:
        db.close()
