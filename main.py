
from tkinter import *
from depress_cubic import *
from complex import *
from cardano import *
from covid import *

root = Tk() 
root.title('Cardano\'s Method')

input_field = Entry(root, width=35)
input_field.pack() 

label_rn = Label(root, text="Enter a potential case count and the program will tell you how long from now Canada is projected to hit that particular case count.\n")
label_rn.pack()

response = Label(root, text='Waiting for input...press submit once ready')
response.pack()

num_attempts = 0
case_count = 0

def when_clicked():
    global num_attempts, case_count
    try:
        case_count = int(input_field.get())
        response.config(text = "Input processed succesfully...please standby")
        root.destroy()
    except ValueError:
        num_attempts += 1
        response.config(text = f"Invalid input, please correct input format and press submit again. Number of invalid attempts: {num_attempts}")    

submit_button = Button(root, text="Submit number", command=when_clicked)
submit_button.pack()

root.mainloop()

coeff = covid_graph()
coeff[3] -= case_count
coeff.reverse()

coeff, H, G, shift = depressed_cubic(coeff)

print(coeff)

answers = cardano_method(H, G, shift)


start_date = date(2021, 11, 26)
end_date = date.today()
days_passed = (end_date - start_date).days

answers = [num_days.real for num_days in answers if (num_days.imaginary == 0) and (num_days.real > days_passed)]
answers.sort() # in the case there are multiple answers, it is probably because the cubic function loops around after going into the negatives briefly; to avoid this, only the smallest possible answer is taken

root = Tk() 
root.title('Cardano\'s Method')

display_ans = Label(root, text = '')

if (len(answers) == 0):
    display_ans = Label(root, text= f"The model does not expect Canada to record {case_count} in the forseeable future.")
else:
    display_ans = Label(root, text = f"Based on the current model, it is expected that Canada will record {case_count} cases in {round(answers[0]-days_passed)} day(s).")
display_ans.pack()

root.mainloop()
