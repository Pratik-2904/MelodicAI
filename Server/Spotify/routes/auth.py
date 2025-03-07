import uuid
import bcrypt
from fastapi import Depends, HTTPException, Header
from middleware.auth_middleware import auth_middleware
from models.user import User
from pydantic_schemas.user_create import UserCreate
from database import get_db
from fastapi import APIRouter
from sqlalchemy.orm import Session
import jwt
from pydantic_schemas.user_login import UserLogin


router = (
    APIRouter()
)  # instead of using app every time what we can do is use router for efficiency


@router.post("/signup", status_code=201)
def SignUp(
    user: UserCreate,
    db: Session = Depends(
        get_db
    ),  # this depends function defined its not an argument or anything but is a dependency
):
    # extract the data coming from the request
    # check if the usre alsreadt inside the databas that is if it alsreasy exists
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(400, "User alreasy exists with the given email!.")

    hashed_pw = bcrypt.hashpw(user.password.encode(), salt=bcrypt.gensalt())

    user_db = User(
        id=str(uuid.uuid4()),
        email=user.email,
        name=user.name,
        password=hashed_pw,
    )

    # add the user to the db
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    # check if user exists
    user_db = db.query(User).filter(User.email == user.email).first()

    if not user_db:
        # if not exist throw error
        raise HTTPException(400, "No user found on this email")

    # check if password is matching
    # hashed_pw = bcrypt.hashpw(user.password.encode(), salt=bcrypt.gensalt()) # this approch logically seam correct but is not realistically treue as the hashed pw changes everytime for each same pass
    is_matched = bcrypt.checkpw(
        user.password.encode(),
        user_db.password,  # no need to encode here as it already in byte format
    )
    # if not return error
    if not is_matched:
        raise HTTPException(400, "Incorrect Password!")
    # if yes return data

    token = jwt.encode({"id": user_db.id}, key="Password_key", algorithm="HS256")
    print(token)
    return {"token": token, "user": user_db}


@router.get("/")
def get_current_user(
    db: Session = Depends(get_db),
    user_dict=Depends(
        auth_middleware
    ),  # this is the auth token which is a header. Python automatically consider the _ here as the - in the header as python dont support the - containing variable _ is used instead and is then casted as the - character
):
    #get the user data from the postgre db
    user = db.query(User).filter(User.id == user_dict['id']).first()
    
    if not user:
        raise HTTPException(404,'User not found!')
    
    return user
