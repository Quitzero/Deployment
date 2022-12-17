from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

# region db
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


# endregion

def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению


# region medicines_test
def test_create_medicines():
    """
    Тест на создание нового лекарства
    """
    response = client.post(
        "/medicines/",
        json={"title": "testTitle", "manufacturer": "testManufacturer", "price": "testPrice"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "testTitle"


def test_create_exist_medicines():
    """
    Проверка случая, когда мы пытаемся добавить существующее лекарство
    в БД, т.е. когда данный title уже присутствует в БД.
    """
    response = client.post(
        "/medicines/",
        json={"title": "testTitle", "manufacturer": "testManufacturer", "price": "testPrice"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    print(data)
    assert data["detail"] == "Title already registered"


def test_get_medicines():
    """
    Тест на получение списка лекарств из БД
    """
    response = client.get("/medicines/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["title"] == "testTitle"


def test_get_medicines_by_id():
    """
    Тест на получение лекарства из БД по его id
    """
    response = client.get("/medicines/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "testTitle"


def test_medicines_not_found():
    """
    Проверка случая, если лекарство с таким id отсутствует в БД
    """
    response = client.get("/medicines/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"


# endregion

# region Pharmacy_test
def test_create_Pharmacy():
    """
    Тест на создание новой аптеки
    """
    response = client.post(
        "/pharmacy/",
        json={"title": "testTitle", "address": "testAddres", "number": "85005553535"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "testTitle"


def test_create_exist_pharmacy():
    """
    Проверка случая, когда мы пытаемся добавить существующею аптеку
    в БД, т.е. когда данный ddress уже присутствует в БД.
    """
    response = client.post(
        "/pharmacy/",
        json={"title": "testTitle", "address": "testAddres", "number": "85005553535"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    print(data)
    assert data["detail"] == "Address already registered"


def test_get_pharmacy():
    """
    Тест на получение списка аптек из БД
    """
    response = client.get("/pharmacy/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["title"] == "testTitle"


def test_get_pharmacy_by_id():
    """
    Тест на получение лекарства из БД по его id
    """
    response = client.get("/pharmacy/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "testTitle"


def test_pharmacy_not_found():
    """
    Проверка случая, если лекарство с таким id отсутствует в БД
    """
    response = client.get("/pharmacy/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "pharmacy not found"


# endregion

# region Applications_test
def test_add_applications_to_pharmacies():
    """
    Тест на добавление Applications аптеке
    """
    response = client.post(
        "/pharmacies/1/applications/",
        json={"аpplication_date": "29.05.01", "аpplication_completion_date": "29.05.02"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["аpplication_date"] == "29.05.01"
    assert data["аpplication_completion_date"] == "29.05.02"
    assert data["pharmacies_id"] == 1


def test_get_applications():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/applications/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["аpplication_date"] == "29.05.01"
    assert data[0]["аpplication_completion_date"] == "29.05.02"
    assert data[0]["pharmacies_id"] == 1
# endregion

# region Purchases_test
def test_add_purchases_to_pharmacies():
    """
    Тест на добавление purchases аптеке
    """
    response = client.post(
        "/1/1/purchases/",
        json={"amount": "250"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["application_id"] == 1
    assert data["medicines_id"] == 1
    assert data["amount"] == 250


def test_get_purchases():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/purchases/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["application_id"] == 1
    assert data[0]["medicines_id"] == 1
    assert data[0]["amount"] == 250
# endregion