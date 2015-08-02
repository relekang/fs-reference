import sys
import os
from fabric.decorators import task
from fabric.state import env
from django_fabric import App

env.hosts = ['filtersystem@s8.wservices.ch']
sys.path.append(os.path.dirname(__file__))


class Site(App):
    project_paths = {
        'prod': '/home/filtersystem/fs_ref',
    }
    project_package = 'fs_ref'
    restart_command = {
        'prod': '/home/filtersystem/init/fs_ref restart'
    }


site = Site()
deploy = task(site.deploy)
test = task(site.test)
