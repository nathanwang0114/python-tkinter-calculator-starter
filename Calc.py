from tkinter import *

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry('315x510')
        self.master.configure(background='grey')

        self.logic = CalculatorLogic()

        self._input = StringVar()

        self.create_widgets()

    def create_widgets(self):
        label = Label(self.master, font=('ariel', 20, 'bold'), text='Calculator', bg='grey', fg='black')
        label.grid(columnspan=4)

        self.display = Entry(self.master, font=('ariel', 20, 'bold'), textvariable=self._input, insertwidth=7, bd=5, bg="black", justify='right')
        self.display.grid(columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        # Row 1
        b7 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="grey", command=lambda: self.btn_click(7))
        b7.grid(row=2, column=0)

        b8 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="grey", command=lambda: self.btn_click(8))
        b8.grid(row=2, column=1)

        b9 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="grey", command=lambda: self.btn_click(9))
        b9.grid(row=2, column=2)

        Add = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+", bg="grey", command=lambda: self.btn_click("+"))
        Add.grid(row=2, column=3)

        # Row 2
        b4 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="grey", command=lambda: self.btn_click(4))
        b4.grid(row=3, column=0)

        b5 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="grey", command=lambda: self.btn_click(5))
        b5.grid(row=3, column=1)

        b6 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="grey", command=lambda: self.btn_click(6))
        b6.grid(row=3, column=2)

        Sub = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-", bg="grey", command=lambda: self.btn_click("-"))
        Sub.grid(row=3, column=3)

        # Row 3
        b1 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="grey", command=lambda: self.btn_click(1))
        b1.grid(row=4, column=0)

        b2 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="grey", command=lambda: self.btn_click(2))
        b2.grid(row=4, column=1)

        b3 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="grey", command=lambda: self.btn_click(3))
        b3.grid(row=4, column=2)

        mul = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*", bg="grey", command=lambda: self.btn_click("*"))
        mul.grid(row=4, column=3)

        # Row 4
        b0 = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="grey", command=lambda: self.btn_click(0))
        b0.grid(row=5, column=0)

        bc = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="C", bg="grey", command=self.clear)
        bc.grid(row=5, column=1)

        Decimal = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=".", bg="grey", command=lambda: self.btn_click("."))
        Decimal.grid(row=5, column=2)

        Div = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/", bg="grey", command=lambda: self.btn_click("/"))
        Div.grid(row=5, column=3)

        # Row 5
        # added mod operation
        bmod = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="%", bg="grey", command=lambda: self.btn_click("%"))
        bmod.grid(row=6, column=0)
        
        # added left parenthesis operation
        blpar = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="(", bg="grey", command=lambda: self.btn_click("("))
        blpar.grid(row=6, column=1)
        
        # added right parenthesis operation
        brpar = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=")", bg="grey", command=lambda: self.btn_click(")"))
        brpar.grid(row=6, column=2)
        
        # added exponents parenthesis operation
        bexp = Button(self.master, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="xʸ", bg="grey", command=lambda: self.btn_click("**"))
        bexp.grid(row=6, column=3)

        # Row 6
        # added delete operation
        bdel = Button(self.master, padx=16, pady=16, bd=4, width=8, fg="black", font=('ariel', 20, 'bold'), text="DEL", bg="grey", command=self.delete)
        bdel.grid(row=7, column=0, columnspan=2)
        
        # reformatted equal button
        bequal = Button(self.master, padx=16, pady=16, bd=4, width=8, fg="black", font=('ariel', 20, 'bold'), text="=", bg="grey", command=self.answer)
        bequal.grid(row=7, column=2, columnspan=2)

    def btn_click(self, num):
        result = self.logic.btn_click(num)
        self._input.set(result)

    def clear(self):
        result = self.logic.clear()
        self._input.set(result)

    def delete(self):
        result = self.logic.delete()
        self._input.set(result)

    def answer(self):
        result = self.logic.answer()
        self._input.set(result)


class CalculatorLogic:
    def __init__(self):
        self.operator = ""
        # added logic to keep track of what to do with saved answer
        self.reset_next_input = False

    def btn_click(self, num):
        # checks to see if we are currently at the saved answer and if the next input is a number and not a operation
        if self.reset_next_input and self.reset_next_input and str(num).isdigit():
            # in this case we want to clear it and keep track that we are not at a saved answer anymore
            self.operator = ""
            self.reset_next_input = False
        self.operator += str(num)
        # not at a saved answer anymore
        self.reset_next_input = False
        return self.operator

    def clear(self):
        self.operator = ""
        return self.operator

    # created delete function
    def delete(self):
        self.operator = self.operator[:-1]
        return self.operator
    
    
    def answer(self):
        # try except to only save valid answers
        try:
            ans = str(eval(self.operator))
            # saving our answer
            self.operator = ans
            # keep track that we are now at the state with a saved answer
            self.reset_next_input = True
            return ans
        except:
            self.operator = ""
            return "Error"


def main():
    root = Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()