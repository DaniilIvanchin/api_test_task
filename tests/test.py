import requests

data = {
    "username": "testuser",
    "password": "P@ssword123!",
    "password_repeat": "P@ssword123!",
    "email": "test@example.com"
}

response = requests.post("http://localhost:8000/auth/register/", json=data)
print(response.status_code, response.text)