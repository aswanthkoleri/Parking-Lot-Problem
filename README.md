# Parking Lot Problem

## Table of Contents
+ [About](#about)
+ [Problem Statement](#problem)
+ [Getting Started](#getting_started)
+ [Usage](#usage)
+ [Contribution](#contribution)


## About <a name = "about"></a>

This is python Object Oriented Implementation for the famous Parking Lot Problem.

## Problem Statement <a name = "problem"></a>

```

I own a multi-storey parking lot that can hold up to 'n' cars at any given point in time.
Each slot is given a number starting at 1 increasing with increasing distance from the
entry point in steps of one. I want to create an automated ticketing system that
allows my customers to use my parking lot without human intervention.
When a car enters my parking lot, I want to have a ticket issued to the driver. The
ticket issuing process includes us documenting the registration number (number
plate) and the colour of the car and allocating an available parking slot to the car
before actually handing over a ticket to the driver (we assume that our customers are
nice enough to always park in the slots allocated to them). The customer should be
allocated a parking slot which is nearest to the entry. At the exit the customer returns
the ticket which then marks the slot they were using as being available.
Due to government regulation, the system should provide me with the ability to find
out:

- Registration numbers of all cars of a particular colour.

- Slot number in which a car with a given registration number is parked.

- Slot numbers of all slots where a car of a particular colour is parked.


We interact with the system via a simple set of commands which produce a specific
output. Please take a look at the example below, which includes all the commands
you need to support - they're self explanatory. The system should allow input in two
ways. Just to clarify, the same codebase should support both modes of input - we
don't want two distinct submissions.
1) It should provide us with an interactive command prompt based shell where
commands can be typed in
2) It should accept a filename as a parameter at the command prompt and read the
commands from that file


```


## Getting Started <a name = "getting_started"></a>

The python version used is : Python 3

- Clone the repo
- Run the Main.py
- You will be able to input command after that

### Commands

- `create_parking_lot <no_of_slots>`
- `park <reg_no> <colour>`
- `leave <slot_no>`
- `status`
- `registration_numbers_for_cars_with_colour <colour>`
- `slot_numbers_for_cars_with_colour <colour>`
- `slot_number_for_registration_number <reg_no>`

### Example Commands

```
create_parking_lot 6
park KA-01-HH-1234 White
park KA-01-HH-9999 White
park KA-01-BB-0001 Black
park KA-01-HH-7777 Red
park KA-01-HH-2701 Blue
park KA-01-HH-3141 Black
leave 4
status
park KA-01-P-333 White
park DL-12-AA-9999 White
registration_numbers_for_cars_with_colour White
slot_numbers_for_cars_with_colour White
slot_number_for_registration_number KA-01-HH-3141
slot_number_for_registration_number MH-04-AY-1111

```


### Prerequisites

You need to know about Object Oriented Programming in Python. I prefer you learn from [here](https://realpython.com/python3-object-oriented-programming/)


## Usage <a name = "usage"></a>

You just need to type the commands as mentioned above. Simple!

## Contributions <a name = "contribution"></a>

Contributions are welcome if it improves the program.

