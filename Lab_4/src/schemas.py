from pydantic import BaseModel


# region Medicines
class MedicinesBase(BaseModel):
    """
    Базовый класс для User
    """
    title: str
    manufacturer: str
    price: str


class MedicinesCreate(MedicinesBase):
    """
    Класс для создания Medicines, наследуется от базового MedicinesBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Medicines(MedicinesBase):
    """
    Класс для отображения информации о Medicines. Все значения полей будут браться
    из базы данных
    """
    id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True


# endregion

# region Pharmacy
class PharmacyBase(BaseModel):
    """
    Базовый класс для User
    """
    title: str
    address: str
    number: str


class PharmacyCreate(PharmacyBase):
    """
    Класс для создания Medicines, наследуется от базового MedicinesBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Pharmacy(PharmacyBase):
    """
    Класс для отображения информации о Medicines. Все значения полей будут браться
    из базы данных
    """
    id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True


# endregion

# region Applications
class ApplicationsBase(BaseModel):
    """
    Базовый класс для Item
    """
    аpplication_date: str
    аpplication_completion_date: str


class ApplicationsCreate(ApplicationsBase):
    """
    Класс для создания Item, наследуется от базового ItemBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Applications(ApplicationsBase):
    """
    Класс для отображения Item, наследуется от базового ItemBase
    поля значения для полей id и owner_id будем получать из БД
    """
    id: int
    pharmacies_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True
# endregion

# region Purchases
class PurchasesBase(BaseModel):
    """
    Базовый класс для Item
    """
    amount: int


class PurchasesCreate(PurchasesBase):
    """
    Класс для создания Item, наследуется от базового ItemBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Purchases(PurchasesBase):
    """
    Класс для отображения Item, наследуется от базового ItemBase
    поля значения для полей id и owner_id будем получать из БД
    """
    id: int
    application_id: int
    medicines_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True
# endregion
