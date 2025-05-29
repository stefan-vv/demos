#!usr/bin/env python

import os
from os.path import dirname, join
import platform
import subprocess
import sys
import logging
from venv import EnvBuilder


def get_logger(name):
    """Add export to a txt file"""
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] [%(process)s] [%(name)s] [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log


venv_logger = get_logger('build_virtual_environment')


class VirtualEnvironmentBuilder:

    def __init__(self):
        self.requirements_dir = join(
            dirname(__file__),
            'requirements'
        )
        self.venv_path = join(os.getcwd(), '..', 'venv')

    def build_virtual_environment(self):
        venv_logger.info('Starting build virtual environment...')

        builder = EnvBuilder(with_pip=True, clear=True)
        builder.create(self.venv_path)

        venv_logger.info('Done building virtual environment, venv is in %s', self.venv_path)

    def install_requirements(self):
        requirements_file_path = join(
            self.requirements_dir,
            'requirements.txt'
        )
        py_exec_path = join(self.venv_path,'Scripts', 'python.exe') \
            if platform.system() == 'Windows' else join(self.venv_path,'bin', 'python')

        cmd = f'{py_exec_path} -m pip install -r {requirements_file_path}'

        venv_logger.info('Installing requirements from %s', requirements_file_path)
        venv_logger.info('Running command %s', cmd)
        subprocess.run(cmd.split(), check=True)
        venv_logger.info('Done installing requirements')


def main():
    venv_builder = VirtualEnvironmentBuilder()
    venv_builder.build_virtual_environment()
    venv_builder.install_requirements()


if __name__ == '__main__':
    main()
