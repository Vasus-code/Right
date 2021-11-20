
#v3,3
#mabe by Vasinkvak1
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox as mes
from easygui import buttonbox as btb
import tkinter.font as tkfont



#Words in En
file = 'File'
langs = ['English','Русский']
fixed = 'v3.3\nFixed cursor\'s color in the dark theme\nChange cursor\'s width  and e.t.c'
infBugs = 'IF you want to save the file\nplease insert the expansion of your file\nelse it won\'t be saved corectly!'
langchose = ['Select language\nPlease restart program after!','Language']
save = 'Save'
load = 'Load'
inf = 'Inf'
quit = 'Quit'
frathes = ['Select theme, you like\nPlease restart program after!']
words = ['Theme','language','Sittings']
styles = ['Dark','Bright']
styleNow = ['','']
styleB = ['#F2F2F2', '#FFFFFF']# Top panel ; Text panel; Bright version 
styleD =['#3C3F41','#2B2B2B']  
styleChose = ['Please restart program after!','Style']
styleDefold= '#F2F2F2','#FFFFFF'
curbg = ''
#Проверка темы
try:
	filestyle = open('stPar.txt','r').read()
	filestyle2 = open('stPar2.txt','r').read()
	styleNow[0] = filestyle
	styleNow[1] = filestyle2
	
	if styleNow[0] == styleD[0]:
		curbg = '#BCBCBC'
	elif styleNow[1] == styleB[1]:
		curbg = '#000000'
	
except:
	filestyle  = open('stPar.txt','w').write(str(styleB[0]))
	filestyle2  = open('stPar2.txt','w').write(str(styleB[1]))
	styleNow[0] = styleB[0]
	styleNow[1] = styleB[1]
	curbg = '#000000'



	


#Проверка языка
try:
	filelang = open('usPar.txt','r').read()
	if langs[0] in filelang :
		pass
	elif langs[1] in filelang:
		#русский слова
		file= 'Файл'
		infBugs = 'Если вы хотите сохранить файл,\nпожалуйста вводите расишрение вашего файла,\nиначе он сохранисться не правельно!'
		langchose = ['Выберите язык\nПожалуйста потом перезагрузите программу', 'Язык']
		fixed = 'v3.3\nИсправлен цвет курсора в темной теме\nИзменена ширина курсора и тп'
		save = 'Сохранить'
		load = 'Открыть'
		inf = 'Информация'
		quit = 'Выйти'
		words = ['Тема','Язык','Настройки']
		frathes = ['Вибирите тему\nПожалуйста потом перезагрузите программу']
		styles = ['Темная', 'Светлая']
		styleChose = ['Пожалуйств перезагрузите ваш ','Style']


except:
	pass

#Functions





def Quit():  	#Quit
	global root
	root.destroy()

def LoadFile():  #Load file
	ftypes = [('all files','*'), ('txt files', '*.txt'),('python files','*.py'),
			  ('html files','*.html'),('css filse','*.css'),('js files','*.js')]
	fn = tkinter.filedialog.Open(root, filetypes = ftypes).show()

	if fn == '':
		return
	textbox.delete('1.0','end')
	textbox.insert('1.0',open(fn).read())

	global cur_path
	cur_path = fn






def SaveFile():	#Save file
	fn = tkinter.filedialog.SaveAs(root, filetypes = [('all files','*'), ('txt files', '*.txt'),('python files','*.py'),
													  ('html files','*.html'),('css filse','*.css'),('js files','*.js')]).show()
	if fn == '':
		return
	open(fn,'wt').write(textbox.get('1.0','end'))

def Inf():	#Information
	mes.showinfo('Inf','Text editor \'Right\' \nV3.3\nMade by Vasinkvak1')		#Inf and version
	mes.showinfo('Bugs',infBugs)
	mes.showinfo('Fixed',fixed)

def Sittings():	#Sittings
	sittins = btb('',words[2],words[0:2])	#Sittings menu
	if sittins == words[1]:


									#If change lenguage
		lang = btb(langchose[0],langchose[1],langs)
		if lang == langs[0]:
			usPars = open('usPar.txt','w').write(langs[0])

		elif lang == langs[1]:
			usPars = open('usPar.txt', 'w').write(langs[1])
		else:
			return



											#If change style
	elif sittins == words[0]:
		style = btb(frathes[0],words[0] ,styles)#What style?
		if style == styles[0]:#If Dark
			filestyle = open('stPar.txt','w').write(str(styleD[0]))
			
			filestyle2 = open('stPar2.txt','w').write(str(styleD[1]))
			

		elif style == styles[1]:		#If bright
			filestyle = open('stPar.txt','w').write(str(styleB[0]))
		
			filestyle2 = open('stPar2.txt','w').write(str(styleB[1]))
			
			


#Tkinter


root = Tk()
root.title('Right')



if styleNow[0] == '#3C3F41':
	textFg = '#BABABA'
else:
	textFg = 'black'

textbox = Text(root, font="Courier 19", wrap = 'word',bg = styleNow[1],fg = textFg)
scrollbar = Scrollbar(root)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill  = 'both', expand = '1')

font = tkfont.Font(font=textbox['font'])					# Set Tab size
tab_size = font.measure('    ')
textbox.config(tabs=tab_size,insertbackground = curbg,insertwidth = 1.8)
scrollbar.pack(side = 'right', fill  = 'y')


menubar = tkinter.Menu(root,bg = styleNow[0])

filemenu = tkinter.Menu(menubar)
filemenu.add_command(label = load, command = LoadFile)
filemenu.add_command(label = save, command = SaveFile)
filemenu.add_command(label = words[2], command = Sittings)

menubar.add_cascade(label = file, menu=filemenu)
menubar.add_command(label = inf, command = Inf)
menubar.add_command(label = quit, command = Quit)

root.config(menu=menubar)


root.mainloop()
