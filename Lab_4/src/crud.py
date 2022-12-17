from sqlalchemy.orm import Session

from src import models, schemas


# region Medicines
def create_medicines(db: Session, medicines: schemas.MedicinesCreate):
    """
    Добавление нового пользователя
    """
    db_medicines = models.Medicines(title=medicines.title, manufacturer=medicines.manufacturer, price=medicines.price)
    db.add(db_medicines)
    db.commit()
    db.refresh(db_medicines)
    return db_medicines


def get_medicine(db: Session, medicines_id: int):
    """
    Получить пользователя по его id
    """
    return db.query(models.Medicines).filter(models.Medicines.id == medicines_id).first()


def get_medicines_by_title(db: Session, title: str):
    """
    Получить лекарство по его title
    """
    return db.query(models.Medicines).filter(models.Medicines.title == title).first()


def get_medicines(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Medicines).offset(skip).limit(limit).all()


# endregion

# region Pharmacy
def create_pharmacy(db: Session, pharmacy: schemas.PharmacyCreate):
    """
    Добавление нового пользователя
    """
    db_pharmacy = models.Pharmacy(title=pharmacy.title, address=pharmacy.address, number=pharmacy.number)
    db.add(db_pharmacy)
    db.commit()
    db.refresh(db_pharmacy)
    return db_pharmacy


def get_pharmacy(db: Session, pharmacy_id: int):
    """
    Получить пользователя по его id
    """
    return db.query(models.Pharmacy).filter(models.Pharmacy.id == pharmacy_id).first()


def get_pharmacy_by_title(db: Session, address: str):
    """
    Получить лекарство по его title
    """
    return db.query(models.Pharmacy).filter(models.Pharmacy.address == address).first()


def get_pharmacys(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Pharmacy).offset(skip).limit(limit).all()


# endregion

# region Applications
def create_pharmacies_applications(db: Session, applications: schemas.ApplicationsCreate, pharmacies_id: int):
    """
    Добавление нового Item пользователю
    """
    db_applications = models.Applications(**applications.dict(), pharmacies_id=pharmacies_id)
    db.add(db_applications)
    db.commit()
    db.refresh(db_applications)
    return db_applications


def get_applications(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список предметов из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Applications).offset(skip).limit(limit).all()


# endregion

# region Purchases
def create_applications_medicines_purchases(db: Session, purchases: schemas.PurchasesCreate, application_id: int,
                                  medicines_id: int):
    """
    Добавление нового Item пользователю
    """
    db_purchases = models.Purchases(**purchases.dict(), application_id=application_id, medicines_id=medicines_id)
    db.add(db_purchases)
    db.commit()
    db.refresh(db_purchases)
    return db_purchases


def get_purchases(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список предметов из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Purchases).offset(skip).limit(limit).all()
# endregion
