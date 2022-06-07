## About

This code draw simple graph using data from CSV file.

## Installation

Install [Python](python.org) and libs.

After Python installation download this repository and open in terminal(or cmd)

Run command below for libs installation
```sh
pip install -r requirements.txt
```

## Usage
There is 2 options op usage

#### Simple run
You should place your data file to this dir and **rename** your file to **data.csv**
Go to this repository dir in terminal(cmd) and run comman below
```sh
python main.py
```
#### or
Run it from VScode
```sh
ctrl+f5
```
#### Advanced run
Run with params.
You can **rename** file or use file name as **parameter**.
Also you can get dotted line, send **True** as parametr

Examples:
```sh
python main.py file_name.csv True
python main.py True
python main.py file_name.csv
```
If you send nothing - program will use default values (**file_name="data.csv", dotted=False**)

Also you can edit your launch.json for run in VScode with params.
Add code below in **configurations**
```sh
"args": [
        "your_file_name.csv",
        "True"
        ],
```
