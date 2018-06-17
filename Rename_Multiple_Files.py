import os
path=input('enter the file path where the files are:')
file_nm=os.listdir(path)
print('RENAME MENU'.center(20,'+'))
print('1.Remove numbers and non- aplhabetic characters')
print('2.Add Numbers Before Its Name')
print('3.Rename Ecah File One By One')
ch=input('enter a choice:')
os.chdir(path)
c1=1
for f in file_nm:
    if ch=='1':
        c=0
        for a in f:
            if a==' ' or a=='-' or a.isdigit():
                c=c+1
            elif a.isalpha():
                break
        os.rename(f,f[c:])
        
    if ch=='2':
        os.rename(f,str(c1)+'. '+f)
        c1+=1
        #print('file name changed')
    if ch=='3':
        print('Current File Name:'+f)
        i1=f.index('.')
        ext=f[i1:]
        new_fnm=input('enter New Name:')
        os.rename(f,new_fnm+ext)
        print('file name changed')
if ch=='1' or ch=='2':
    print("All file's  name changed")

