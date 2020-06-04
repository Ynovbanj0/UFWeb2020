-- Install packages
> pip install -r requirements.txt

-- To create the database structure
> flask db init 
> flask db migrate
> flask db upgrade

-- Start the server
> set FLASK_APP=run.py
> flask run