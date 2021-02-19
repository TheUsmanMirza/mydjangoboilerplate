import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Rename a Django project"

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help="The new Django project name")

    def handle(self, *args, **options):
        new_project_name = options['new_project_name']

        # logic to rename project
        files_to_rename = ['myboilerplate/settings/base.py', 'myboilerplate/wsgi.py', 'manage.py']
        folder_to_rename = 'myboilerplate'

        for file in files_to_rename:
            with open(file, 'r') as f:
                file_data = f.read()

            file_data = file_data.replace('myboilerplate', new_project_name)

            with open(file, 'w') as f:
                f.write(file_data)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS("Project has been renamed to {}".format(new_project_name)))