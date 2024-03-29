"""

"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

while state_code != "":
    if state_code.upper() in CODE_TO_NAME:
        print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

