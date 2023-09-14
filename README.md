# Flask CRUD API Documentation

Introduction

This documentation outlines the Flask CRUD API implemented in the `app.py` file. The API allows you to perform basic Create, Read, Update, and Delete (CRUD) operations on a "person" resource in a MySQL database.

 Endpoints

 1. Display List of People

- **Endpoint:** `/`
- **HTTP Methods:** GET
- **Description:** Fetches a list of people from the database.
- **Response Format:** HTML template rendering the list of people.

 2. Add a New Person

- **Endpoint:** `/insert`
- **HTTP Methods:** POST
- **Description:** Adds a new person to the database.
- **Request Format:** Form data with fields: `name`, `email`, and `phone`.
- **Response:** Redirects to the home page (`/`) with a success message.

 3. Update an Existing Person

- **Endpoint:** `/update`
- **HTTP Methods:** POST (used for simplicity)
- **Description:** Modifies the details of an existing person.
- **Request Format:** Form data with fields: `id`, `name`, `email`, and `phone`.
- **Response:** Redirects to the home page (`/`) with a success message.

 4. Delete a Person

- **Endpoint:** `/delete/<person_id>`
- **HTTP Methods:** GET (used for simplicity)
- **Description:** Removes a person from the database based on their ID.
- **Response:** Redirects to the home page (`/`) with a success message.

 Environment Configuration

The following environment variables should be set in a `.env` file:

- `db_password`: MySQL database password.

 Known Limitations

- No user authentication or authorization is implemented in this API.
- The API assumes that person IDs are unique, but no constraints are in place to enforce this assumption.

 Usage

1. Clone the project repository from GitHub.

2. Create a `.env` file with the required environment variables.

3. Install the required dependencies by running:
   ```shell
   pip install -r requirements.txt
