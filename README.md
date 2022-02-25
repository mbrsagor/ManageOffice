# Manage Office

> The application is basically backend web API application which the application manage employees and office curriculum activities.

Please follow the instructions to run the application your systems.
#### Setup:

###### Dependencies:-
- Python 3.8
- Postgresql 14.1

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```bash
git clone https://github.com/mbrsagor/manageOffice.git
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
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

#### Install postgresql
```bash
pip install psycopg2-binary
```

##### Create Postgresql database: Example
>1st open your terminal and follow the commands.
- ```psql postgres```
```bash
CREATE DATABASE db_name;
\q
```
