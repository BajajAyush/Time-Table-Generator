import random
from PyQt5 import QtWidgets,uic
sub=[]




app=QtWidgets.QApplication([])
call=uic.loadUi("noofsub.ui")
call1=uic.loadUi("subject.ui")
def noof():
    noofsub=int(call.noofsub.text(),10)
    return noofsub
    sub.append()
    


    call.destroy()
    

call.submit.clicked.connect(noof)
call.show() 
app.exec()
noofsub=noof()
print(noofsub)

for i in range (0,noofsub):
    sname=input("Enter the name of subject:")
    sub.append(sname)
print("The subjects added are=",sub)
periodno={}
for i in sub:
    print("\t",i,":",end=" ")
    x=int(input("The number of periods for the subject are="))
    periodno[i]=x
print("The subjects with its periods are:",periodno)
teach={}
while True:
    for i in sub:
        print("\t",i,end=" ",)
        x=int(input("Enter the number of teachers for the subject:"))
        teachname=[]
        for j in range(0,x):
            name=input("Enter teacher name:")
            teachname.append(name)
        teach[i]=teachname
    else:
        break
print(teach)


secno=int(input("Enter number of sections:"))
sec={}
templist=[]
t=teach.copy()
for i in range(0,secno):
    x=str(input("Enter section name(roman numeral with section name in lowercase w/o space or special characters):"))
    temp={}
    for j in sub:
        y=random.choice(t[j])
        temp[j]=y
        templist.append(y)
        if templist.count(y)>=2 and periodno[j]>=5:
            t[j].remove(y)
    sec[x]=temp
print(sec)



#matrix

def tablemaker():
    row=5
    col=8
    import mysql.connector
    for n in sec:
        l=[[ (i,j) for j in range (col)] for i in range(row)]
        #print(l)
        free=l.copy()
        #this section ensures that all su8bjects are placed in a dufferent celll
        for i in sub:        
            for j in range(0,periodno[i]):
                x=random.randint(0,7)
                y=random.randint(0,4)
                z=(y,x)
                while True: 
                   if free[y][x]!=z:
                       x=random.randint(0,7)
                       y=random.randint(0,4)
                       z=(y,x)
                   else:
                       break
                p=free[y].index(z)
                free[y][p]=i
        for i in range(0,10000):
            for i in sub:
                for k in range(0 ,len(free)):
                    while True:
                        if free[k].count(i)>=2:
                            g=free[k].index(i)
                            x=random.randint(0,7)
                            y=random.choice((list(range(1,y))) + (list(range(y+1,4))))
                            a=free[y][x]
                            free[k][g]=a
                            free[y][x]=i
                        else:
                            break
      
        
        #inserting days into time time table 
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        e=0
        for h in free:
            h.insert(0,days[e])
            e+=1
        
        #print(free)    
        #consolidated dictionary of time tables
        cons={}
        abc=[]
        for h in free:
            abc.append(h)
        cons[n]=abc    
        
        print()
        print ("\033[4m",n,"\033[0m")
        print()
        print()
        #printing the result in pyhton
        for i in range(row):
            for j in range(col):
                print(l[i][j],end="       ")
            print()
        
    
    
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Ayush0510",
        database="timetable"
        )
        mycursor = mydb.cursor()
    
        r="create table "+n+"(Day varchar(15),I varchar(12),II varchar(12),III varchar(12),IV varchar(12),V varchar(12), VI varchar(12), VII varchar(12), VIII varchar(12))"
        print(r)
        mycursor.execute(r)
        
        for i in cons:
            for k in cons[i]:
                mycursor = mydb.cursor()
                d="insert into "+n+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(d,k)
                mydb.commit()




    
tablemaker()
"""def sqlinserter():
    
    import mysql.connector
    
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ayush0510",
    database="timetable"
    )
    mycursor = mydb.cursor()
    
    for n in sec:
        
        r="create table "+n+"(Day varchar(15),I varchar(12),II varchar(12),III varchar(12),IV varchar(12),V varchar(12), VI varchar(12), VII varchar(12), VIII varchar(12))"
        print(r)
        mycursor.execute(r)
    
    for i in cons:
        for k in cons[i]:
            mycursor = mydb.cursor()
            d="insert into "+n+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(d,k)
            mydb.commit()
                
sqlinserter()    
    
  """  
    
    
    
    

    

































