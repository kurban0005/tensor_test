import os
import subprocess
import sys
from loguru import logger

def create_venv(venv_name='.venv'):
    """Создает виртуальную среду, если её не существует."""
    if not os.path.exists(venv_name):
        logger.info(f'\nСоздание виртуальной среды: "{venv_name}" ...\n')
        subprocess.check_call([sys.executable, '-m', 'venv', venv_name])
    else:
        logger.info(f'\nВиртуальная среда "{venv_name}" уже существует.\n')


def install_requirements(venv_name='.venv'):
    """Устанавливает зависимости из requirements.txt."""
    pip = os.path.join(venv_name, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(venv_name, 'bin', 'pip')

    if os.path.exists('requirements.txt'):
        logger.info('\nУстановка библиотек из "requirements.txt" ...\n')
        subprocess.check_call([pip, 'install', '-r', 'requirements.txt'])
        process = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
        logger.info(f'\n{process.stdout}\n')
    else:
        logger.info('\nФайл requirements.txt не найден.\n')


if __name__ == '__main__':
    create_venv()
    install_requirements()
