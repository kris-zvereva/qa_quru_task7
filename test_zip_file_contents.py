import os
import zipfile

from pypdf import PdfReader
import io
import csv
import pandas



def test_zip_file_created(create_zip_file):
    assert os.path.isfile(create_zip_file)
    assert create_zip_file.endswith('ZIP_file.zip')


def test_all_files_exist_in_zip(create_zip_file):
    with zipfile.ZipFile(create_zip_file, mode='r') as archive:
        assert archive.namelist() == ['test.csv', 'test.pdf', 'test.xlsx']


def test_pdf_file(create_zip_file):
    expected_text = 'labadabadabda'
    with zipfile.ZipFile(create_zip_file, mode='r') as archive:
        with archive.open('test.pdf') as pdf:
            reader = PdfReader(pdf)
            assert len(reader.pages) == 1
            assert expected_text in reader.pages[0].extract_text()

def test_csv_file(create_zip_file):
    expected_text = 'extra something for csv format'
    with zipfile.ZipFile(create_zip_file, mode='r') as archive:
        with archive.open('test.csv') as csv_file:
            df = pandas.read_csv(csv_file)
            assert expected_text in df.to_string()


def test_xlsx_file(create_zip_file):
    expected_text = 'test column'
    with zipfile.ZipFile(create_zip_file, mode='r') as archive:
        with archive.open('test.xlsx') as xlsx_file:
            df = pandas.read_excel(xlsx_file)
            assert expected_text in df.columns