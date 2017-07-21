#! /usr/bin/env python3
from enum import Enum

class Rank(Enum):
    RESPONDENT = 0
    MANAGER = 1
    DIRECTOR = 2

    value = None #assigns value to rank instance

    def __init__(self, v):
        self.value = v

    def getValue(self):
        return self.value
