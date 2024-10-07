import tkinter as tk
from tkinter import messagebox

#window
window = tk.Tk()
window.title("Pyton Tkinter")
window.minsize(width=450, height=300)

#label
lWeight=tk.Label(text="Enter Your Weight (kg)", font=('Arial',12))
lWeight.pack()
#weight
tWeight = tk.Entry()
tWeight.pack()
#label
lHeight=tk.Label(text="Enter Your Height (cm)", font=('Arial',12))
lHeight.pack()
#weight
tHeight = tk.Entry()
tHeight.pack()


def vki (weight:int,height:int):
    return weight / ((height / 100) ** 2)

def vki_d(vki_):


    if vki_ <18.50:
        return "Düşük kilolu"
    elif 18.49 < vki_ < 24.99:
        return "Normal kilo"
    elif 25 < vki_ <29.99:
        return "Fazla kilolu"
    else:
        return "Obez"

def click_button():
    tW=tWeight.get()
    tH=tHeight.get()

    if tW and tH:
        if tWeight.get().isnumeric() and tWeight.get().isnumeric():
            vkiSonucu = vki(int(tW), int(tH))
            metin = vki_d(vkiSonucu)
            messagebox.showinfo("Uyari", f"VKI = {vkiSonucu}, {metin}")
        else:
            messagebox.showwarning("Uyari", "Lutfen bir sayi giriniz")

    else:
        messagebox.showinfo("Uyari", "Lutfen Verileri Giriniz")

my_button = tk.Button(text= "Calculate", command = click_button)
my_button.pack()



window.mainloop()

