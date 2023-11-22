# HCL Backend

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)

## Requirements

- asgiref==3.7.2
- Django==4.2.7
- django-cors-headers==4.3.1
- django-extensions==3.2.3
- djangorestframework==3.14.0
- pytz==2023.3.post1
- sqlparse==0.4.4
- tzdata==2023.3


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kartikeyhpandey/HCL-Backend.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Running the Project

```bash
python manage.py runserver
```



