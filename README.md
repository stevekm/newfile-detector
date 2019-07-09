# newfile detector

A basic demo app that demonstrates how to use a Django ORM Standalone Application to add new files to a database (SQLite).

This app demonstrates how to use the Django ORM without a full Django app.

# Installation

First, clone this repository:

```
git clone https://github.com/stevekm/newfile-detector.git
cd newfile-detector
```

Setup a local `conda` installation to hold the Django library

```
make conda-install
```

- NOTE: configured for macOS and Linux

Initialize the Django database

```
make init
```

- Run this every time changes are made to the database structure under `db/models.py`

- the command `make reinit` can be used to erase the current database and start over from scratch

You should also generate a new `SECRET_KEY` for your `settings.py`.

If you do not wish to use a new `conda` installation as described, you can simply run the commands described in the `Makefile` with your pre-existing environment that includes a Django installation.

# Usage

Run the app with

```
make run
```

This will look inside the included `files` directory, and add listings for any files found to the database. Example:

```
$ make run
python main.py
Found files:
['files/file1.txt', 'files/file2.txt', 'files/file3.txt']

File files/file1.txt already in database: False
Added file files/file1.txt to database
File files/file2.txt already in database: False
Added file files/file2.txt to database
File files/file3.txt already in database: False
Added file files/file3.txt to database
```

Upon adding more files to the `files` directory, they will be added to the database. However, old files will be skipped:

```
$ touch files/file4.txt
$ touch files/file5.txt
$ make run
python main.py
Found files:
['files/file1.txt', 'files/file2.txt', 'files/file3.txt', 'files/file4.txt', 'files/file5.txt']

File files/file1.txt already in database: True
Did not add file files/file1.txt to database
File files/file2.txt already in database: True
Did not add file files/file2.txt to database
File files/file3.txt already in database: True
Did not add file files/file3.txt to database
File files/file4.txt already in database: False
Added file files/file4.txt to database
File files/file5.txt already in database: False
Added file files/file5.txt to database
```

You can check the contents of the database easily with a command like this:

```
$ sqlite3 db.sqlite3 'SELECT * FROM db_file'
1|files/file1.txt|/Users/kellys04/projects/newfile-detector/files/file1.txt|2019-07-09 12:44:24.388268|2019-07-09 12:44:24.388290
2|files/file2.txt|/Users/kellys04/projects/newfile-detector/files/file2.txt|2019-07-09 12:44:24.390758|2019-07-09 12:44:24.390777
3|files/file3.txt|/Users/kellys04/projects/newfile-detector/files/file3.txt|2019-07-09 12:44:24.392343|2019-07-09 12:44:24.392360
4|files/file4.txt|/Users/kellys04/projects/newfile-detector/files/file4.txt|2019-07-09 12:45:38.585296|2019-07-09 12:45:38.585318
5|files/file5.txt|/Users/kellys04/projects/newfile-detector/files/file5.txt|2019-07-09 12:45:38.587730|2019-07-09 12:45:38.587748
```

# Application Structure

- `settings.py` - The Django settings module. Contains the database configuration in it. Modify this file to match your database credentials.
- `manage.py` - Script for running Django projects.
- `main.py` - Custom code and logic goes here.

- `db` - The database configuration directory, used by Django to manage the database, contains `models.py` which contains models that define the database schema and Python interface.

# Software

Developed on macOS 10.12 High Sierra, should be compatible with most Linux installations.

- Python 3 (installed with `conda`)

- Django 2.1.5 (installed with `conda`)

- SQLite 3

- GNU `make` and `bash` for running the `Makefile` recipes for easier app initialization and running
