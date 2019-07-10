# Parking Slot
# 1. Slot Number
# 2. Car in Slot
# 3. Available or Not

class ParkingSlot:
    """docstring for ParkingSlot"""
    def __init__(self,slotNo,available):
        self._car = None
        self._slotNo = slotNo
        self._available = available

    # Getters and setters
    def car(self):
        return self._car

    def car(self,car):
        self._car = car
        self._available = False

    def freeSlot(self):
        self._car = None
        self._available = True

    def isFree(self):
        return self._available

    def slotNo(self):
        return self._slotNo

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self,value):
        self._available = value

