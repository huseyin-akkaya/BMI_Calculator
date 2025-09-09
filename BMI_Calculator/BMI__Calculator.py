import tkinter


window = tkinter.Tk()
window.title("BMI Calculator") #uygulamanın üst kısmında adını yazdırır
window.config(padx=30, pady=30) #açılacak pencerenin boyutu

input_question = tkinter.Label(text="Enter Your Wight(kg)",font=('Arial',10,'normal')) #kullanıcıdan verilerin istenmesi
input_question.pack(pady=5)

input_one = tkinter.Entry(width=10) #kullanıcı girdisi
input_one.pack()

input_question2 = tkinter.Label(text="Enter Your Height(cm)",font=('Arial',10,'normal')) #kullanıcıdan verilerin istennmesi
input_question2.pack(pady=5)

input_two = tkinter.Entry(width=10) #kullanıcı girdisi
input_two.pack()

result_label = tkinter.Label(text="",font=('Arial',10,'normal')) #ekranın altında bmı sonucun, kullanıcı kaynaklı hataların uyarılarının yazılması
result_label.pack()

def calculate_process():
    weight = input_one.get() #işlenecek değerler çağırılır
    height = input_two.get() #işlenecek değerler çağırılır

    if weight == '' or height == '': #kullanıcı değer girmezse uyarı verir uygulama çökmemesi için
        result_label.config(text="Enter both weight and height!")
        return None
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2) #bmı hesaplanması
            return bmi

        except: #kullanıcı sayı yerine farklı değer girerse uyarı verir uygulama çökmesinin önüne geçebilmek için
            result_label.config(text="Enter a valid number!")
            return None

def calculate_fonk():
    result = calculate_process()
    if result is None:  # sayı değilse veya boşsa direkt çık
        return

    if 18.5<= result <= 24.9: #yapılan bmı hesabının uygun aralığa göre kullanıcıya yansıtılması
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



calculator_button = tkinter.Button(text="Calculate",command=calculate_fonk) #hesaplama işlemini başlatabilmesi için kullanıcını tıklayacağı buton
calculator_button.pack(pady=10)



window.mainloop()


