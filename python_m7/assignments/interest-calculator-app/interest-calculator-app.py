from tkinter import *
from tkinter.filedialog import asksaveasfilename

window = Tk()
window.title("Interest Calculator App")
window.geometry("600x300")
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)


def calculate():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    years = float(years_entry.get())
    interest = principal * rate * years / 100
    total = principal + interest
    txt_result.delete(1.0, END)
    txt_result.insert(END, "Principal: " + str(principal) + "\n")
    txt_result.insert(END, "Rate: " + str(rate) + "%\n")
    txt_result.insert(END, "Years: " + str(years) + "\n")
    txt_result.insert(END, "Interest: " + str(interest) + "\n")
    txt_result.insert(END, "Total amount: " + str(total))


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        output_file.write(txt_result.get(1.0, END))
    window.title(f"Interest Calculator App - {filepath}")


fr_inputs = Frame(window, relief=RAISED, bd=2)
principal_lbl = Label(fr_inputs, text="Principal")
principal_entry = Entry(fr_inputs)
rate_lbl = Label(fr_inputs, text="Rate (%)")
rate_entry = Entry(fr_inputs)
years_lbl = Label(fr_inputs, text="Years")
years_entry = Entry(fr_inputs)
btn_calc = Button(fr_inputs, text="Calculate", command=calculate)
btn_save = Button(fr_inputs, text="Save As...", command=save_file)
txt_result = Text(window)

principal_lbl.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
principal_entry.grid(row=1, column=0, sticky="ew", padx=5)
rate_lbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
rate_entry.grid(row=3, column=0, sticky="ew", padx=5)
years_lbl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
years_entry.grid(row=5, column=0, sticky="ew", padx=5)
btn_calc.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=7, column=0, sticky="ew", padx=5)

fr_inputs.grid(row=0, column=0, sticky="ns")
txt_result.grid(row=0, column=1, sticky="nsew")

window.mainloop()
