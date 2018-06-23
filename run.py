import os
from flask import Flask

from app import create_app
# from app import views
# from app.auth import auth

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__=='__main__':
    app.run(debug=True)
