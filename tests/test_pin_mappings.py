#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`OPi.pin_mappings` module.
"""

from OPi.pin_mappings import raw, board, sunxi, custom, set_custom_pin_mappings


def test_mappings():
    assert raw(12) == board(3) == sunxi("PA12") == 12
    assert raw(11) == board(5) == sunxi("PA11") == 11
    assert raw(6) == board(7) == sunxi("PA06") == 6
    assert raw(1) == board(11) == sunxi("PA01") == 1
    assert raw(0) == board(13) == sunxi("PA00") == 0
    assert raw(3) == board(15) == sunxi("PA03") == 3
    assert raw(15) == board(19) == sunxi("PA15") == 15
    assert raw(16) == board(21) == sunxi("PA16") == 16
    assert raw(14) == board(23) == sunxi("PA14") == 14
    assert raw(198) == board(8) == sunxi("PG06") == 198
    assert raw(199) == board(10) == sunxi("PG07") == 199
    assert raw(7) == board(12) == sunxi("PA07") == 7
    assert raw(19) == board(16) == sunxi("PA19") == 19
    assert raw(18) == board(18) == sunxi("PA18") == 18
    assert raw(2) == board(22) == sunxi("PA02") == 2
    assert raw(13) == board(24) == sunxi("PA13") == 13
    assert raw(10) == board(26) == sunxi("PA10") == 10


def test_custom_dict():
    set_custom_pin_mappings({1: 2, 2: 3, 3: 4})
    assert custom(1) == 2
    assert custom(2) == 3
    assert custom(3) == 4


def test_custom_object():

    class mapper(object):
        def __getitem__(self, value):
            return value + 4

    set_custom_pin_mappings(mapper())
    assert custom(1) == 5
    assert custom(2) == 6
    assert custom(3) == 7
