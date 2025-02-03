# Django CRUD with Multiple Authentication

## Overview
This project is a Django-based CRUD application with multiple authentication roles, including authors. It allows users to perform Create, Read, Update, and Delete operations on various models while maintaining authentication and authorization.

## Features
- User authentication with multiple roles
- CRUD operations for managing data
- Secure user management
- Django Admin panel integration
- Responsive design with Django templates

## Installation

### Prerequisites
- Python 3.x
- Django
- Virtual Environment (Recommended)

### Setup Guide
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Binaryx01/multicrudproject.git
   cd your-repo
   ```

2. **Create and Activate Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```



4. **Create a Superuser**
   ```sh
   python manage.py createsuperuser
   ```

5. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   The project will be accessible at `http://127.0.0.1:8000/`.

## Usage
- Register and log in as a user
- Perform CRUD operations based on user roles
- Access Django Admin at `/admin/`

## Project Structure
```
project_root/
│── crudapp/
│   ├── models.py  # Database models
│   ├── views.py   # Application views
│   ├── urls.py    # URL routing
│   ├── templates/ # HTML Templates
│   └── static/    # Static files (CSS, JS)
│── projectname/
│   ├── settings.py # Project settings
│── manage.py  # Django CLI
│── requirements.txt  # Python dependencies
└── .gitignore  # Files to exclude from Git
```

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, contact: `adhikariishwor013@gmail.com`

