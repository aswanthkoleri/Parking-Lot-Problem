# Basic characteristics
# 1. Reg No
# 2. Colour

class Car:
    """docstring for Car"""
    def __init__(self,regNo,colour):
        self._regNo = regNo
        self._colour=colour

    # Now getters
    def regNo(self):
        return self._regNo

    def colour(self):
        return self.colour



