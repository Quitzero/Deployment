from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>"


class Medicines(BaseModel):
    __tablename__ = "medicines"

    title = Column('Название лекарства', String(100))
    manufacturer = Column('Производитель', String(100))
    price = Column('Цена (руб.)', String(100))


class Pharmacy(BaseModel):
    __tablename__ = "pharmacy"

    title = Column('Название аптеки', String(100))
    address = Column('Адрес аптеки', String(100))
    number = Column('Номер телефона', String(11))


class Applications(BaseModel):
    __tablename__ = "applications"

    аpplication_date = Column('Дата составления заявки', String(20), default=datetime.now)
    pharmacies_id = Column('Номер аптеки', ForeignKey("pharmacy.id"))
    аpplication_completion_date = Column('Дата выполнения заявки', String(20))


class Purchases(BaseModel):
    __tablename__ = "purchases"

    application_id = Column('номер заявки', ForeignKey("applications.id"))
    medicines_id = Column('код лекарства', ForeignKey("medicines.id"))
    amount = Column('количество (шт.)', Integer())
