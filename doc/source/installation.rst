Installation
============

This guide will help you install and run the project on Windows, Linux/macOS, or using Docker.

Windows
-------

1. **Clone the repository:**

   .. code-block:: powershell

      git clone https://github.com/HDanDev/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. **Create a virtual environment and activate it:**

   .. code-block:: powershell

      python -m venv venv
      .\venv\Scripts\activate

3. **Install the required dependencies:**

   .. code-block:: powershell

      pip install -r requirements.txt

4. **Run database migrations:**

   .. code-block:: powershell

      python manage.py migrate

5. **Start the development server:**

   .. code-block:: powershell

      python manage.py runserver

6. **Open your browser at** http://127.0.0.1:8000

Linux / macOS
-------------

1. **Clone the repository:**

   .. code-block:: bash

      git clone https://github.com/HDanDev/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. **Create a virtual environment and activate it:**

   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

3. **Install the required dependencies:**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Run database migrations:**

   .. code-block:: bash

      python manage.py migrate

5. **Start the development server:**

   .. code-block:: bash

      python manage.py runserver

6. **Open your browser at** http://127.0.0.1:8000

Docker (using Docker Hub)
-------------------------

1. **Pull the image from Docker Hub:**

   .. code-block:: bash

      docker pull hdandev/oc-lettings:latest

2. **Run the Docker container:**

   .. code-block:: bash

      docker run -p 8000:8000 hdandev/oc-lettings:latest

3. **Open your browser at** http://127.0.0.1:8000

---

If you want to build the Docker image yourself:

1. **Build the image:**

   .. code-block:: bash

      docker build -t your-dockerhub-username/your-image-name .

2. **Push it to Docker Hub:**

   .. code-block:: bash

      docker push your-dockerhub-username/your-image-name
