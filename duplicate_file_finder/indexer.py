
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


def get_all_file_paths(root: str) -> typing.List:
    '''Walks the file system starting from `root` and returns a list of all file paths'''
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            results.append(fpath)
    return results


def main():
    paths = get_all_file_paths(TEST_PATH)
    for p in paths:
        print(Record.compute_hash(path=p))


if __name__ == '__main__':
    main()