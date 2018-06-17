import requests,os,img2pdf,shutil,sys,time
from bs4 import BeautifulSoup
# url='https://readcomics.io/deadpool-2016/chapter-10'
url=input('enter the url of the comic book chapter from readcomics.io=')
# to create the folder that is having the images
folder_name=url.split('/')[3]+' '+url.split('/')[4]
path=input('enter the path where you want to save the pdf=')
npath=path+f'\{folder_name}'
try:
    os.mkdir(npath)   
except:
    pass

r=requests.get(url)
data=r.text
soup = BeautifulSoup(data, "lxml")
# to get the pages available to download
pages=int(soup.find("div", {"class": "label"}).text.split(' ')[1])
os.chdir(npath)
for i in range(1,pages+1):
    curl=url+'/'+str(i)
    comic=requests.get(curl)
    comic_content=comic.text
    soup=BeautifulSoup(comic_content,"lxml")
    img=soup.find_all('img')[1].get('src')
    try:
        name='image_'+i*'a'+'.'+img.split('.')[2]
        f=open(name,'wb')
        r1=requests.get(img)
        f.write(r1.content)
        f.close()
        perc=round((i/pages)*100,1)
        print(str(perc)+'% complete')

    except Exception as e:
        print(e)
        pass    
    curl=url

# Converting the images to PDF
with open(f"{folder_name}.pdf", "wb") as com:
    com.write(img2pdf.convert([i for i in os.listdir(npath) if i.endswith(".jpg")]))
    print('converted to pdf')
com.close()    
try:
    shutil.move(npath+f'\{folder_name}.pdf',path)
except Exception as e:
    print(e)
    pass
print('file moved')
try:
    shutil.rmtree(npath)
except Exception as e:
    print(e)
print('images deleted')    


