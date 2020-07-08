import os

from app import create_app
from instance.config import config_level

#config_name = os.getenv('APP_SETTINGS') # config_name = "development"
config_name = config_level

app = create_app(config_name)

if __name__ == '__main__':
    app.run()

