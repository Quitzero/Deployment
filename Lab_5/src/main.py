from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db(): # pragma: no cover:
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# region Medicines
@app.get("/medicines/", response_model=list[schemas.Medicines])
def read_medicines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка пользователей
    """
    medicines = crud.get_medicines(db, skip=skip, limit=limit)
    return medicines


@app.post("/medicines/", response_model=schemas.Medicines)
def create_medicine(medicines: schemas.MedicinesCreate, db: Session = Depends(get_db)):
    """
    Создание лекарства, если такой title уже есть в БД, то выдается ошибка
    """
    db_medicines = crud.get_medicines_by_title(db, title=medicines.title)
    if db_medicines:
        raise HTTPException(status_code=400, detail="Title already registered")
    return crud.create_medicines(db=db, medicines=medicines)


@app.get("/medicines/{medicines_id}", response_model=schemas.Medicines)
def read_medicines(medicines_id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя по id, если такого id нет, то выдается ошибка
    """
    db_medicine = crud.get_medicine(db, medicines_id=medicines_id)
    if db_medicine is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_medicine


# endregion

# region Pharmacy
@app.get("/pharmacy/", response_model=list[schemas.Pharmacy])
def read_pharmacy(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка пользователей
    """
    pharmacys = crud.get_pharmacys(db, skip=skip, limit=limit)
    return pharmacys


@app.post("/pharmacy/", response_model=schemas.Pharmacy)
def create_medicine(pharmacy: schemas.PharmacyCreate, db: Session = Depends(get_db)):
    """
    Создание лекарства, если такой title уже есть в БД, то выдается ошибка
    """
    db_pharmacy = crud.get_pharmacy_by_title(db, address=pharmacy.address)
    if db_pharmacy:
        raise HTTPException(status_code=400, detail="Address already registered")
    return crud.create_pharmacy(db=db, pharmacy=pharmacy)


@app.get("/pharmacy/{pharmacy_id}", response_model=schemas.Pharmacy)
def read_medicines(pharmacy_id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя по id, если такого id нет, то выдается ошибка
    """
    db_pharmacy = crud.get_pharmacy(db, pharmacy_id=pharmacy_id)
    if db_pharmacy is None:
        raise HTTPException(status_code=404, detail="pharmacy not found")
    return db_pharmacy


# endregion

# region Applications
@app.get("/applications/", response_model=list[schemas.Applications])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка предметов
    """
    applications = crud.get_applications(db, skip=skip, limit=limit)
    return applications


@app.post("/pharmacies/{pharmacies_id}/applications/", response_model=schemas.Applications)
def create_applications_for_pharmacies(
        pharmacies_id: int, applications: schemas.ApplicationsCreate, db: Session = Depends(get_db)
):
    """
    Добавление пользователю нового предмета
    """
    return crud.create_pharmacies_applications(db=db, applications=applications, pharmacies_id=pharmacies_id)


# endregion

# region Purchases
@app.get("/purchases/", response_model=list[schemas.Purchases])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка предметов
    """
    purchases = crud.get_purchases(db, skip=skip, limit=limit)
    return purchases

@app.post("/{medicines_id}/{application_id}/purchases/", response_model=schemas.Purchases)
def create_purchases_for_application_medicines(
        application_id: int, medicines_id: int, purchases: schemas.PurchasesCreate, db: Session = Depends(get_db)
):
    """
    Добавление пользователю нового предмета
    """
    return crud.create_applications_medicines_purchases(db=db, purchases=purchases, medicines_id=medicines_id, application_id=application_id)
# endregion
