import os.path
import shutil
import zipfile

import pytest

RESOURCES_DIRECTORY = os.path.abspath('resources')
FILES_DIRECTORY = os.path.join(RESOURCES_DIRECTORY, 'files')
ZIP_DIRECTORY = os.path.join(RESOURCES_DIRECTORY, 'zip_files')

@pytest.fixture(scope='session')
def create_zip_file():
    if not os.path.isdir(ZIP_DIRECTORY):
        os.mkdir(ZIP_DIRECTORY)

    zip_file_name = os.path.join(ZIP_DIRECTORY, 'ZIP_file.zip')
    files = os.listdir(FILES_DIRECTORY)
    with zipfile.ZipFile(zip_file_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        for file in files:
            file_path = os.path.join(FILES_DIRECTORY, file)
            zip_file.write(file_path, file)
    yield zip_file_name

    if os.path.isdir(ZIP_DIRECTORY):
        shutil.rmtree(ZIP_DIRECTORY)