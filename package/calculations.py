import matplotlib.pyplot as plt

class FutureValueCalculator:
    def __init__(self, principal, rate, time):
        try:
            self.principal = float(principal)
            self.rate = float(rate)
            self.time = int(time)
        except (TypeError, ValueError):
            raise ValueError("Principal, rate, and time must be numeric values.")

        if self.principal <= 0 or self.rate <= 0 or self.time <= 0:
            raise ValueError("Principal, rate, and time must be positive values.")

        self.values_over_time = self.calculate_values_over_time()
        self.balance = self.values_over_time[-1][-1]
        print(f"Compound interest calculation done for Principal: ${self.principal:.2f}, Rate: {self.rate*100:.2f}%, Time: {self.time} years\nFinal Balance: ${self.balance:.2f}")

    def calculate_values_over_time(self):
        values_over_time = []
        for t in range(1, self.time + 1):
            amount = self.principal * (1 + self.rate) ** t
            values_over_time.append((t, amount))
        return values_over_time

    def plot(self):
        times, amounts = zip(*self.values_over_time)
        
        plt.plot(times, amounts, label='Compound Interest')
        plt.xlabel('Time (years)')
        plt.ylabel('Amount')
        plt.title('Compound Interest Growth Over Time')
        plt.text(times[-1], self.balance, f'Final Balance: {self.balance}', fontsize=12, ha='right')
        plt.legend()
        plt.show()

class PresentValueCalculator:
    def __init__(self, future_value, rate, time):
        try:
            self.future_value = float(future_value)
            self.rate = float(rate)
            self.time = int(time)
        except (TypeError, ValueError):
            raise ValueError("Future value, rate, and time must be numeric values.")

        if self.future_value <= 0 or self.rate <= 0 or self.time <= 0:
            raise ValueError("Future value, rate, and time must be positive values.")

        self.values_over_time = self.calculate_values_over_time()
        self.present_value = self.values_over_time[-1][-1]
        print(f"Present value calculation done for Future Value: ${self.future_value:.2f}, Rate: {self.rate*100:.2f}%, Time: {self.time} years\nPresent Value: ${self.present_value:.2f}")

    def calculate_values_over_time(self):
        values_over_time = []
        for t in range(self.time-1, -1, -1):
            present_value = self.future_value / ((1 + self.rate) ** (self.time-t))
            values_over_time.append((t+1, present_value))
        return values_over_time

    def plot(self):
        times, values = zip(*self.values_over_time)
        
        plt.plot(times, values, label='Present Value')
        plt.xlabel('Time (years)')
        plt.ylabel('Value')
        plt.title('Present Value Over Time')
        plt.text(times[-1], self.present_value, f'Present Value: {self.present_value:.2f}', fontsize=12, ha='right')
        plt.legend()
        plt.show()

class CAGR:
    def __init__(self, principal, future_value, time):
        try:
            self.principal = float(principal)
            self.future_value = float(future_value)
            self.time = int(time)
        except (TypeError, ValueError):
            raise ValueError("Principal, future value, and time must be numeric values.")

        if self.principal <= 0 or self.future_value <= 0 or self.time <= 0:
            raise ValueError("Principal, future value, and time must be positive values.")

        self.rate = ((self.future_value / self.principal) ** (1 / self.time)) - 1
        print(f"Compound Annual Growth Rate calculation done for Principal: ${self.principal:.2f}, Future Value: ${self.future_value:.2f}, Time: {self.time} years\nCompound Annual Growth Rate: {self.rate * 100:.2f}%")
def prompt():
    interface_choice = input("Do you prefer an Graphical User Interface: (yes/no)? ")

    if interface_choice.lower() == "yes":
        import gui.main_window as interface
        interface.run()

    print("Choose a financial calculation:\n1. Future Value\n2. Present Value\n3. Compound Annual Growth Rate (CAGR)")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (as a decimal): "))
        time = int(input("Enter the number of years: "))
        future_value_calculator = FutureValueCalculator(principal, rate, time)

        # Ask if the user wants to see the plot
        plot_choice = input("Do you want to see the plot (yes/no)? ").lower()
        if plot_choice == "yes":
            future_value_calculator.plot()
    elif choice == "2":
        future_value = float(input("Enter the future value: "))
        rate = float(input("Enter the discount rate (as a decimal): "))
        time = int(input("Enter the number of years: "))
        present_value_calculator = PresentValueCalculator(future_value, rate, time)

        # Ask if the user wants to see the plot
        plot_choice = input("Do you want to see the plot (yes/no)? ").lower()
        if plot_choice == "yes":
            present_value_calculator.plot()
    elif choice == "3":
        principal = float(input("Enter the initial principal amount: "))
        future_value = float(input("Enter the final value: "))
        time = int(input("Enter the number of years: "))
        cagr_calculator = CAGR(principal, future_value, time)    
    else:
        print("Invalid choice. Please choose a valid option.")
        prompt()
if __name__ == '__main__':

    prompt()
