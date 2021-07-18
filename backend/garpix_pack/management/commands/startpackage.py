import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from distutils.core import run_setup
import subprocess


def snake_to_camel_case(text_snake):
    return '{}'.format(
        text_snake.title().replace('_', ''),
    )


def generate_init(package_name):
    return f"""default_app_config = '{package_name}.apps.{snake_to_camel_case(package_name)}Config'
"""


def generate_apps(package_name):
    return f"""from django.apps import AppConfig


class {snake_to_camel_case(package_name)}Config(AppConfig):
    name = '{package_name}'
    verbose_name = '{snake_to_camel_case(package_name)}'
"""


def generate_manifest(package_name):
    return f"""recursive-include {package_name} *"""


def generate_setup_py(package_name):
    return f"""from setuptools import setup, find_packages
from os import path
from m2r import convert
from django.conf import settings


with open(path.join(settings.BASE_DIR, '..', 'README.md'), encoding='utf-8') as f:
    long_description = convert(f.read())

setup(
    name='{package_name}',
    version='1.0.0',
    description='',
    long_description=long_description,
    url='https://github.com/garpixcms/{package_name}',
    author='Garpix LTD',
    author_email='info@garpix.com',
    license='MIT',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'garpixcms >= 1.7.0',
    ],
)

"""


class Command(BaseCommand):
    help = 'Create new app as package'

    def add_arguments(self, parser):
        parser.add_argument('package_name', type=str)

    def handle(self, *args, **options):
        package_name = options['package_name']
        self.stdout.write(f'Create new package: {package_name}')
        package_dir = os.path.join(settings.BASE_DIR, package_name)
        os.makedirs(package_dir, exist_ok=True)
        # setup.py
        with open(os.path.join(package_dir, 'setup.py'), 'w') as f:
            f.write(generate_setup_py(package_name))
        # MANIFEST.in
        with open(os.path.join(package_dir, 'MANIFEST.in'), 'w') as f:
            f.write(generate_manifest(package_name))
        # apps.py
        with open(os.path.join(package_dir, 'apps.py'), 'w') as f:
            f.write(generate_apps(package_name))
        # __init__.py
        with open(os.path.join(package_dir, '__init__.py'), 'w') as f:
            f.write(generate_init(package_name))
        self.stdout.write(self.style.SUCCESS('Done'))
