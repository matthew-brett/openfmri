""" Testing utils module
"""
from __future__ import absolute_import

from ..utils import open4csv

from nose.tools import (assert_true, assert_false, assert_raises,
                        assert_equal, assert_not_equal)

from ..tmpdirs import InTemporaryDirectory


def test_open4csv():
    # Test opening of csv files
    import csv
    contents = [['oh', 'my', 'G'],
                ['L', 'O', 'L'],
                ['when', 'cleaning', 'windas']]
    with InTemporaryDirectory():
        with open4csv('my.csv', 'w') as fobj:
            writer = csv.writer(fobj)
            writer.writerows(contents)
        with open4csv('my.csv', 'r') as fobj:
            dialect = csv.Sniffer().sniff(fobj.read())
            fobj.seek(0)
            reader = csv.reader(fobj, dialect)
            back = list(reader)
    assert_equal(contents, back)
    assert_raises(ValueError, open4csv, 'my.csv', 'rb')
    assert_raises(ValueError, open4csv, 'my.csv', 'wt')
