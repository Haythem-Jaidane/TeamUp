# -*- coding: utf-8 -*-


import pytest

import sys
sys.path.append("../TeamUp")
from Controller import MainControl
from Model import DataBase

class TestCRUD:
    
    def test_read(self):
        data = MainControl.MainControl()
        assert data.read("Student")