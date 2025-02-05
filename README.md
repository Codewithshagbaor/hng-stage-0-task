# Django API Project

This is a Django-based API project that provides user information including email, current datetime, and GitHub URL.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- Django CORS headers

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Codewithshagbaor/hng-stage-0-task.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Documentation

### Endpoint URL

- **GET** `/api/`

### Request/Response Format

#### Request

- Method: `GET`
- URL: `/api/`

#### Response

- Status: `200 OK`
- Body:
    ```json
    {
        "email": "dxtlive@gmail.com",
        "current_datetime": "2023-10-05T12:34:56.789Z",
        "github_url": "https://github.com/Codewithshagbaor/hng-stage-0-task.git"
    }
    ```

### Example Usage

#### cURL

```sh
curl -X GET http://127.0.0.1:8000/api/
```

#### Python usage (request)

```sh
import requests

response = requests.get('http://127.0.0.1:8000/api/')
print(response.json())
```