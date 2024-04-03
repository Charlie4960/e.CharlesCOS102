class AnnuityPlanCalculator:
    def __init__(self):
        self.principal = 0
        self.rate = 0
        self.time = 0
        self.nperiod = 0
    

    def set_values(self, principal, rate, time, nperiod):
        self.principal = principal
        self.rate = rate
        self.time = time
        self.nperiod = nperiod

    def calculate_interest(self):
        interest = (self.principal*((1+self.rate/self.nperiod) ** (self.nperiod * self.time))-1)/(self.rate/self.nperiod)
        return interest

# Function to get input for principal, rate, time, and nperiod
def get_user_input():
    principal = float(input("Enter Period Cash Payment: "))
    rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter number of times period elapsed: "))
    nperiod = float(input("Enter number of times interest was applied: "))

    return principal, rate, time, nperiod

# Usage
calculator = AnnuityPlanCalculator()

# User input
principal, rate, time, nperiod = get_user_input()

# Set values
calculator.set_values(principal, rate, time, nperiod)

# Calculate Interest
interest = calculator.calculate_interest()
print("Annuity Calculator:", interest)
