import Tkinter as tk

kalk = tk.Tk()
kalk.title("Kalkulator ver. 1")

buttons = [
'7',  '8',  '9',  '*', 'C',
'4',  '5',  '6',  '/', 'ver',
'1',  '2',  '3',  '-', 'git',
'0',  '.',  '=',  '+', ' ']

# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(kalk, text = i, width = 5, height = 5, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(kalk, width = 50, bg = "white")  #width = szerokosc panelu wprowadzania '50'
display.grid(row = 0, column = 0, columnspan = 5)

def click_event(key):

	# = -> calculate results
    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")
			
        # attempt to evaluate results
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")
			
	# C -> clear display		
    elif key == 'C':
        display.delete(0, tk.END)
		
		
	# $ -> clear display		
    elif key == 'ver':
        display.delete(0, tk.END)
        display.insert(tk.END, "Kalkulator ver. 1")
		

	# @ -> clear display		
    elif key == '@':
        display.delete(0, tk.END)
        display.insert(tk.END, "https://github.com/kamilpek/python-kalkulator")		

		
	# neg -> negate term
    elif key == 'neg':
        if '=' in display.get():
            display.delete(0, tk.END)
        try:
            if display.get()[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except IndexError:
            pass

	# clear display and start new input		
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)


# RUNTIME
kalk.mainloop()
