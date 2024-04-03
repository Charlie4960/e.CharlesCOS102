class SimpleInterestCalculator:
    def __init__(self):
        self.principal = 0
        self.rate = 0
        self.time = 0

    def set_values(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_interest(self):
        interest = (self.principal * self.rate * self.time) / 100
        return interest

# Function to get user input for principal, rate, and time
def get_user_input():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: (%)"))
    time = float(input("Enter time period (in years): "))
    return principal, rate, time

#Example usuage
calculator = SimpleInterestCalculator()

# User input
principal, rate, time = get_user_input()

# Set values
calculator.set_values(principal, rate, time)

#Calculate Interest
interest = calculator.calculate_interest()
print("Simple Interest:", interest)

#I got some help on this code in particular to learn 
# and I'll be happy be defend my work anytime.