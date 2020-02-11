'this is test demo'
f=open('data.txt','r')
lst=f.readlines()
f.close()
lst=[i for i in lst if i!='\n']
for i in lst:
    if i == '\n':
        lst.remove(i)
    else:
        j = i.split(',')
        if int(j[2])>100 or int(j[3])>100 or int(j[2])<0 or int(j[3])<0:
            lst.remove(i)
print('剩余人数为：',len(lst))
lst=sorted(lst,key=lambda x:x.split(',')[1],reverse=True)
lst=sorted(lst,key=lambda x:int(x.split(',')[2])*0.2+int(x.split(',')[3])*0.8,reverse=True)
for i in lst:
    s=i.split(',')
    if s[1]=='1':s[1]='Female'
    else:s[1]='Male'
    k=int(s[2])*0.2+int(s[3])*0.8
    print('{0:<20}{1:<10}{2:<5.1f}'.format(s[0],s[1],k))



