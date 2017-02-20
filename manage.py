from flask_script import Manager, Server, Shell
import main
import models
from config import Devconfig

main.app.config.from_object(Devconfig)
#Init manager object via app object
manager = Manager(main.app)

def make_shell_context():
    '''
    Create a python Cli.
    '''
    return dict(app=main.app, db=models.db, User=models.User)

#Create a new commands:Server
#This command will be run the Flask development_env server
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()