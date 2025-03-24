# mobile_phone.py

# Define a class representing a mobile phone
class MobilePhone:
    # Initialize the phone with a number
    def __init__(self, number):
        self.number = number
    
    # Simulate turning on the phone
    def turn_on(self):
        print(f'Mobile phone {self.number} is turned on.')

    # Simulate turning off the phone
    def turn_off(self):
        print(f'Mobile phone is turned off.')

    # Simulate making a call to another number
    def call(self, number):
        print(f'Calling {number}')

# Create two instances of MobilePhone with different numbers
num_1, num_2 = MobilePhone('867-5309'), MobilePhone('111-1111')

# Turn on both phones
num_1.turn_on()
num_2.turn_on()

# Make calls between the two phones
num_1.call(num_2.number) # num_1 calls num_2
num_2.call(num_1.number) # num_2 calls num_1

# Turn off both phones
num_1.turn_off()
num_2.turn_off()