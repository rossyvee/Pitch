# from flask_script import Manager, Server
# from app.models import User
from app import create_app,db


app = create_app('production')

# manager = Manager(app)


# manager.add_command('db',MigrateCommand)
# manager.add_command('run',Server(use_debugger=True))

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User)

# @manager.command
# def test():
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    app.run()