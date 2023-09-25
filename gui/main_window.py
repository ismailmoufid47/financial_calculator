import tkinter as tk
from tkinter import ttk
import package.calculations as calc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FinancialCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Calculator")
        
        # Calculate the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set the width and height for the main application window
        window_width = 400
        window_height = 300
        
        # Calculate the x and y coordinates to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # Center the window on the screen
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Create a notebook with tabs for different calculations
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)  # Add padding
        
        # Create tabs for Future Value, Present Value, and CAGR calculations
        self.future_value_tab = ttk.Frame(self.notebook)
        self.present_value_tab = ttk.Frame(self.notebook)
        self.cagr_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.future_value_tab, text='Future Value')
        self.notebook.add(self.present_value_tab, text='Present Value')
        self.notebook.add(self.cagr_tab, text='CAGR')
        
        # Create widgets for each tab
        self.create_future_value_tab()
        self.create_present_value_tab()
        self.create_cagr_tab()
    
    def create_future_value_tab(self):
        # Widgets for the Future Value tab
        ttk.Label(self.future_value_tab, text="Principal:").grid(row=0, column=0, sticky='w')
        self.future_value_principal_entry = ttk.Entry(self.future_value_tab)
        self.future_value_principal_entry.grid(row=0, column=1)
        
        ttk.Label(self.future_value_tab, text="Annual Interest Rate (%):").grid(row=1, column=0, sticky='w')
        self.future_value_rate_entry = ttk.Entry(self.future_value_tab)
        self.future_value_rate_entry.grid(row=1, column=1)
        
        ttk.Label(self.future_value_tab, text="Time (years):").grid(row=2, column=0, sticky='w')
        self.future_value_time_entry = ttk.Entry(self.future_value_tab)
        self.future_value_time_entry.grid(row=2, column=1)
        
        ttk.Button(self.future_value_tab, text="Calculate", command=self.calculate_future_value).grid(row=3, column=0, columnspan=2)
        
        self.future_value_result_label = ttk.Label(self.future_value_tab, text="")
        self.future_value_result_label.grid(row=4, column=0, columnspan=2)
    
    def calculate_future_value(self):
        principal = float(self.future_value_principal_entry.get())
        rate = float(self.future_value_rate_entry.get()) / 100  # Convert percentage to decimal
        time = int(self.future_value_time_entry.get())
        
        future_value_calculator = calc.FutureValueCalculator(principal, rate, time)
        result = future_value_calculator.balance
        
        self.future_value_result_label.config(text=f"Future Value: ${result:.2f}")
        
        # Visualize the result
        future_value_calculator.plot()
    
    def create_present_value_tab(self):
        # Widgets for the Present Value tab
        ttk.Label(self.present_value_tab, text="Future Value:").grid(row=0, column=0, sticky='w')
        self.present_value_future_value_entry = ttk.Entry(self.present_value_tab)
        self.present_value_future_value_entry.grid(row=0, column=1)
        
        ttk.Label(self.present_value_tab, text="Discount Rate (%):").grid(row=1, column=0, sticky='w')
        self.present_value_rate_entry = ttk.Entry(self.present_value_tab)
        self.present_value_rate_entry.grid(row=1, column=1)
        
        ttk.Label(self.present_value_tab, text="Time (years):").grid(row=2, column=0, sticky='w')
        self.present_value_time_entry = ttk.Entry(self.present_value_tab)
        self.present_value_time_entry.grid(row=2, column=1)
        
        ttk.Button(self.present_value_tab, text="Calculate", command=self.calculate_present_value).grid(row=3, column=0, columnspan=2)
        
        self.present_value_result_label = ttk.Label(self.present_value_tab, text="")
        self.present_value_result_label.grid(row=4, column=0, columnspan=2)
    
    def calculate_present_value(self):
        future_value = float(self.present_value_future_value_entry.get())
        rate = float(self.present_value_rate_entry.get()) / 100  # Convert percentage to decimal
        time = int(self.present_value_time_entry.get())
        
        present_value_calculator = calc.PresentValueCalculator(future_value, rate, time)
        result = present_value_calculator.present_value
        
        self.present_value_result_label.config(text=f"Present Value: ${result:.2f}")
        
        # Visualize the result
        present_value_calculator.plot()
    
    def create_cagr_tab(self):
        # Widgets for the CAGR tab
        ttk.Label(self.cagr_tab, text="Initial Principal:").grid(row=0, column=0, sticky='w')
        self.cagr_principal_entry = ttk.Entry(self.cagr_tab)
        self.cagr_principal_entry.grid(row=0, column=1)
        
        ttk.Label(self.cagr_tab, text="Final Value:").grid(row=1, column=0, sticky='w')
        self.cagr_future_value_entry = ttk.Entry(self.cagr_tab)
        self.cagr_future_value_entry.grid(row=1, column=1)
        
        ttk.Label(self.cagr_tab, text="Time (years):").grid(row=2, column=0, sticky='w')
        self.cagr_time_entry = ttk.Entry(self.cagr_tab)
        self.cagr_time_entry.grid(row=2, column=1)
        
        ttk.Button(self.cagr_tab, text="Calculate", command=self.calculate_cagr).grid(row=3, column=0, columnspan=2)
        
        self.cagr_result_label = ttk.Label(self.cagr_tab, text="")
        self.cagr_result_label.grid(row=4, column=0, columnspan=2)
    
    def calculate_cagr(self):
        principal = float(self.cagr_principal_entry.get())
        future_value = float(self.cagr_future_value_entry.get())
        time = int(self.cagr_time_entry.get())
        
        cagr_calculator = calc.CAGR(principal, future_value, time)
        result = cagr_calculator.rate
        
        self.cagr_result_label.config(text=f"CAGR: {result*100:.2f}%")
        
        # Visualize the result
        # Add visualization code here if needed.

def run():
    root = tk.Tk()
    app = FinancialCalculatorApp(root)
    root.mainloop()
if __name__ == '__main__':
    run()
