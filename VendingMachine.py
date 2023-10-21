import tkinter as tk
from tkinter import messagebox


class VendingMachine(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vending Machine")
        self.geometry("390x500")

        # Set the background image
        self.background_image = tk.PhotoImage(file="background.png")
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Define the images for the drinks and their corresponding names
        self.drink_info = {
            "coke.png": "Coke",
            "cokezero.png": "Coke Zero",
            "sprite.png": "Sprite",
            "pepsi.png": "Pepsi",
            "drpep.png": "Dr. Pepper",
            "mtndew.png": "Mountain Dew",
            "fanta.png": "Fanta",
            "pwrade.png": "Powerade",
            "dasani.png": "Dasani",
            # Add more images and names as needed
        }

        # Adds images to dictionary
        self.drink_images = {filename: tk.PhotoImage(file=filename) for filename in self.drink_info.keys()}
        # Initialize dispense counts to 10
        self.drink_counts = {filename: 10 for filename in self.drink_info.keys()}

        self.selected_drink = tk.StringVar()
        self.payment_amount = tk.StringVar()
        self.create_buttons()
        self.create_restock_dropdown()
        self.create_restock_button()
        self.create_payment_entry()

    def create_buttons(self):
        # Create a 3x3 grid of buttons
        for row in range(3):
            for col in range(3):
                filename = list(self.drink_info.keys())[row * 3 + col]
                button = tk.Button(self, image=self.drink_images[filename])
                button.grid(row=row, column=col, padx=10, pady=10)
                # Add command to dispense the corresponding drink
                button.config(command=lambda f=filename: self.dispense_drink(f))

    def create_restock_dropdown(self):
        drinks = list(self.drink_info.values())
        self.selected_drink.set(drinks[0])  # Set default value
        restock_dropdown = tk.OptionMenu(self, self.selected_drink, *drinks)
        restock_dropdown.grid(row=3, column=0, padx=10, pady=10)

    def create_restock_button(self):
        restock_button = tk.Button(self, text="Restock", command=self.restock_drink)
        restock_button.grid(row=3, column=1, padx=10, pady=10)

    def create_payment_entry(self):
        payment_label = tk.Label(self, text="Payment:")
        payment_label.grid(row=3, column=2, padx=10, pady=10)
        payment_entry = tk.Entry(self, textvariable=self.payment_amount)
        payment_entry.grid(row=3, column=3, padx=10, pady=10)

    def create_payment_entry(self):
        payment_entry = tk.Entry(self, textvariable=self.payment_amount)
        payment_entry.grid(row=3, column=2, padx=10, pady=10)

    def dispense_drink(self, filename):
        payment_str = self.payment_amount.get()
        try:
            payment = float(payment_str)
            if payment < 1:
                raise ValueError("Insufficient funds. Please enter at least $1.")

            if self.drink_counts[filename] > 0:
                drink_name = self.drink_info[filename]
                self.drink_counts[filename] -= 1
                change = payment - 1
                messagebox.showinfo("Dispense Drink", f"Dispensing {drink_name}. Remaining: {self.drink_counts[filename]}/10. Change: ${change:.2f}")
            else:
                messagebox.showinfo("Out of Stock", "This drink is out of stock. Please restock.")
        except ValueError as error:
            if not payment_str:  # Empty string check
                error = "Please enter payment."
            messagebox.showinfo("Error", str(error))
        finally:
            # Clear the payment entry field
            self.payment_amount.set("")


    def restock_drink(self):
        selected_drink_name = self.selected_drink.get()
        for filename, drink_name in self.drink_info.items():
            if drink_name == selected_drink_name:
                self.drink_counts[filename] = 10
                break
        messagebox.showinfo("Restock", f"{selected_drink_name} has been restocked.")



vending_machine = VendingMachine()
vending_machine.mainloop()