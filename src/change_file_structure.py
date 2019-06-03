#!/usr/bin/env python3

import os
import sys
import shutil
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('.')
sys.path.append('ROOT_DIR')


"""

Run like so: $ python src/change_file_structure <SOURCE_DIR> <DESTINATION_DIR>

Runs in Python 3.6 (at least on GNU-Linux).

Naive implementation to convert a file-type-oriented file structure such as:

dir__
     |_raw__day1__file1
     |    |     |_file2
     |    |        :
     |    |
     |    |_day2__file3
     |          |_file4
     |          |_file5
     |             :
     |      
     |_tif__day1 _file6
     |    |     |_file7
     |    |        :
     |    |
     |    |_day2__file8
     |          |_file9
     |          |_file10
     |             :
     |       
     |_dev__day1__file11
     |    |     |_file12
     |    |        :
     |    |
     |    |_day2__file13
     |          |_file14
     |          |_file15
     |             :
     :


into a date-oriented file structure:

dir__day1__raw__file1
     |  |     |_file2
     |  |         :
     |  |
     |  |__tif__file6
     |  |     |_file7
     |  |         :
     |  |
     |  |__def__file11
     |        |_file12
     |           :
     |
     day2__raw__file3
     |  |     |_file4
     |  |     |_file5
     |  |         :
     |  |
     |  |__tif__file8
     |  |     |_file9
     |  |     |_file10
     |  |         :
     |  |
     |  |__def__file13
     |        |_file14
     |        |_file15
     |           :
     :
     
Only copies, but does not delete, the original structure to the destination directory.
    
"""


def change_file_structure():

    source = sys.argv[1]
    dest = sys.argv[2]
    image_types = (sys.argv[3], sys.argv[4], sys.argv[5])

    # image_types = ('raw', 'tiff', 'developed')
    date_dirs = get_date_folders(source, image_types)
    create_dest_dirs(dest, date_dirs, image_types)
    write_image_files_to_dest(source, dest, date_dirs, image_types)


def get_date_folders(source, image_types) -> set:
    # Get set of date folders.
    date_dirs = set()
    for image_type in image_types:
        date_dirs.update(os.listdir(f'{source}/{image_type}'))
    return date_dirs


def create_dest_dirs(dest: str, dirs: set, image_types: tuple):
    for _dir in dirs:
        for image_type in image_types:
            Path(os.path.join(dest, _dir, image_type)).mkdir(parents=True, exist_ok=True)


def write_image_files_to_dest(source, dest, date_dirs, images_types):
    for day in date_dirs:
        for image_type in images_types:
            path_source = os.path.join(source, image_type, day)
            files = get_files(path_source)
            for file in files:
                shutil.copy(file, os.path.join(dest, day, image_type))


def get_files(path: str) -> list:
    files = []
    for root, dirs, files_ in os.walk(path):
        for file in files_:
            files.append(os.path.join(root, file))
    return files


if __name__ == '__main__':
    change_file_structure()
