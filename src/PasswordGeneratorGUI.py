# This project uses a GUI to generate password customized based on the needs of the user
# while including input validation and other features


# Libraries/packages used
import tkinter as tk
from tkinter import Frame, messagebox
import string
import random
import secrets
import tkinter.font as tkFont
import pyperclip


class Password_GUI:
    # Constructor
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.set_window_properties()
        self.root.resizable(0, 0)  # Will make the GUI not resizable
        self.set_frame1()
        self.set_frame2()
        self.set_frame3()
        self.set_frame4()
        self.set_frame5()
        self.set_frame6()
        self.set_frame7()
        self.set_frame8()
        self.set_frame9()

    # Starts the GUI
    def start(self) -> None:
        self.root.mainloop()
        
    def set_window_properties(self) -> None:
        self.root.geometry("500x300")
        self.root.title("Password Generator")
        self.root["bg"] = "#334854"  # Background color
        brand_logo=tk.PhotoImage(file="C:\\Users\\haniy\\OneDrive\Pictures\\logobrand.png")
        self.root.iconphoto(True, brand_logo)

    # Frames enable the organization of GUI
    def set_frame1(self) -> None:
        self.frame1 = tk.Frame(self.root)

        self.password_label = tk.Label(
            text="Password Length:", bg="#334854", fg="#f9c535", font=(tkFont.BOLD, 10)
        )
        self.password_label.place(x=9, y=23, anchor=tk.W)

        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack(side=tk.TOP, pady=(15, 0))

    def set_frame2(self) -> None:
        self.frame2 = tk.Frame(self.root)

        self.lower_label = tk.Label(
            text="Lower Alphabet Number:",
            bg="#334854",
            fg="#f9c535",
            font=(tkFont.BOLD, 10),
        )
        self.lower_label.place(x=9, y=51, anchor=tk.W)

        self.lower_entry = tk.Entry(self.root)
        self.lower_entry.pack(pady=(9, 0))

    def set_frame3(self) -> None:
        self.frame3 = tk.Frame(self.root)

        self.upper_label = tk.Label(
            text="Upper Alphabet Number:",
            bg="#334854",
            fg="#f9c535",
            font=(tkFont.BOLD, 10),
        )
        self.upper_label.place(x=9, y=79, anchor=tk.W)

        self.upper_entry = tk.Entry(self.root)
        self.upper_entry.pack(pady=(9, 0))

    def set_frame4(self) -> None:
        self.frame4 = tk.Frame(self.root)

        self.digits_label = tk.Label(
            text="Digits Number:", bg="#334854", fg="#f9c535", font=(tkFont.BOLD, 10)
        )
        self.digits_label.place(x=9, y=107, anchor=tk.W)
        self.digits_entry = tk.Entry(self.root)
        self.digits_entry.pack(pady=(9, 0))

    def set_frame5(self) -> None:
        self.frame5 = tk.Frame(self.root)

        self.symbols_label = tk.Label(
            text="Symbols Number:", bg="#334854", fg="#f9c535", font=(tkFont.BOLD, 10)
        )
        self.symbols_label.place(x=9, y=135, anchor=tk.W)

        self.symbols_entry = tk.Entry(self.root)
        self.symbols_entry.pack(pady=(9, 0))

    def set_frame6(self) -> None:
        self.set_frame6 = tk.Frame(self.root)

        self.generate_label = tk.Label(
            text="Generated Password:",
            bg="#334854",
            fg="#f9c535",
            font=(tkFont.BOLD, 10),
        )
        self.generate_label.place(x=9, y=180, anchor=tk.W)

        self.generated_entry = tk.Entry(self.root)
        self.generated_entry.pack(pady=(25, 0))

    def set_frame7(self) -> None:
        self.frame7 = tk.Frame(self.root)
        self.password_button = tk.Button(
            self.root,
            text="Generate Password",
            font=("Arial", 10),
            bg="#e04462",
            fg="white",
            command=self.generate,  # Calls the generate method once the button is clicked
        )
        self.password_button.pack(pady=(7, 0))

    def set_frame8(self) -> None:
        self.frame8 = tk.Frame(self.root)
        self.copy_button = tk.Button(
            self.root,
            text="Copy Password",
            font=("Arial", 10),
            bg="#e04462",
            fg="white",
            command=self.copy,  # Calls the copy method once the button is clicked
        )
        self.copy_button.pack(pady=(7, 0))

    def set_frame9(self) -> None:
        self.frame9 = tk.Frame(self.root)
        self.reset_button = tk.Button(
            self.root,
            text="Reset",
            font=("Arial", 10),
            bg="#e04462",
            fg="white",
            command=self.reset,  # Calls the copy method once the button is clicked
        )
        self.reset_button.pack(pady=(7, 0))

    def generate(self) -> str:
        self.generated_entry.delete(0, "end")  # Resets the generated password entry
        self.password_length = self.password_entry.get()

        # Input validation
        try:
            self.password_length = int(self.password_length)
        except ValueError:
            tk.messagebox.showerror(
                title="Value Error", message="The password length must be an integer"
            )
            return

        self.upper_alphabet = self.upper_entry.get()

        try:
            self.upper_alphabet = int(self.upper_alphabet)
        except ValueError:
            tk.messagebox.showerror(
                title="Value Error",
                message="The upper alphabet number must be an integer",
            )
            return

        self.lower_alphabet = self.lower_entry.get()
        try:
            self.lower_alphabet = int(self.lower_alphabet)
        except ValueError:
            tk.messagebox.showerror(
                title="Value Error",
                message="The lower alphabet number must be an integer",
            )
            return

        self.symbols_number = self.symbols_entry.get()
        try:
            self.symbols_number = int(self.symbols_number)
        except ValueError:
            tk.messagebox.showerror(
                title="Value Error", message="The symbols number must be an integer"
            )
            return

        self.digits_number = self.digits_entry.get()
        try:
            self.digits_number = int(self.digits_number)
        except ValueError:
            tk.messagebox.showerror(
                title="Value Error", message="The digits number must be an integer"
            )
            return

        self.characters_total = (
            self.upper_alphabet
            + self.lower_alphabet
            + self.symbols_number
            + self.digits_number
        )

        # Input Validation
        if self.characters_total > self.password_length:
            tk.messagebox.showerror(
                title="Value Discrepancy",
                message="The characters total must equal the password length",
            )
            return

        self.password = []

        for _ in range(self.symbols_number):
            self.password.append(secrets.choice(string.punctuation))

        for _ in range(self.lower_alphabet):
            self.password.append(secrets.choice(string.ascii_lowercase))

        for _ in range(self.upper_alphabet):
            self.password.append(secrets.choice(string.ascii_uppercase))

        for _ in range(self.digits_number):
            self.password.append(secrets.choice(string.digits))

        # Input validation
        if self.characters_total < self.password_length:
            tk.messagebox.showerror(
                title="Value Discrepancy",
                message="The characters total must equal the password length",
            )
            return

        # Shuffling enhances the security of the password
        random.shuffle(self.password)

        # Converting the password to a string
        self.password = "".join([str(s) for s in self.password])

        # Displaying the password in the entry box
        self.generated_entry.insert(0, self.password)

    # Method to copy the password
    def copy(self) -> str:
        pyperclip.copy(self.generated_entry.get())

    # Method to reset the entry boxes
    def reset(self) -> None:
        self.password_entry.delete(0, "end")
        self.upper_entry.delete(0, "end")
        self.lower_entry.delete(0, "end")
        self.symbols_entry.delete(0, "end")
        self.digits_entry.delete(0, "end")
        self.generated_entry.delete(0, "end")


def main():
    app = Password_GUI()
    app.start()


if __name__ == "__main__":
    main()
