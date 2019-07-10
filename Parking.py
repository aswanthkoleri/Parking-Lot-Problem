# Parking
# Have to store slots
# Basic functions (According to the question)
# Todo
# 1. Create slots
# 2. Assign the nearest Slot to the Car
# 3. Remove cars from slots
# 4. Show the status of the slots
# 5. Show registration no of cars with a particular colour
# 6. Show slot No of cars with a particular Colour
# 7. Show slot no for a registration number
from ParkingSlot import ParkingSlot
from Car import Car
class Parking:


    def __init__(self):
        self._slots = {}
        self._no_of_slots = 0
    # Create slots
    def create_parking_lot(self,no_of_slots):
        self._no_of_slots=int(no_of_slots)
        if len(self._slots) > 0:
            print("Slots are already created")
            return
        if self._no_of_slots > 0:
            for i in range(self._no_of_slots):
                self._slots[i] = ParkingSlot(i,True)
            print("{} slots are created!".format(self._no_of_slots))
        else:
            print("There is an error in the entered slot number")

    # Assign the nearest slot to the car
    def getNearestFreeSlot(self):
        freeSlot=None
        for i in range(self._no_of_slots):
            # If the slot is free then return the slot_no

            if self._slots[i].available:
                freeSlot = i
                break
        return freeSlot

    def park(self, regNo, colour):
        # For this we need to get the nearest free slot
        car = Car(regNo,colour)
        if not self._primaryCheck():
            return
        nearestSlot = self.getNearestFreeSlot()
        # print(nearestSlot)
        if nearestSlot!=None:
            # Assign
            self._slots[nearestSlot].car(car)
            print("Allotted Slot no : {}".format(nearestSlot))
        else:
            # Slots are full
            print("Slots are full")
            return
# Leave a spot
    def leave(self,slotNo):
        if not self._primaryCheck():
            return
        slotNo = int(slotNo)
        if slotNo >= self._no_of_slots:
            print("The slot does not exist")
        else:
            if not self._slots[slotNo].isFree():
                self._slots[slotNo].freeSlot()
                print("The slot No {} is free ".format(slotNo))
            else:
                print("The slot is already free")
        return

    def status(self):
        if not self._primaryCheck():
            return
        print("Slot No","Registration No","Colour")
        # print(self._slots)
        for slot in self._slots.values():
            # print(slot.available)
            if not slot.available:
                print(slot._slotNo,slot._car._regNo,slot._car._colour)
        return

    def registration_numbers_for_cars_with_colour(self,colour):
        if not self._primaryCheck():
            return
        cars = list(filter(lambda x: x._car._colour == colour,self._slots.values()))
        # print(cars)
    #     Got the list of slots having cars colour white
    # Now display the registration number
        if len(cars)==0:
            print("There are No cars of this colour")
        else:
            for item in cars:
                print(item._car._regNo,end=", ")
        return

    def slot_numbers_for_cars_with_colour(self,colour):
        if not self._primaryCheck():
            return
        slots = list(filter(lambda x: x._car._colour == colour,self._slots.values()))
        # print(slots)
    #     Got the list of slots having cars colour white
    # Now display the registration number
        if len(slots)==0:
            print("There are No slots of this colour")
        else:
            for item in slots:
                print(item.slotNo(),end=", ")
        return

    def slot_number_for_registration_number(self,regNo):
    #     First search for the register number in the slots
        if not self._primaryCheck():
            return
        slotNo=None
        for slot in self._slots.values():
            if not slot.available and slot._car._regNo == regNo:
                slotNo = slot.slotNo()
        if slotNo:
            print("The slot No for the car with register no {} is {}".format(regNo,slotNo))
        else:
            print("No slots have that car")

    def _primaryCheck(self):
        if len(self._slots)==0:
            print("Slots are not created yet")
            return False
        return True


