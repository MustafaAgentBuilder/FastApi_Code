# FastAPI Simple User and Item API

## Overview
This FastAPI application provides a simple, static set of user and item endpoints, demonstrating how to build high-performance APIs with minimal boilerplate. FastAPI is a modern, fast (high-performance) web framework for building APIs with Python based on standard type hints. It automatically generates interactive API documentation using OpenAPI (formerly Swagger) and JSON Schema.

## Features
* **Ultra fast**: Built on Starlette and Pydantic for maximum performance.
* **Automatic docs**: Interactive Swagger UI at `/docs` and Redoc at `/redoc` without extra code.
* **Type-safe**: Uses Python type hints and Pydantic models for request validation.
* **Minimal setup**: Ready for production with just a few lines of code.
* **Clear structure**: Follows common README conventions to make onboarding easy.

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-name>/<your-repo>.git
cd <your-repo>
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install "fastapi[standard]"
```

4. **Run the application**
```bash
uvicorn main:app --reload
```
* Server will start at `http://127.0.0.1:8000/`.

## Usage

* **Root endpoint**
   * `GET /`
   * Returns basic API status.
* **Static user endpoints**
   * `GET /user/1` → Returns user with ID 1.
   * `GET /user/2` → Returns user with ID 2.
* **Static item endpoints**
   * `GET /items` → Returns full list of items.
   * `GET /item/{id}` → Returns item by ID, with parameter validation using `Path`.

Example request with `curl`:
```bash
curl http://127.0.0.1:8000/item/3
```

## API Documentation

FastAPI automatically provides two interactive docs:
* **Swagger UI**: http://127.0.0.1:8000/docs
* **ReDoc**: http://127.0.0.1:8000/redoc

Use these to explore endpoints, view request/response schemas, and try out calls in-browser.

## Project Structure

```
.
├── main.py           # FastAPI app and routes
├── requirements.txt  # Dependencies
└── README.md
```

* **main.py** Contains all route definitions, static data, and path parameter validations.
* **requirements.txt** Pinned dependencies for reproducible environments.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please follow PEP 8 and include docstrings for new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## References & Further Reading

1. **Official FastAPI README** – FastAPI on GitHub
2. **FastAPI Tutorial** – User Guide on the FastAPI site
3. **Docstring Best Practices** – How to document an API for Python FastAPI
4. **FastAPI Starter Template** – Basic setup example
5. **FastAPI Project Generation** – Tiangolo's Full-Stack template
6. **README Guidelines** – Writing a good README.md
7. **FastAPI Automatic Docs** – Dev.to guide on built-in docs
8. **Comprehensive Docs Guide** – Apidog's ultimate documentation guide
9. **Best Practices** – Startup-level conventions
10. **Mastering FastAPI** – Technostacks article on best practices
