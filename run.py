from app import create_app
from flask_mail import Mail

config_name = "dev" #this command does work idk why
app = create_app(config_name)

mail = Mail(app)

if __name__ == '__main__':
    app.run()
