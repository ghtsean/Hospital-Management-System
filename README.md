# Hospital Management System

An open-source hospital management system built with **Python (Flask)** and **MySQL**.  
This demo web application is designed to help small hospitals manage their daily operations more efficiently.

## Features

- Patient registration and management
- Doctor and appointment scheduling
- Lab test and prescription management
- User authentication and registration
- Simple, extensible architecture using Flask and SQLAlchemy

## Tech Stack

- **Backend:** Python, Flask  
- **Database:** MySQL (default is SQLite for local development)  
- **Frontend:** HTML, CSS, JavaScript  
- **Other:** Docker support, virtual environment recommended  

## Getting Started

Follow these steps to run the project locally.

### 1. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
```

### 2. Install Dependencies

From the project root directory, install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

By default, the app can run with SQLite. To use MySQL (or another database), set the `DATABASE_URI` environment variable:

```bash
export DATABASE_URI="mysql+pymysql://<username>:<password>@<host>:<port>/<database>"
```

On Windows (PowerShell), you can set it with:

```powershell
$env:DATABASE_URI = "mysql+pymysql://<username>:<password>@<host>:<port>/<database>"
```

### 4. Initialize the Database

Before running the app for the first time, initialize the database schema:

```python
from utils.database import Base, engine
Base.metadata.create_all(bind=engine)
```

### 5. Run the Application

From the project directory, start the Flask app:

```bash
python app.py
```

### 6. Access the Application

Once the app is running, open your browser and navigate to:

```text
http://localhost:5000/
```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

> Note: Please target your pull requests to the `develop` branch.

## License

This project is open-source and available under the [MIT License](LICENSE).
