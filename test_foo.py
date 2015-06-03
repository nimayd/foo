#! usr/bin/env python

import pytest

import foo

import sys

# def test_parse():
    

def test_makelines():
    assert foo.makelines((5 - 2, 5 - 2, 3 * ' ')) == (3, 3, 3, '   +---+', '   |   |')
    assert foo.makelines((1 - 2, 1 - 2, '')) == (-1, -1, 0, '+', '|')
    assert foo.makelines((6 - 2, 4 - 2, '')) == (4, 2, 0, '+----+', '|    |')

@pytest.mark.parametrize(("test_file", "nums"), [
  # ("1x1x1.out", foo.create, (-1, -1, len(' '), ' +', ' |')) 
  ("1x1x1.out", (-1, -1, len(' '), ' +', ' |')),
  ("5x1x3.out", (3, -1, len('   '), '   +---+', '   |   |')),
  ("1x5x2.out", (-1, 3, len('  '), '  +', '  |'))
    ])

def test_create(capfd, test_file, nums):
    foo.create(nums)
    resout, reserr = capfd.readouterr()
    expected = open(r'expected_output/test_file', 'r').read()
    assert resout == expected

