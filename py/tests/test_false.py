from __future__ import absolute_import
from erlpack import pack


def test_false():
    assert pack(False) == '\x83s\x05false'
