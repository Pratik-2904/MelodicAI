import uuid
import cloudinary.uploader
from fastapi import APIRouter, Depends, FastAPI, File, Form, UploadFile
from sqlalchemy.orm import Session
from database import get_db
from middleware.auth_middleware import auth_middleware
import claudinary_config  # Import the Cloudinary configuration

from models.song import Song

router = APIRouter()

@router.post("/upload", status_code=201)
def upload_Song(
    song: UploadFile = File(...),  # as the file needs to be uploaded argument should not be query but the file thus Type Upload file
    thumbnail: UploadFile = File(...),
    artist: str = Form(...),  # here the values are taken from the formm thus form
    song_name: str = Form(...),  # triple dot specify that the fields are required
    hex_code: str = Form(...),
    db: Session = Depends(get_db),
    auth_dic=Depends(auth_middleware),
):
    song_id = str(uuid.uuid4())
    song_res = cloudinary.uploader.upload(
        song.file, resource_type="auto", folder=f"songs/{song_id}"
    )

    thumb_res = cloudinary.uploader.upload(
        thumbnail.file, resource_type="image", folder=f"songs/{song_id}"
    )
    # print(song_res)
    # return song_res, thumb_res

    # save to db
    new_song = Song(
        id=song_id,
        song_url=song_res["url"],
        thumbnail_url=thumb_res["url"],
        artist_name=artist,
        song_name=song_name,
        hex_code=hex_code,
    )
    
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    
    return new_song
