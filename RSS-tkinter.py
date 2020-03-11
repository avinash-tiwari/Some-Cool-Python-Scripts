import bs4,requests,webbrowser,os
from tkinter import *
import wckToolTips

# r=requests.get('http://www.androidauthority.com/feed')
r=requests.get('https://www.androidcentral.com/rss.xml')

r.raise_for_status()
b=bs4.BeautifulSoup(r.text,'xml')

os.chdir(r'c:\users\tiwari\desktop')
f=open('androidcen_xml.txt','w')
f.write(b.prettify())
f.close()
# print('__________________________CAtegory_______________________')
# cat=b.find_all('category')
# for i in cat:
# 	print(i.text)
# print('__________________________________________________________')	
# print('_________________________description______________________')
# desc=b.find_all('description')
# for i in desc:
# 	print(i.text)
# print('___________________________________________________________')	
# __________________title tag consist of imp article_______________
ti=b.find_all('title')
# _________________________________________________________________

# ___________________all links_______________________________
link=b.find_all('link')
# _________________________________________________________________

# print('_________________________publication date____________________________')
# pub=b.find_all('pubDate')
# for i in pub:
# 	print(i.text)
# print('_______________________________________________________________________')
def but(event):
	bu=event.widget
	for i in b.find_all('item'):
		if i.title.text==bu['text']:
			webbrowser.open(i.link.text)
	
def ent(event):
	bu=event.widget
	bu['fg']='red'

def lea(event):
	bu=event.widget
	bu['fg']='black'

def but1(event):
	for j in f.winfo_children():
		j.destroy()
	c1=0
	for i in ti:
		l2=Label(f,text=i.text)
		l2.bind('<Button-1>',but)
		l2.bind('<Enter>',ent)
		l2.bind('<Leave>',lea)
		l2.grid(row=0+c1,column=0)
		c1+=1	

def addurl():
	v1=StringVar()
	t=Toplevel(root)
	t.title('Add RSS URL')
	Label(t,text='add url here').grid(row=0,column=0)
	e1=Entry(t,textvariable=v1).grid(row=0,column=1)
	b1=Button(t,text='Add').grid(row=1,column=0)
	
root=Tk()
root.title('RSS READER')
l1=Label(root,text=ti[0].text)
l1.grid(row=1,column=0)

Button(root,text='ADD',command=addurl).grid(row=0,column=0)

ti.pop(0)
l1.bind('<Enter>',ent)
l1.bind('<Button-1>',but1)
if len(b.description.text)>0:
	wckToolTips.register(l1,b.description.text)
f=Frame(root)
f.grid(row=2,column=0)

# c1=0
# for i in ti:
# 	l2=Label(f,text=i.text)
# 	l2.bind('<Button-1>',but)
# 	l2.bind('<Enter>',ent)
# 	l2.bind('<Leave>',lea)
# 	l2.grid(row=0+c1,column=0)
# 	c1+=1
root.mainloop()
