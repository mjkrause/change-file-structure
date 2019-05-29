#!usr/bin/env python3

import unittest
import sys
import os
import shutil
from pathlib import Path
from src.change_file_structure import get_date_folders, create_dest_dirs, write_image_files_to_dest


class TestDriver(unittest.TestCase):

    # Set up command line arguments for unit tests.
    SOURCE = '/tmp/k1'
    DEST = '/tmp/new/k1'

    def setUp(self) -> None:

        # Set up directory and file structure as found in the source.

        raw_path = os.path.join(self.SOURCE, 'raw')
        tiff_path = os.path.join(self.SOURCE, 'tiff')
        developed_path = os.path.join(self.SOURCE, 'developed')

        paths = (raw_path, tiff_path, developed_path)
        days = ('2000-01-01', '2000-01-02', '2000-01-03')

        self.raw_files1 = ('IMG1000.PEF', 'IMG1000.ppm', 'IMG1001.PEF', 'IMG1002.PEF')
        self.raw_files2 = ('IMG1003.PEF', 'IMG1003.ppm', 'IMG1004.PEF', 'IMG1005.PEF')
        self.raw_files3 = ('IMG1006.PEF', 'IMG1007.PEF', 'IMG1008.PEF')

        self.tiff_files1 = ('IMG1000.TIF', 'IMG1001.TIF', 'IMG1002.TIF')
        self.tiff_files2 = ('IMG1003.TIF', 'IMG1004.TIF', 'IMG1005.TIF')
        self.tiff_files3 = ('IMG1006.TIF', 'IMG1007.TIF', 'IMG1008.TIF')

        self.developed_files1 = ('IMG1000.xcf', 'IMG1000.jpg', 'IMG1000.jpg1234', 'IMG1001.xcf',
                                 'IMG1001.jpeg', 'IMG1002.xcp', 'IMG1002.jpg')
        self.developed_files2 = ('IMG1003.xcf', 'IMG1003.jpg', 'IMG1003.jpg1234', 'IMG1004.xcf',
                                 'IMG1004.jpeg', 'IMG1005.xcp', 'IMG1005.jpg')
        self.developed_files3 = ('IMG1006.xcf', 'IMG1006.jpg', 'IMG1006.jpg1234', 'IMG1007.xcf',
                                 'IMG1007.jpeg', 'IMG1008.xcp', 'IMG1008.jpg')

        for _path in paths:
            for day in days:
                Path(f'{_path}/{day}').mkdir(parents=True, exist_ok=True)
                if day == '2000-01-01':
                    if _path == raw_path:
                        for _file in self.raw_files1:
                            Path(f'{_path}/{day}/{_file}').touch()
                    elif _path == tiff_path:
                        for _file in self.tiff_files1:
                            Path(f'{_path}/{day}/{_file}').touch()
                    elif _path == developed_path:
                        for _file in self.developed_files1:
                            Path(f'{_path}/{day}/{_file}').touch()
                elif day == '2000-01-02':
                    if _path == raw_path:
                        for _file in self.raw_files2:
                            Path(f'{_path}/{day}/{_file}').touch()
                    elif _path == tiff_path:
                        for _file in self.tiff_files2:
                            Path(f'{_path}/{day}/{_file}').touch()
                    elif _path == developed_path:
                        for _file in self.developed_files2:
                            Path(f'{_path}/{day}/{_file}').touch()
                elif day == '2000-01-03':
                    if _path == raw_path:
                        for _file in self.raw_files3:
                            Path(f'{_path}/{day}/{_file}').touch()
                    elif _path == tiff_path:
                        for _file in self.tiff_files3:
                            Path(f'{_path}/{day}/{_file}').touch()
                    elif _path == developed_path:
                        for _file in self.developed_files3:
                            Path(f'{_path}/{day}/{_file}').touch()

        self.image_types = ('raw', 'tiff', 'developed')
        self.dir_set = {'2000-01-01', '2000-01-03', '2000-01-02'}

    def tearDown(self) -> None:
        shutil.rmtree('/tmp/k1')

    def test_setup(self):
        observed = os.listdir('/tmp/k1')
        expected = ['raw', 'developed', 'tiff']
        self.assertEqual(observed, expected)

    def test_process_files(self):
        observed = get_date_folders(self.SOURCE, self.image_types)
        expected = self.dir_set
        self.assertEqual(observed, expected)

    def test_create_dest_dirs(self):
        create_dest_dirs(self.DEST, self.dir_set, self.image_types)
        for day in self.dir_set:
            for image_type in self.image_types:
                self.assertTrue(Path(os.path.join(self.DEST, day, image_type)).exists())

    def test_write_image_files_to_dest(self):
        create_dest_dirs(self.DEST, self.dir_set, self.image_types)
        write_image_files_to_dest(self.SOURCE, self.DEST, self.dir_set, self.image_types)
        
        for day in self.dir_set:

            if day == '2000-01-01':
                for image_type in self.image_types:
                    if image_type == 'raw':
                        for file in self.raw_files1:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())
                    elif image_type == 'tiff':
                        for file in self.tiff_files1:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())
                    elif image_type == 'developed':
                        for file in self.developed_files1:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())

            if day == '2000-01-02':
                for image_type in self.image_types:
                    if image_type == 'raw':
                        for file in self.raw_files2:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())
                    elif image_type == 'tiff':
                        for file in self.tiff_files2:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())
                    elif image_type == 'developed':
                        for file in self.developed_files2:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())

            if day == '2000-01-03':
                for image_type in self.image_types:
                    if image_type == 'raw':
                        for file in self.raw_files3:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())
                    elif image_type == 'tiff':
                        for file in self.tiff_files3:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())
                    elif image_type == 'developed':
                        for file in self.developed_files3:
                            self.assertTrue(
                                Path(os.path.join(self.DEST, day, image_type, file)).exists())


if __name__ == "__main__":
    # Slightly hackish way to by-pass parsing command line arguments.
    if len(sys.argv) > 1:
        TestDriver.SOURCE = sys.argv.pop()
        TestDriver.DEST = sys.argv.pop()
    unittest.main()
