import tkinter as tk
from tkinter import *
import requests
from PIL import ImageTk, Image
from tkinter import Tk, Frame, Canvas
from tkinter import Tk, Canvas
import math
import PIL

def round_up(number:float, digits:int):
  return math.ceil(number * 10**digits) / 10**digits

def convert():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    conversion_rate = data['rates'][to_currency]
    
    converted_amount = amount * conversion_rate
    converted_amount = round_up(converted_amount, 2)
    result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")

    label_rate.config(text = f"1 {from_currency} = {conversion_rate} {to_currency}")

def get_exchange_rate():
    try:
        response = requests.get('https://api.coinbase.com/v2/prices/eur-rub/spot')
        data = response.json()
        euro_rate = data['data']['amount']

        response = requests.get('https://api.coinbase.com/v2/prices/usd-rub/spot')
        data = response.json()
        dollar_rate = data['data']['amount']

        response = requests.get('https://api.coinbase.com/v2/prices/btc-usd/spot')
        data = response.json()
        bitcoin_price = data['data']['amount']
    
        response = requests.get('https://api.coinbase.com/v2/prices/eth-usd/spot')
        data = response.json()
        ethereum_price = data['data']['amount']

        euro_rate = float(euro_rate)
        dollar_rate = float(dollar_rate)
        bitcoin_price = float(bitcoin_price)
        ethereum_price = float(ethereum_price)

        euro_label.config(text='EUR: {:.3f}'.format(euro_rate))
        dollar_label.config(text='USD: {:.3f}'.format(dollar_rate))
        bitcoin_label.config(text='BTC: {:.3f}'.format(float(bitcoin_price)))
        ethereum_label.config(text='ETH: {:.3f}'.format(float(ethereum_price)))
    except requests.exceptions.RequestException:
        currency_label = tk.Label(window, font=('Arial', 24, 'bold'))
        currency_label.config(text='Ошибка при обновлении курса')
    window.after(5000, get_exchange_rate)
    
window = tk.Tk()
window.title('Changer')
window.resizable(width=False, height=False)
window.geometry("710x648")

img =Image.open('ChangerBack.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(window, image=bg)
label.place(x = 0,y = 0)

euro_label = tk.Label(window, font=('Arial', 20), bg="black", fg="white")
euro_label.place(x=20, y=20)

dollar_label = tk.Label(window, font=('Arial', 20), bg="black", fg="white")
dollar_label.place(x=525, y=20)

bitcoin_label = tk.Label(window, font=('Arial', 20), bg="black", fg="white")
bitcoin_label.place(x=20, y=600)

ethereum_label = tk.Label(window, font=('Arial', 20), bg="black", fg="white")
ethereum_label.place(x=500, y=600) 

nameLabelU = tk.Label(window, text="U", fg="white", bg="black", font="Algerian 30")
nameLabelU.place(x=20, y=200)

nameLabelN = tk.Label(window, text="N", fg="white", bg="black", font="Algerian 30")
nameLabelN.place(x=20, y=240)

nameLabelI = tk.Label(window, text="I", fg="white", bg="black", font="Algerian 30")
nameLabelI.place(x=25, y=280)

nameLabelT = tk.Label(window, text="T", fg="white", bg="black", font="Algerian 30")
nameLabelT.place(x=20, y=320)

nameLabelE = tk.Label(window, text="E", fg="white", bg="black", font="Algerian 30")
nameLabelE.place(x=20, y=360)

nameLabelD = tk.Label(window, text="D", fg="white", bg="black", font="Algerian 30")
nameLabelD.place(x=20, y=400)

nameLabelC = tk.Label(window, text="C", fg="white", bg="black", font="Algerian 30")
nameLabelC.place(x=628, y=180)

nameLabelH = tk.Label(window, text="H", fg="white", bg="black", font="Algerian 30")
nameLabelH.place(x=628, y=220)

nameLabelA = tk.Label(window, text="A", fg="white", bg="black", font="Algerian 30")
nameLabelA.place(x=625, y=260)

nameLabelNN = tk.Label(window, text="N", fg="white", bg="black", font="Algerian 30")
nameLabelNN.place(x=628, y=300)

nameLabelG = tk.Label(window, text="G", fg="white", bg="black", font="Algerian 30")
nameLabelG.place(x=627, y=340)

nameLabelEE = tk.Label(window, text="E", fg="white", bg="black", font="Algerian 30")
nameLabelEE.place(x=628, y=380)

nameLabelR = tk.Label(window, text="R", fg="white", bg="black", font="Algerian 30")
nameLabelR.place(x=628, y=420)

amount_label = tk.Label(window, text="Am:", fg="white", bg="black", font="Arial 17")
amount_label.place(x=250, y=235)

amount_entry = tk.Entry(window, fg="black", bg="white", font="Arial 16", width=8,textvariable=1)
amount_entry.place(x=305, y=240)

from_label = tk.Label(window, text="Fr:", fg="white", bg="black", font="Arial 17")
from_label.place(x=250, y=285)

from_currency_var = tk.StringVar(window)
from_currency_var.set("RUB") 
from_currency_menu = tk.OptionMenu(window, from_currency_var, "USD", "EUR", "CNY", "RUB")
from_currency_menu.place(x=305, y=290)

to_label = tk.Label(window, text="To:", fg="white", bg="black", font="Arial 17")
to_label.place(x=250, y=335)

to_currency_var = tk.StringVar(window)
to_currency_var.set("USD") 
to_currency_menu = tk.OptionMenu(window, to_currency_var, "USD", "EUR", "CNY", "RUB")
to_currency_menu.place(x=305, y=338)

CR_Label = tk.Label(window, text="Cr:", bg="black", fg="white", font="Arial 17")
CR_Label.place(x=250, y=382)

convert_button = tk.Button(window, text="Convert", command=convert, font="Arial 12 bold", bg="black", fg="white")
convert_button.place(x=215, y=420)

label_rate = tk.Label(window, fg="white", bg="black", font="Arial 14", borderwidth=2, relief="raised")
label_rate.place(x=305, y=385)

result_label = tk.Label(window, fg="white", bg="black", font="Arial 14", borderwidth=2, relief="raised")
result_label.place(x=305, y=422)

imag =Image.open('LogoChanger.jpg')
bag = ImageTk.PhotoImage(imag)
labela = Label(window, image=bag)
labela.place(x = 295, y = 20)

get_exchange_rate()

window.mainloop()
