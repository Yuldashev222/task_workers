# Task by "CPA Traffic Light"

### 1. Clone the Repository

```bash
git clone https://github.com/yuldashev222/task_workers.git
```

### 2. Create Virtual Environment

```bash
mkdir task_workers && cd task_workers
```

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. create database

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

### 5. Generate fake data

```bash
python3 manage.py generate_data
```

### 5. Run application

```bash
python3 manage.py runserver
```