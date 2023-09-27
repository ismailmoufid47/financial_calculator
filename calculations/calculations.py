class FutureValueCalculator:
    def __init__(self, principal, rate, time):
        try:
            self.principal = float(principal)
            self.rate = float(rate)
            self.time = int(time)
        except:
            raise ValueError("Principal, rate, and time must be numeric values.")

        if self.principal <= 0 or self.rate <= 0 or self.time <= 0:
            raise ValueError("Principal, rate, and time must be positive values.")

        self.values_over_time = self.calculate_values_over_time()
        self.balance = self.values_over_time[-1][-1]
        print(
            f"Compound interest calculation done for Principal: ${self.principal:.2f}, Rate: {self.rate*100:.2f}%, Time: {self.time} years\nFinal Balance: ${self.balance:.2f}"
        )
        times, amounts = zip(*self.values_over_time)
        self.plot = (
            times,
            amounts,
            "Compound Interest",
            "Time (years)",
            "Amount",
            "Compound Interest Growth Over Time",
            times[-1],
            self.balance,
            f"Final Balance: {self.balance}",
        )

    def calculate_values_over_time(self):
        values_over_time = []
        for t in range(1, self.time + 1):
            amount = self.principal * (1 + self.rate) ** t
            values_over_time.append((t, amount))
        return values_over_time


class PresentValueCalculator:
    def __init__(self, future_value, rate, time):
        try:
            self.future_value = float(future_value)
            self.rate = float(rate)
            self.time = int(time)
        except:
            raise ValueError("Future value, rate, and time must be numeric values.")

        if self.future_value <= 0 or self.rate <= 0 or self.time <= 0:
            raise ValueError("Future value, rate, and time must be positive values.")

        self.values_over_time = self.calculate_values_over_time()
        self.present_value = self.values_over_time[-1][-1]
        print(
            f"Present value calculation done for Future Value: ${self.future_value:.2f}, Rate: {self.rate*100:.2f}%, Time: {self.time} years\nPresent Value: ${self.present_value:.2f}"
        )
        times, values = zip(*self.values_over_time)
        self.plot = (
            times,
            values,
            "Present Value",
            "Time (years)",
            "Value",
            "Present Value Over Time",
            times[-1],
            self.present_value,
            f"Present Value: {self.present_value:.2f}",
        )

    def calculate_values_over_time(self):
        values_over_time = []
        for t in range(self.time - 1, -1, -1):
            present_value = self.future_value / ((1 + self.rate) ** (self.time - t))
            values_over_time.append((t + 1, present_value))
        return values_over_time


class CAGR:
    def __init__(self, principal, future_value, time):
        try:
            self.principal = float(principal)
            self.future_value = float(future_value)
            self.time = int(time)
        except:
            raise ValueError(
                "Principal, future value, and time must be numeric values."
            )

        if self.principal <= 0 or self.future_value <= 0 or self.time <= 0:
            raise ValueError(
                "Principal, future value, and time must be positive values."
            )

        self.rate = ((self.future_value / self.principal) ** (1 / self.time)) - 1
        print(
            f"Compound Annual Growth Rate calculation done for Principal: ${self.principal:.2f}, Future Value: ${self.future_value:.2f}, Time: {self.time} years\nCompound Annual Growth Rate: {self.rate * 100:.2f}%"
        )
