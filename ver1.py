import Tkinter as tk
import math

kalk = tk.Tk()
kalk.title("Kalkulator ver. 1.7")

etykiety = [
'7',  '8',  '9',  '*', 'C', 'pi', 'bin',
'4',  '5',  '6',  '/', 'ver', 'sqrt', 'hex',
'1',  '2',  '3',  '-', 'neg', 'kwadrat', 'log10',
'0',  '.',  '+',  '=', '=', '=', '=']

# ustawienia GUI
row = 1
col = 0
for i in etykiety:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(kalk, text = i, width = 5, height = 5, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 6:
        col = 0
        row += 1

wysw = tk.Entry(kalk, width = 50, bg = "white", font = "Helvetica 14 bold")  #width = szerokosc panelu wprowadzania '50'
wysw.grid(row = 0, column = 0, columnspan = 7)
wysw.focus()


def click_event(key):

	# = -> wyniki obliczen
    if key == '=':
        if '/' in wysw.get() and '.' not in wysw.get():
            wysw.insert(tk.END, ".0")
			
        try:
            result = eval(wysw.get())
            wysw.insert(tk.END, " = " + str(result))
        except:
            wysw.insert(tk.END, "   Error :(")
			
	# C -> czysczenie prompta		
    elif key == 'C':
        wysw.delete(0, tk.END)
		
		
	# ver -> wyswietlanie wersji programu
    elif key == 'ver':
        wysw.delete(0, tk.END)
        wysw.insert(tk.END, "Kalkulator ver. 1.7")
        
        
    elif key == 'pi':
		wysw.insert(tk.END, "3.14159")

    elif key == 'kwadrat':
		a=int(wysw.get())
		kwadrat=a*a
		wysw.delete(0, tk.END)
		wysw.insert(tk.END, kwadrat)
		
    elif key == 'sqrt':
		a=int(wysw.get())
		sqrt=math.sqrt(a)
		wysw.delete(0, tk.END)
		wysw.insert(tk.END, sqrt)

    elif key == 'bin':
		a=int(wysw.get())
		binary=bin(a)
		wysw.delete(0, tk.END)
		wysw.insert(tk.END, binary)

    elif key == 'hex':
		a=int(wysw.get())
		hexadecimal=hex(a)
		wysw.delete(0, tk.END)
		wysw.insert(tk.END, hexadecimal)
		
    elif key == 'log10':
		a=int(wysw.get())
		log10=math.log10(a)
		wysw.delete(0, tk.END)
		wysw.insert(tk.END, log10)
		
	# neg -> negate term
    elif key == 'neg':
        if '=' in wysw.get():
            wysw.delete(0, tk.END)
        try:
            if wysw.get()[0] == '-':
                wysw.delete(0)
            else:
                wysw.insert(0, '-')
        except IndexError:
            pass

	# czyszcenie wysietlacza		
    else:
        if '=' in wysw.get():
            wysw.delete(0, tk.END)
        wysw.insert(tk.END, key)

kalk.mainloop()
