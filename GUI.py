
from tkinter import Tk, Label, Entry, Button
from cubic import CubicEquation

class GUI:

    # constructor

    def __init__(self):
        pass

    # loading the GUI to interact with the user

    def load(self):
        # creating a GUI object using tkinter
        root = Tk() 

        # setting a title for the window
        root.title('Cardano\'s Method')

        # adding a label to the window with instructions for what to enter
        label = Label(root, text="Enter the cubic polynomial's coefficients (must be real) in order of decreasing degree separated by commas.\n")
        label.pack()

        # adding a text box to the window to collect user input
        inputField = Entry(root)
        inputField.pack() 

        # declaring global variables to store input taken from the gui
        coefficients = []

        # a method to deal with the action when the user pushes the submit button
        def whenClicked():
            nonlocal coefficients

            try:
                # collecting user input and parsing it appropriately
                coefficients = [int(i) for i in inputField.get().split(',')]

                # exiting the current window by destroying the current window
                root.destroy()
            
            except ValueError:
                # not returning anything in the case invalid input is provided
                return

        # adding a submit button to the window to allow the user to 'submit' their input
        submitButton = Button(root, text="Submit Coefficients", command=whenClicked)
        submitButton.pack()

        # running the main loop for the GUI object
        root.mainloop()

        # initializing a CubicEquation object using the equation taken as input
        currentEquation = CubicEquation(coefficients)
        
        # calling the solve method to solve the cubic equations, and then assigning that to 
        answers = currentEquation.solve()

        # creating a GUI object using tkinter
        root = Tk() 

        # setting a title for the window
        root.title('Cardano\'s Method')

        # adding a label to the window with the roots determined for the entered polynomial
        displayRoots = Label(root, text=f"the roots of the given polynomial are {', '.join(str(root) for root in answers)}.")
        displayRoots.pack()

        # running the main loop for the GUI object
        root.mainloop()
