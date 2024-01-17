#Lab 2 (part 2)
#student name: Ethan Watchorn
#student number: 16538530

from __future__ import annotations  #helps with type hints
from tkinter import *
#do not import any more modules

#do not change the skeleton of the program. Only add code where it is requested. 
class Complex:
    """ 
        this class implements the complex number type 
        it stores the complex number
        two data fields: 
            real and complex
        Operation: 
            add, subtract, multiply and divide
            toString
    """
    def __init__(self, real: int, complex: int) -> None:
        """ initializer stores the complex number """ 
        self.real = real
        self.complex = complex
    
    def add(self, secondComplex: Complex) -> Complex:
        """
           adds 'this' rational to secondRational
           returns the result as a rational number (type Rational)
        """
        # Adds both complex numbers (Don't need to convert any signs/scale)
        new_complex = Complex(
            real=(self.real + secondComplex.real),
            complex=(self.complex + secondComplex.complex)
        )
        return new_complex
    
    def subtract(self, secondComplex: Complex) -> Complex:
        """
           subtracts secondRational from 'this' rational to 
           returns the result as a rational number (type Rational)
        """ 
        # Subtracts second complex number (Very similar implementation to add())
        new_complex = Complex(
            real=(self.real - secondComplex.real),
            complex=(self.complex - secondComplex.complex)
        )
        return new_complex

    def multiply(self, secondComplex: Complex) -> Complex:
        """
           multiplies 'this' rational to secondRational
           returns the result as a rational number (type Rational)
        """
        # using (x+yi)*(u+vi)=(xu-yv)+(xv+yu)i to instantiate a new Complex number
        new_real = (self.real*secondComplex.real) - (self.complex*secondComplex.complex)
        new_complex = (self.real*secondComplex.complex) + (self.complex*secondComplex.real)
        ret_val = Complex(
            real=new_real,
            complex=new_complex
        )
        return ret_val

    def divide(self, secondComplex: Complex) -> Complex:
        """
           divides 'this' rational by secondRational
           returns the result as a rational number (type Rational)
        """
        denominator = (secondComplex.real ** 2) + (secondComplex.complex ** 2)
        if denominator == 0:
            # If dividing by 0, output value will be NaN
            new_complex = Complex(None, None)
        else:
            real_numerator = (self.real*secondComplex.real) + (self.complex*secondComplex.complex)
            complex_numerator = (self.complex*secondComplex.real) - (self.real*secondComplex.complex)
            new_complex = Complex(
                real=real_numerator/denominator,
                complex=complex_numerator/denominator
            )

        return new_complex

    def toString(self) -> str:
        """             
            returns a string representation of 'this' rational
            the general output format is: numerator/denominator
            especial cases:
                if 'this' rational is an integer, it must not show any denominator 
                if denominator is 0, it returns "NaN" (not a number)
                if numerator or the denominator is not an integer, it returns "NaN"
        """ 
        # If numerator is a multiple of denominator, then only return the numerator
        complex_string = str(abs(self.complex)) + "i" if self.complex != 1 else "i"
        if self.complex == 0:
            return str(self.real)
        elif self.real == 0:
            return complex_string
        # If denominator is 0, return "Nan"
        elif (self.real == None) or (self.complex == None):
            return "NaN"
        # Otherwise, it's a normal rational. Can print out like normal.
        else:
            sign = "+" if self.complex > 0 else "-"
            return str(self.real) + sign + complex_string

# Note - 3 types of changes to GUI class:
#       1. Changed size of the window (didn't want to keep resizing each time I ran the program)
#       2. Naming conventions for symbols (changed Rational class to Complex)
#       3. Text/formatting in the window (says "Complex 1/2: " instead of "Rational 1/2: ")
#                                        ("+" instead of "/")
#                                        (added "i" at the end of each frame)
#      - I kept everything else that didn't affect functionality/look of the output
#           (you can still find things like self.rational1Denominator, but
#            since that name doesn't affect anything I didn't change it.)
class GUI:
    """ 
        this class implements the GUI for our program
        use as is.
        The add, subtract, multiply and divide methods invoke the corresponding
        methods from the Rational class to calculate the result to display.
    """
    def __init__(self):
        """ 
            The initializer creates the main window, label and entry widgets,
            and starts the GUI mainloop.
        """
        window = Tk()
        window.title("Complex Numbers")
        window.geometry("380x180")
       
        # Labels and entries for the first rational number
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1, pady = 10)
        Label(frame1, text = "Complex 1:").pack(side = LEFT)
        self.rational1Numerator = StringVar()
        Entry(frame1, width = 5, textvariable = self.rational1Numerator, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "+").pack(side = LEFT)
        self.rational1Denominator = StringVar()
        Entry(frame1, width = 5, textvariable = self.rational1Denominator, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "i").pack(side = LEFT)
        
        # Labels and entries for the second rational number
        frame2 = Frame(window)
        frame2.grid(row = 3, column = 1, pady = 10)
        Label(frame2, text = "Complex 2:").pack(side = LEFT)
        self.rational2Numerator = StringVar()
        Entry(frame2, width = 5, textvariable = self.rational2Numerator, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "+").pack(side = LEFT)
        self.rational2Denominator = StringVar()
        Entry(frame2, width = 5, textvariable = self.rational2Denominator, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "i").pack(side = LEFT)
        
        # Labels and entries for the result rational number
        # an entry widget is used as the output here
        frame3 = Frame(window)
        frame3.grid(row = 4, column = 1, pady = 10)
        Label(frame3, text = "Result:     ").pack(side = LEFT)
        self.result = StringVar()
        Entry(frame3, width = 10, textvariable = self.result, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)

        # Buttons for add, subtract, multiply and divide
        frame4 = Frame(window) # Create and add a frame to window
        frame4.grid(row = 5, column = 1, pady = 5, sticky = E)
        Button(frame4, text = "Add", command = self.add).pack(
            side = LEFT)
        Button(frame4, text = "Subtract", 
               command = self.subtract).pack(side = LEFT)
        Button(frame4, text = "Multiply", 
               command = self.multiply).pack(side = LEFT)
        Button(frame4, text = "Divide", 
               command = self.divide).pack(side = LEFT)
               
        mainloop()
        
    def add(self): 
        (rational1, rational2) = self.getBothRational()
        result = rational1.add(rational2)
        self.result.set(result.toString())
    
    def subtract(self):
        (rational1, rational2) = self.getBothRational()
        result = rational1.subtract(rational2)
        self.result.set(result.toString())
    
    def multiply(self):
        (rational1, rational2) = self.getBothRational()
        result = rational1.multiply(rational2)
        self.result.set(result.toString())
    
    def divide(self):
        (rational1, rational2) = self.getBothRational()
        result = rational1.divide(rational2)
        self.result.set(result.toString())

    def getBothRational(self):
        """ Helper method used by add, subtract, multiply and divide methods """
        try:
            numerator1 = eval(self.rational1Numerator.get())
            denominator1 = eval(self.rational1Denominator.get())
            rational1 = Complex(numerator1, denominator1)

            numerator2 = eval(self.rational2Numerator.get())
            denominator2 = eval(self.rational2Denominator.get())
            rational2 = Complex(numerator2, denominator2)
            return (rational1, rational2)
        except:
            return(Complex(0,0), Complex(0,0)) #if an entry value is missing, cause NaN

if __name__ == "__main__": GUI()