import Tkinter as tk

kalk = tk.Tk()
kalk.title("Kalkulator ver. 1.3")

etykiety = [
'7',  '8',  '9',  '*', 'C',
'4',  '5',  '6',  '/', 'ver',
'1',  '2',  '3',  '-', 'neg',
'0',  '.',  '+',  '=', '=']

# set up GUI
row = 1
col = 0
for i in etykiety:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(kalk, text = i, width = 5, height = 5, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

wysw = tk.Entry(kalk, width = 50, bg = "white", font = "Helvetica 14 bold")  #width = szerokosc panelu wprowadzania '50'
wysw.grid(row = 0, column = 0, columnspan = 5)
wysw.focus()

def click_event(key):

	# = -> calculate results
    if key == '=':
        # safeguard against integer division
        if '/' in wysw.get() and '.' not in wysw.get():
            wysw.insert(tk.END, ".0")
			
        # attempt to evaluate results
        try:
            result = eval(wysw.get())
            wysw.insert(tk.END, " = " + str(result))
        except:
            wysw.insert(tk.END, "   Error, use only valid chars")
			
	# C -> czysczenie prompta		
    elif key == 'C':
        wysw.delete(0, tk.END)
		
		
	# ver -> wyswietlanie wersji programu
    elif key == 'ver':
        wysw.delete(0, tk.END)
        wysw.insert(tk.END, "Kalkulator ver. 1.3")
		

	# git -> adres do zdalnego repo na githubie		
    elif key == 'git':
        wysw.delete(0, tk.END)
        wysw.insert(tk.END, "https://github.com/kamilpek/python-kalkulator")		

		
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

	# clear wysw and start new input		
    else:
        if '=' in wysw.get():
            wysw.delete(0, tk.END)
        wysw.insert(tk.END, key)


# RUNTIME
kalk.mainloop()
