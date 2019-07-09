import os
import glob

# Initailize Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from db.models import File

def get_file_list(files_dir = "files"):
    glob_pattern = os.path.join(files_dir, '*')
    files = glob.glob(glob_pattern)
    return(files)

def add_file(filename):
    """
    Add the file to the database if it does not already exist
    Skips creation for files that already exist, based on provided filename
    """
    instance, created = File.objects.get_or_create(filename = filename)
    return(created)

def file_in_database(filename):
    """
    Checks if a file is already in the database
    """
    return(File.objects.filter(filename = filename).exists())

def main():
    files = get_file_list()
    print("Found files:\n{0}\n".format(files))
    for file in files:
        is_in_db = file_in_database(filename = file)
        print("File {0} already in database: {1}".format(file, is_in_db))
        created = add_file(filename = file)
        if created:
            print("Added file {0} to database".format(file))
        else:
            print("Did not add file {0} to database".format(file))

if __name__ == '__main__':
    main()
