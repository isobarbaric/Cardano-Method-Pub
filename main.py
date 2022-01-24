from depress_cubic import *
from complex import *
from cardano import *

# list indices 'i' map directly to a_i notation 
coeff = [int(i) for i in input("Enter the cubic polynomial's coefficients in order of increasing degree separated by spaces. Any vanishing terms should be included with the coefficient zero.\n").split()]

root = Tk() 
root.title('Cardano\'s Method')

input_field = Entry(root, width=65)
input_field.pack() 

label_rn = Label(root, text="Enter the cubic polynomial's coefficients in order of increasing degree separated by spaces. Any vanishing terms should be included with the coefficient zero.\n")
label_rn.pack()

response = Label(root, text='Waiting for input...press submit once ready')
response.pack()

num_attempts = 0
coeff = []

def when_clicked():
    global num_attempts, coeff
    try:
        coeff = [int(i) for i in input_field.get().split()]
        response.config(text = "Input processed succesfully...please standby")
        root.destroy()
    except ValueError:
        num_attempts += 1
        response.config(text = f"Invalid input, please correct input format and press submit again. Number of invalid attempts: {num_attempts}")    

submit_button = Button(root, text="Submit coefficients", command=when_clicked)
submit_button.pack()

root.mainloop()

# real coefficients only 

coeff, H, G, shift = depressed_cubic(coeff)

answers = cardano_method(H, G, shift)

for root in answers:
    print(root)
