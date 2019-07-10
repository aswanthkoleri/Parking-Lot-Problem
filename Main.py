import Parking

class Processing:
    def __init__(self):
        self.parking = Parking.Parking()

    def processKeyboardInput(self):
        try:
            while True:
                Input = input("Enter the command : ")
                self.process_command(Input)
        except (KeyboardInterrupt,SystemExit):
            return
        except Exception as ex:
            print(ex)

    def process_command(self,Input):
        Inputs = Input.split()
        command = Inputs[0]
        params = Inputs[1:]
        if hasattr(self.parking, command):
            # print("Working ")
            command_function = getattr(self.parking,command)
            command_function(*params)
        else:
            print("Wrong Command")
        return

if __name__ == '__main__':
    print("Welcome to Parking Lot")
    p = Processing()
    p.processKeyboardInput()
