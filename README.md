# Professors API

A simple FastAPI application that manages professor data stored in a `data.json` file.  
This project demonstrates CRUD operations (GET, POST, PUT, DELETE) and returning HTML responses.

---

## Features
- List all professors
- Retrieve professor by code
- Add a new professor
- Update professor information
- Delete professor
- Display professor image with styled HTML

---

## Requirements
- Python 3.9+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- Pydantic

Install dependencies with:
```bash
pip install fastapi uvicorn pydantic
```

---

## Project Structure
```
.
├── main.py        # FastAPI application
├── data.json      # JSON "database"
└── README.md      # Project documentation
```

---

## Running the API
1. Clone or download this repository.
2. Create a `data.json` file in the same folder as `main.py`. Example:

   ```json
   {
       "professors": [
           {
               "code": 200,
               "name": "Dr. Fronchetti",
               "message": "Go Corinthians! (I hope that's the right team)",
               "image_url": "https://example.com/fronchetti.jpg"
           }
       ]
   }
   ```
3. Start the app:
   ```fastapi dev main.py
   ```
4. Open your browser at:
   - API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

5. To open the interactive web documentation, append '/docs' to the fowarded port

---

## API Endpoints

### Get all professors
```http
GET /prof
```
Returns all professors from the JSON file.

---

### Get a professor by code
```http
GET /profs/{code}
```

---

### Add a new professor
```http
POST /profs
```
Request body:
```json
{
  "code": 200,
  "name": "Dr. Fronchetti",
  "message": "I'm teaching CSC 3501",
  "image_url": "https://example.com/fronchetti.jpg"
}
```

---

### Update professor by code
```http
PUT /profs/{code}
```
Request body:
```json
{
  "code": 2,
  "name": "Dr. Fronchetti",
  "message": "Now I'm teaching CSC 4330",
  "image_url": "https://example.com/fronchetti.jpg"
}
```

---

### Delete professor by code
```http
DELETE /profs/{code}
```

---

### Show professor image (HTML page)
```http
GET /profs/{code}/image
```
Displays a styled HTML card with the professor’s image, name, code, and message.

---

