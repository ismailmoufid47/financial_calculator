from calculations.calculations import FutureValueCalculator, PresentValueCalculator, CAGR
from plots.plot import plot_values_over_time
import gui

def prompt():
    interface_choice = input("Do you prefer an Graphical User Interface: (yes/no)? ")

    if interface_choice.lower() == "yes":
        import gui.main_window as interface

        interface.run()

    print(
        "Choose a financial calculation:\n1. Future Value\n2. Present Value\n3. Compound Annual Growth Rate (CAGR)"
    )
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (as a decimal): "))
        time = int(input("Enter the number of years: "))
        future_value_calculator = FutureValueCalculator(principal, rate, time)

        # Ask if the user wants to see the plot
        plot_choice = input("Do you want to see the plot (yes/no)? ").lower()
        if plot_choice == "yes":
            plot_values_over_time(future_value_calculator.plot)
    elif choice == "2":
        future_value = float(input("Enter the future value: "))
        rate = float(input("Enter the discount rate (as a decimal): "))
        time = int(input("Enter the number of years: "))
        present_value_calculator = PresentValueCalculator(future_value, rate, time)

        # Ask if the user wants to see the plot
        plot_choice = input("Do you want to see the plot (yes/no)? ").lower()
        if plot_choice == "yes":
            plot_values_over_time(present_value_calculator.plot)
    elif choice == "3":
        principal = float(input("Enter the initial principal amount: "))
        future_value = float(input("Enter the final value: "))
        time = int(input("Enter the number of years: "))
        cagr_calculator = CAGR(principal, future_value, time)
    else:
        print("Invalid choice. Please choose a valid option.")
        prompt()


if __name__ == "__main__":
    prompt()
