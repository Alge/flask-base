import os
from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import models
from instance.config import config_level


app = create_app(config_name=config_level)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    "Load some initial data into the DB. Only use during dev..."
    user = models.User("admin@example.com", "admin", "password")
    user.id_admin = True
    user.save()

if __name__ == '__main__':
    manager.run()
