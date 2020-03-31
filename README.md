# awesomebat


## Cài đặt

Đầu tiên, tải repository về máy tính:

```bash
git clone https://github.com/batTrung/awesomebat.git
```

Cài đặt requirements:

```bash
cd awesomebat
pip install -r requirements/dev.txt
```

Tạo database:

```bash
python manage.py makemigrations users
python manage.py migrate
```

Chạy development server:

```bash
python manage.py runserver
```

Mở Chrome hay FireFox : **127.0.0.1:8000**
