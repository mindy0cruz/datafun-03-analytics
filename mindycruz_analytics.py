# Project 3 emphasizes skills in using Git for version control, creating and managing Python virtual environments, and handling different types of data. The project involves fetching data from the web, processing it using appropriate Python collections, and writing the processed data to files.
# Std Lib Imports
import pathlib
import csv
import os
import json

# External lib imports (requires virtual environment)
import requests
from collections import Counter
import pandas as pd
import xlrd

#Fetch Data Functions

##Fetch JSON w/exception

def fetch_and_write_json_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
    finally:
        print(f"Finished attempting to fetch and write JSON data from {url}")

##Fetch CSV w/exception

def fetch_and_write_csv_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
    finally:
        print(f"Finished attempting to fetch and write CSV data from {url}")

##Fetch Excel w/exception

def fetch_and_write_excel_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
    finally:
        print(f"Finished attempting to fetch and write Excel data from {url}")


##Fetch Plain Text w/exception

def fetch_and_write_txt_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
    finally:
        print(f"Finished attempting to fetch and write text data from {url}")

#Write Data Functions

##Write JSON

def write_json_file(folder_name, filename, data):
    try:
        file_path = pathlib.Path(folder_name) / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)  
        with file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"JSON data saved to {file_path}")
    except IOError as e:
        print(f"Failed to write JSON file: {e}")

##Write CSV

def write_csv_file(folder_name, filename, data):
    try:
        file_path = pathlib.Path(folder_name) / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)  
        with file_path.open('w', newline='', encoding='utf-8') as file:
            file.write(data)
        print(f"CSV data saved to {file_path}")
    except IOError as e:
        print(f"Failed to write CSV file: {e}")

##Write Excel

def write_excel_file(folder_name, filename, data):
    try:
        file_path = pathlib.Path(folder_name) / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)  
        with file_path.open('wb') as file:
            file.write(data)
        print(f"Excel data saved to {file_path}")
    except IOError as e:
        print(f"Failed to write Excel file: {e}")

##Write Plain Text

def write_txt_file(folder_name, filename, data):
    try:
        file_path = pathlib.Path(folder_name) / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)  
        with file_path.open('w', encoding='utf-8') as file:
            file.write(data)
        print(f"Text data saved to {file_path}")
    except IOError as e:
        print(f"Failed to write text file: {e}")

#Process Data

##JSON

def process_excel_file(input_folder, input_filename, output_filename):
    file_path = pathlib.Path(input_folder) / input_filename
    data = pd.read_excel(file_path)

    row_count = data.shape[0]
    column_count = data.shape[1]
    summary = data.describe()

    output_path = pathlib.Path(input_folder) / output_filename
    with output_path.open('w', encoding='utf-8') as file:
        file.write(f"Total Rows: {row_count}\n")
        file.write(f"Total Columns: {column_count}\n")
        file.write("Summary Statistics:\n")
        file.write(summary.to_string())
    
    print(f"Excel analysis saved to {output_path}")

##CSV

def process_csv_file(input_folder, input_filename, output_filename):
    file_path = pathlib.Path(input_folder) / input_filename
    with file_path.open('r', encoding='utf-8') as file:

        reader = csv.reader(file)
        header = next(reader)
        rows = [tuple(row) for row in reader]


    column_count = len(header)
    

    output_path = pathlib.Path(input_folder) / output_filename
    with output_path.open('w', encoding='utf-8') as file:

        file.write(f"Total Columns: {column_count}\n")
        
        for column, summary in column_summaries.items():
            file.write(f"{column_count}: {summary[:5]} (showing first 5 values)\n")
    
    print(f"CSV analysis saved to {output_path}")


##TEXT

def process_txt_file(input_folder, input_filename, output_filename):
    file_path = pathlib.Path(input_folder) / input_filename
    with file_path.open('r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    word_count = len(words)
    word_frequency = {word: words.count(word)}

    output_path = pathlib.Path(input_folder) / output_filename
    with output_path.open('w', encoding='utf-8') as file:
        file.write(f"Total Words: {word_count}\n")
        for word, freq in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True):
            file.write(f"{word}: {freq}\n")
    
    print(f"Text analysis saved to {output_path}")

##EXCEL

def process_excel_file(input_folder, input_filename, output_filename):
    file_path = pathlib.Path(input_folder) / input_filename
    data = pd.read_excel(file_path)

    row_count = data.shape[0]

    output_path = pathlib.Path(input_folder) / output_filename
    with output_path.open('w', encoding='utf-8') as file:
        file.write(f"Total Rows: {row_count}\n")

        print(f"Excel analysis saved to {output_path}")



#MAIN


def main():
    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    json_url = 'http://api.open-notify.org/astros.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    process_txt_file(txt_folder_name, txt_filename, 'results_txt.txt')
    process_csv_file(csv_folder_name, csv_filename, 'results_csv.txt')
    process_excel_file(excel_folder_name, excel_filename, 'results_excel.txt')
    process_json_file(json_folder_name, json_filename, 'results_json.txt')

if __name__ == '__main__':
    main()
