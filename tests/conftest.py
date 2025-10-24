import pytest
from faker import Faker
from utils.api_utils import ApiUtils
from services.auth.auth_service import AuthService
from services.auth.models.register_request import RegisterRequest
from services.auth.models.login_request import LoginRequest
from services.university.university_service import UniversityService


faker = Faker()


@pytest.fixture(scope="session")
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="session")
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="session")
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)

    username = faker.user_name()
    password = faker.password(
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()
        )
    )

    login_response = auth_service.login_user(
        LoginRequest(username=username, password=password)
    )

    return login_response.access_token

@pytest.fixture(scope="session")
def auth_service(auth_api_utils_anonym):
    return AuthService(auth_api_utils_anonym)

@pytest.fixture(scope="session", autouse=True)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils

@pytest.fixture(scope="session", autouse=True)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils

@pytest.fixture(scope="session")
def university_service(university_api_utils_anonym):
    return UniversityService(university_api_utils_anonym)