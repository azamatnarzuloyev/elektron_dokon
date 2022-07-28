# Django E-Commerce 
django elektron dokon to'liq yaratilgan 




install virtualenv:
```
pip install virtualenv
```

create virtual environment:
```
virtualenv venv
```

activate virtual environment:
```
cd venv\Scripts\activate
```

Agar siz Widows PowerShell-dan foydalansangiz, virtual muhitni faollashtirishdan oldin PowerShell-ga ushbu buyruqni kiriting:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

### install requirements and run project

install requirements:
```
pip install -r requirements.txt
```

preparing DataBase:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
```

create super user for access to admin section:
```
python3 manage.py createsuperuser
```
*fill necessary fields*

run project on localhost (default port: 8000):
```
python3 manage.py runserver <port>
```
