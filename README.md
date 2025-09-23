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

Open a virtual environment:
- Choose .venv for the environment
- Select one of the python 3.12.1 options
- Check the requirements.txt box (this installs necessary packages: uvicorn, pydantic)

Install dependencies with:
```bash
pip install "fastapi[standard]"
```

---

## Running the API
1. Clone or download this repository.

2. Start the app:
   ```bash
   fastapi dev main.py
   ```
3. Open your browser at:
   - API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

4. To open the interactive web documentation, append '/docs' to the fowarded port

---

## API Endpoints

### Get all professors
```http
GET /profs
```
sample cURL request:
```http
curl -X 'GET' \
  'https://fluffy-engine-69w4gxgjpg9hr9gj-8000.app.github.dev/prof' \
  -H 'accept: application/json'
```
Returns all professors from the JSON file.

---

### Get a professor by code
```http
GET /profs/{code}
```
sample cURL request:
```http
curl -X 'GET' \
  'https://fluffy-engine-69w4gxgjpg9hr9gj-8000.app.github.dev/profs/200' \
  -H 'accept: application/json'
```

---

### Add a new professor
```http
POST /profs
```
sample cURL request:
```http
curl -X 'POST' \
  'https://fluffy-engine-69w4gxgjpg9hr9gj-8000.app.github.dev/profs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "code": 200,
  "name": "Professor Fronchetti",
  "message": "Highest rated professor in LSU !!",
  "image_url": "https://marvel-b1-cdn.bc0a.com/f00000000290274/www.lsu.edu/eng/cse/_media/photos/photoshoot2025/fronchetti.dias.luiz.felipe.web.jpg"
}'
```

---

### Update professor by code
```http
PUT /profs/{code}
```
```
sample cURL request:
```http
curl -X 'PUT' \
  'https://fluffy-engine-69w4gxgjpg9hr9gj-8000.app.github.dev/profs/200' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "code": 200,
  "name": "Professor Fronchetti",
  "message": "Highest rated professor in LSU !! He has awesome PhD students :)",
  "image_url": "https://marvel-b1-cdn.bc0a.com/f00000000290274/www.lsu.edu/eng/cse/_media/photos/photoshoot2025/fronchetti.dias.luiz.felipe.web.jpg"
}'
```

---

### Delete professor by code
```http
DELETE /profs/{code}
```
sample cURL request:
```http
curl -X 'DELETE' \
  'https://fluffy-engine-69w4gxgjpg9hr9gj-8000.app.github.dev/profs/200' \
  -H 'accept: application/json'
```

---

### Show professor image (HTML page)
```http
GET /profs/{code}/image
```
sample cURL request:
```http
curl -X 'GET' \
  'https://fluffy-engine-69w4gxgjpg9hr9gj-8000.app.github.dev/profs/200/image' \
  -H 'accept: text/html'
```
Displays a styled HTML card with the professor’s image, name, code, and message.

---

## Members
Helena Schuler
Steven Tan
Amber Gill 
Kashvi Teli
Robert Breaux

