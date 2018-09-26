import os

app = input('App name: ')

parent_folders = ['static', 'templates']

if os.path.exists(app):

    print('App exists. Completing app...', end='')

    for folder in parent_folders:

        sub_path = os.path.join(app, folder)

        os.mkdir(sub_path)

        sub_path2 = os.path.join(sub_path, app)
        
        os.mkdir(sub_path2)

        if folder == 'static':
            os.mkdir(os.path.join(sub_path2, 'css'))
            os.mkdir(os.path.join(sub_path2, 'images'))
            os.mkdir(os.path.join(sub_path2, 'js'))

    urls_file_path = os.path.join(app, 'urls.py')
    with open(urls_file_path, 'w') as f:
        
        code = '''from django.conf.urls import url
from .views import *

app_name = '{app_name}'

urlpatterns = [

    # HTTP URLs

    # AJAX URLs

]
'''.format(
    app_name=app
)
        f.write(code)

    print('DONE')

else:
    print('App doesn\'t exist')
