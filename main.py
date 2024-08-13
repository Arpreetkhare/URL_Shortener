from fastapi import FastAPI
from fastapi import FastAPI, Depends
from fastapi import HTTPException

from sqlalchemy import text
from sqlalchemy.orm import Session,sessionmaker
from database import get_db,Session,create_tables
from routers.short import short_router




app=FastAPI()

create_tables()


      

@app.on_event("startup")
def startup_event():
    try:
        with sessionmaker() as session:
            session.execute(text("SELECT 1"))
            print("Database connected")
    except Exception as e:
        print(f"Database connection failed: {e}")

@app.on_event("shutdown")
def shutdown_event():
    print("Application shutdown")

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    try:
        query = text("SELECT 1")
        db.execute(query)
        return {"message": "Connection to database successful!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error", headers={"Error": str(e)})


# @app.get("/")
# async def read_root(db:Session = Depends(get_db)):
#     try:
#         await db.execute(text("SELECT 1"))
#         return {"message": "Connection to database successful!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Database error", headers={"Error": str(e)})

app.include_router(short_router, tags=["short_router"])




