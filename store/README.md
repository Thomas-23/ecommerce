创建项目过程

git clone https://github.com/Thomas-23/ecommerce.git

cd ecommerce

pyvenv .

windows:
    /path/to/ecommerce/Scripts/activate
类unix:
    source /path/to/ecommerce/bin/activate

cd store

pip install -r requirements-devel.txt

创建sqlite数据库
python manage.py migrate

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata category/fixtures/category.json

python manage.py createsuperuser

python manage.py runserver 8001
--------------------------------------------

测试能够访问到接口数据

http GET http://127.0.0.1:8001/products/

HTTP/1.0 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Date: Thu, 07 Apr 2016 09:05:30 GMT
Server: WSGIServer/0.2 CPython/3.5.0
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "brand": "豹纹",
        "categories": [
            1
        ],
        "created": "2016-04-07T07:04:37.283953Z",
        "description": "新款吉他，深受年轻朋友的喜爱，已经卖出100w台",
        "id": 1,
        "image": "image_name",
        "is_active": true,
        "is_best_seller": false,
        "is_featured": false,
        "meta_description": "乐器",
        "meta_keywords": "吉他,乐器",
        "name": "吉他",
        "old_price": "550.00",
        "price": "600.00",
        "quantity": 50,
        "sku": "sku code",
        "updated": "2016-04-07T08:59:02.220190Z"
    }
]
