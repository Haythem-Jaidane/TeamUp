# -*- coding: utf-8 -*-

import pytest

import sys
sys.path.append("../TeamUp")
from Model import DataBase


class TestDatabase:
    
    def test_connection(self):
        assert DataBase.DataBase().connectMySQL()
        

