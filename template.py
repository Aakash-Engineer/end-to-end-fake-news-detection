import os
from pathlib import Path



PROJECT_NAME = 'FakeNewsDetection'

# list of files to be created

list_of_files = [
    f'src/{PROJECT_NAME}/__init__.py',
    f'src/{PROJECT_NAME}/config/__init__.py',
    f'src/{PROJECT_NAME}/config/configuration.py',
    f'src/{PROJECT_NAME}/components/__init__.py',
    f'src/{PROJECT_NAME}/utils/__init__.py',
    f'src/{PROJECT_NAME}/utils/common.py',
    f'src/{PROJECT_NAME}/pipeline/__init__.py',
    f'src/{PROJECT_NAME}/entity/__init__.py',
    f'src/{PROJECT_NAME}/entity/config_entity.py',
    f'src/{PROJECT_NAME}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/ndex.html',
    'Dockerfile',
    '.github/workflows/.gitkeep'
]

# create template structure

for filename in list_of_files:
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filename, 'w') as file:
            pass
        
