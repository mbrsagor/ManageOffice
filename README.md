# Manage Office

> The application is basically backend web API application which the application manage employees and office curriculum activities.

Please follow the instructions to run the application your systems.
#### Setup:
```bash
git clone https://github.com/mbrsagor/MnageOffice.git
cd MnageOffice
```
Then create .env file and paste code from `example.env` file and add validate information.

```bash
|--> example.env
|--> .env
```

###### Step 2:
```bash
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations accounts
./manage.py migrate accounts
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

#### Install postgresql
```bash
pip install psycopg2-binary
```
