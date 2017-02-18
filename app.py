from flask import Flask
from config import DevConfig
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)


# Get the config from object of DevConfig
app.config.from_object(DevConfig)

# Add models


class User(db.Model):

    '''Represents Proected users.'''
    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __repr__(self):
        '''Define the string format for instance of User.'''
        return '<Model User {}>'.format(self.username)

# Init manager object via app object
# This command will be run the flask_development_env server
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)


# Add commands
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# Add views


@app.route('/')
def home():
    return 'xxxxxx'

if __name__ == '__main__':
    manager.run()
