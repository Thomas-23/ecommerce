开发过程记录
------------------

```
pyvenv ecommerce

cd ecommerce

git init .
```

创建一个 .gitignore 文件,内容如下:

```
/Include
/Lib
/Scripts
/pip-selfcheck.json
/pyvenv.cfg
/store/.idea
/store/category/migrations
/store/category/__pycache__
/store/db.sqlite3
/store/env.bat
```

创建一个 README.md 文件 

提交文件
```
git commit -a "commit description"
git remote add origin https://github.com/Thomas-23/ecommerce.git
git push -u origin master
```

激活虚拟环境
`ecommerce/Scripts/activate`

安装需要的包

```
pip install 
django 
djangorestframework 
django-filter
httpie
```

创建项目
```
django-admin startproject store
cd store
python manage.py startapp category
```

配置app, 将app加入到settings文件INSTALLED_APPS中
```
'rest_framework',
'category',
```

创建数据库
```
python manage.py migrate
python manage.py makemigrations
```






