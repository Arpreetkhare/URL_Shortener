import random
import string
from fastapi import HTTPException, status
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from models.urls import Urls
from schemas.schema import URLCreate
from database import sessionmaker,get_db


short_router=APIRouter()
def generate_short_code(length=6):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


@short_router.post("/url", status_code=status.HTTP_201_CREATED)

async def short_url(request:URLCreate=Depends(),db:Session=Depends(get_db)):
    try:
        codes = Urls(

            short_code=generate_short_code(),
            long_url=request.long_url

        )
     
            
        db.add(codes)
        db.commit()
        return codes
    except Exception as e:
        print(e) 


@short_router.get("/{short_code}") 

async def ReShort_url(short_code:str,db:Session=Depends(get_db)):
    url = db.query(Urls).filter(Urls.short_code == short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return {"short_code": short_code, "long_url": url.long_url}



