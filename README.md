FastAPI Project with Gemini Flash API Integration
This project is a FastAPI application that interacts with the Gemini Flash API to accept a query, fetch a response, and save the request and response in a PostgreSQL database. The application also streams the response back to the client.

Features
Accepts a query as input.
Calls the Gemini Flash API with the input query.
Returns the response from the Gemini Flash API.
Stores the request and response in a PostgreSQL database.
Streams the response back to the client.
Requirements
Python 3.8 or higher
PostgreSQL
Git

Getting Started
1. Clone the Repository
git clone https://github.com/Krishnagupta20/fastapi_project.git
cd fastapi_project
2. Create and Activate a Virtual Environment
3. Install Required Packages
pip install fastapi uvicorn sqlalchemy httpx psycopg2-binary dotenv

5. Set Up the PostgreSQL Database
4.1 Create a PostgreSQL Database and User
Open pgAdmin or any PostgreSQL client.
Create a new database, for example, fastapi_db.
Create a new PostgreSQL user with a username and password, for example, fastapi_user and password123.
Grant the user access to the database.
Update the Database URL in .env
In the root of your project directory, create a .env file with the following contents:
DATABASE_URL=postgresql://<username>:<password>@localhost/<database_name>
GEMINI_API_KEY=your_gemini_api_key_here
Replace:
<username> with your PostgreSQL username.
<password> with your PostgreSQL password.
<database_name> with the name of your PostgreSQL database.
your_gemini_api_key_here with your actual Gemini API key.
Example:
DATABASE_URL=postgresql://fastapi_user:password123@localhost/fastapi_db
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
5. Run Database Migrations
The project has a migration.py file to create the necessary tables in the database.
python migration.py
You should see Tables created successfully. if the migration is successful.
6. Run the FastAPI Application
Start the FastAPI application using uvicorn:
uvicorn main:app --reload
The application will be available at http://127.0.0.1:8000.
You can submit a query to the API by making a POST request to /query.
Curl of command-
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d "{\"query\": \"Explain how AI works\"}"
