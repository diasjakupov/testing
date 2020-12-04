import os
import subprocess

# auto using command autopep8
ls = os.listdir()
for i in ls:
    if i not in ['db.sqlite3', 'manage.py', 'utils.py', 'frontend', 'media']:
        abss = os.path.abspath(i)
        for j in os.listdir(i):
            if j not in [
                'apps.py',
                'tests.py',
                'migrations',
                '__init__.py',
                '__pycache__',
                'asgi.py',
                'settings.py',
                    'wsgi.py']:
                item = os.path.basename(j)
                path = rf'{abss}\{item}'
                print(path)
                subprocess.call(
                    f'autopep8 --in-place --aggressive --aggressive {path}',
                    shell=True)
