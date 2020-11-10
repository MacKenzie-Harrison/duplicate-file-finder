
# 1. crawl the file system and get a list of all of the file paths on the drive
# 2. compute hashes and gather metadata for each file, including size, modified date, and created date
# Our confidence is that it is unlikely that two files with the same hash, name, length, create date,
# modified date are in truth different files
# 3. dump all of that information into a csv
# example code https://stackoverflow.com/questions/8505457/how-to-crawl-folders-to-index-files

import os
import hashlib
import dataclasses as dcs
import datetime as dt
import typing


TEST_PATH = 'S:\\Library\\Pictures'


@dcs.dataclass
class Record:
    path: str
    md5hash: str
    size: int
    created: dt.datetime
    modified: dt.datetime

    def to_csv_format(self) -> str:
        '''Returns a string in the format of `path,md5hash,size,created,modified`'''
        return f'{self.path},{self.md5hash},{self.size},{self.created},{self.modified}'

    @staticmethod
    def compute_hash(path):
        '''Returns the MD5 hex digest for the contents of a file located at `path`'''
        f = open(path, 'rb')
        x = hashlib.md5(f.read()).hexdigest()
        f.close()
        return x

def gather_metadata(index_path: str, metadata_path: str):
    '''Reads the index at `index_path` and gathers metadata for every file listed which is then written to a text file at `metadata_path`'''
    pass


def build_index(index_file_name: str, root_path: str):
    '''Walks the file system starting from `root_path` and generates a list of file paths which are then written to a text file at `index_file_name`'''
    index_file = open(index_file_name, 'w')
    for dirpath, dirnames, filenames in os.walk(root_path):
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            index_file.write(fpath + '\n')
    index_file.close()


def main():
    now = dt.datetime.now().strftime('%Y-%m-%d-%H-%M')
    index_file_name = now + '-index-file.txt'
    build_index(index_file_name=index_file_name, root_path=TEST_PATH)


if __name__ == '__main__':
    main()
