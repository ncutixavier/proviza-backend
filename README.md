# FastAPI MongoDB Project 🚀

Welcome to the FastAPI MongoDB project! This project demonstrates how to build a RESTful API using FastAPI with MongoDB for data storage.

## Features 🌟

- Connects to a MongoDB database
- Performs CRUD operations on user data
- Includes basic data validation
- Filters and returns only valid data

## Installation 🛠️

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ncutixavier/proviza-backend
   cd proviza-backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file referring to `.env.example`:**

   Create a `.env` file in the project root with the following content:

   ```env
   MONGODB_URL=mongodb://localhost:27017/db_name
   ```

## Usage 🚀

To run the FastAPI application with auto-reload enabled, use the following command:

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000` in your browser to access the API.

## Endpoints 📍

- **GET `/api/v1/users`**: Retrieve a list of users. Only valid users based on defined criteria are returned.

- **POST `/api/v1/users`**: Create a new user. Ensures no duplicate email or phone number exists.

## Environment Variables 🌱

- `MONGODB_URL`: URL for connecting to your MongoDB instance (e.g., `mongodb://localhost:27017/quizzapp_db`).

- `DB_NAME`: The name of the MongoDB database to use (default is `quizzapp_db`).

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding! 😊 If you have any questions, feel free to open an issue or submit a pull request.
