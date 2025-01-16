"""Check if Year is a Leap year
Write a program that check if entered year is a leap Year and if it is a leap year display it. And if it is not a leap Year then display it accordingly
Rules to determine if Year is a leap year
1.
"""
"""year = 2020
checker = year/4
if year in checker:
    leap_checker = year/4
    print(f"Year {year} + is a Leap Year")
else:
    print(f"Year {year} + is not a Lear Year")"""
#Create a function for defining rules that determine if Year is a Leap Year
#import tkinter as tk
def check_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
def main():
    entered_year = int(input("Please enter Year: "))
    if check_leap_year(entered_year):
        print(f"{entered_year}" + " is a Leap Year")
    else:
        print(f"{entered_year}" + " is not a Leap Year")
#    result_label.config(text=entered_year)

#root = tk.Tk()
#root.title("Leap Year Checker")

#tk.Label(root, text="Enter a year:").pack()
#year_entry = tk.Entry(root)
#year_entry.pack()

#check_button = tk.Button(root, text="Check", command=lambda: check_leap_year(year_entry.get()))
#check_button.pack()

#result_label = tk.Label(root, text="")
#result_label.pack()

#root.mainloop()

if __name__ == "__main__":
    main()