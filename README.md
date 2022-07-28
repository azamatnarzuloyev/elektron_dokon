django elektron dokon loyihasi 





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

administrator bo'limiga kirish uchun super foydalanuvchi yarating:
```
python3 manage.py createsuperuser
```
Loyihani ishga tushiring 

```
python3 manage.py runserver <port>
```
