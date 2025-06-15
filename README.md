# Documentation

[![Read The Doc link](https://python-oc-lettings-doc.readthedocs.io/en/latest/)](https://python-oc-lettings-doc.readthedocs.io/en/latest/)

# Installation

This guide will help you install and run the project on **Windows**, **Linux/macOS**, or using **Docker**.

---

## Windows

1. **Clone the repository:**

   ```powershell
   git clone https://github.com/HDanDev/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   ```

2. **Create a virtual environment and activate it:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```powershell
   python manage.py migrate
   ```

5. **Start the development server:**

   ```powershell
   python manage.py runserver
   ```

6. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Linux / macOS

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HDanDev/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

6. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Docker (using Docker Hub)

1. **Pull the image from Docker Hub:**

   ```bash
   docker pull hdandev/oc-lettings:latest
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 8000:8000 hdandev/oc-lettings:latest
   ```

3. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

**If you want to build the Docker image yourself:**

1. **Build the image:**

   ```bash
   docker build -t your-dockerhub-username/your-image-name .
   ```

2. **Push it to Docker Hub:**

   ```bash
   docker push your-dockerhub-username/your-image-name
   ```

# Linting

   ```bash
   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   flake8
   ```

# Tests

   ```bash
   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   pytest
   ```

# Database

Start shell session:
   ```bash
   cd /path/to/Python-OC-Lettings-FR
   sqlite3
   ```

Connect to database:
   ```bash
   .open oc-lettings-site.sqlite3
   ```

Display tables:
   ```bash
   .tables
   ```

Display columns:
   ```bash
   pragma table_info(Python-OC-Lettings-FR_profile);
   ```

Custom query:
   ```bash
   select user_id, favorite_city from
   Python-OC-Lettings-FR_profile where favorite_city like 'B%';
   ```

End session:
   ```bash
   .quit
   ```

# Connect as administrator

[Admin login URL](http://localhost:8000/admin)

Username: `admin`
Password: `Abc1234!`
