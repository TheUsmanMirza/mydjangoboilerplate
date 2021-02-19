# mydjangoboilerplate
A basic django boilerplate providing the feature of 
- django debug-toolbar
- separate settings files for production and development
- secret file handling for secret keys
<br> and many other features

#### Clone the repository
```
git clone https://github.com/TheUsmanMirza/mydjangoboilerplate.git 
```
#### Go to the directory and create and activate virtual env

```
cd mydjangoboilerplate
python3 -m venv venv
source venv/bin/activate
```

#### install requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```

#### Run the server
```
python manage.py runserver
```

#### Note: You can rename the project if you want by this command
```
python manage.py rename your-new-project-name
```