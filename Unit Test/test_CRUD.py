# -*- coding: utf-8 -*-


import pytest

import sys
sys.path.append("../TeamUp")
from Control import MainControl
from Model import DataBase

class TestCRUD:
    
    def test_read(self):
        data = MainControl.MainControl()
        assert data.read("Student")