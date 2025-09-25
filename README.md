
---

### `Blog API README `
```markdown


A **FastAPI** backend for creating, reading, updating, and deleting blog posts.

---

## 🚀 Features
- Blog post CRUD operations
- MongoDB storage
- Ready for future user authentication and tagging

---

## ⚙️ Setup & Installation


- git clone https://github.com/<your-username>/blog_api.git
- cd blog_api
- pip install -r requirements.txt
- uvicorn main:app --reload --port 8003

## Docs

Swagger UI: http://127.0.0.1:8003/docs

## Env

MONGO_URI=mongodb+srv://<user>:<password>@<cluster>.mongodb.net/
DB_NAME=blog_db
