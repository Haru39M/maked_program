PowerShell -command
.\venv\Scripts\activate
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
cd .\WEBAPP\flask-tutorial
flask run