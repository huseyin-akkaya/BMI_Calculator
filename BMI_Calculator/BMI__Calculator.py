import tkinter


window = tkinter.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

def calculate_process():
    weight = input_one.get()
    height = input_two.get()

    if weight == '' or height == '':
        result_label.config(text="Enter both weight and height!")
        return None
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            return bmi

        except:
            result_label.config(text="Enter a valid number!")
            return None


input_question = tkinter.Label(text="Enter Your Wight(kg)",font=('Arial Black',10,'normal'))
input_question.pack(pady=10)

input_one = tkinter.Entry(width=10)
input_one.pack()

input_question2 = tkinter.Label(text="Enter Your Height(cm)",font=('Arial Black',10,'normal'))
input_question2.pack(pady=10)

input_two = tkinter.Entry(width=10)
input_two.pack()

result_label = tkinter.Label(text="",font=('Arial',10,'normal'))
result_label.pack(pady=20)



def calculate_fonk():
    result = calculate_process()
    if result is None:  # sayı değilse veya boşsa direkt çık
        return

    if 18.5<= result <= 24.9:
        result_label.config(text=f"Your BMI is: {result:.2f} -> Normal",fg="green")
    elif result<18.5:
        result_label.config(text=f"Your BMI is: {result:.2f} -> Weak",fg="blue")
    elif 25<=result <= 29.9:
        result_label.config(text=f"Your BMI is: {result:.2f} -> Overweight",fg="orange")
    elif 40<=result <= 50:
        result_label.config(text=f"Your BMI is: {result:.2f} -> Morbid Obese",fg="red")
    elif result>50:
        result_label.config(text=f"Your BMI is: {result:.2f} -> Super obese",fg="dark red")
    else:
        result_label.config(text=f" {result:.2f} Invalid dialing ",fg="black")



calculator_button = tkinter.Button(text="Calculate",command=calculate_fonk)
calculator_button.pack(pady=10)


window.mainloop()