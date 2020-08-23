import random
import copy
from PyQt5 import QtWidgets,uic



sub=[]
periodno={}

xyz=[]

app=QtWidgets.QApplication([])
call=uic.loadUi("noofsub.ui")

def noof():
    noofsub=int(call.noofsub.text(),10)
    return noofsub
    
call.submit.clicked.connect(noof)
call.show() 
app.exec()
noofsub=noof()

teach={}
for i in range (0,noofsub):
    call1=uic.loadUi("subject.ui")
    def data():
        subject=call1.ename.text()
        sub.append(subject)
        noofperiod=int(call1.eperiod.text(),10)
        periodno[subject]=noofperiod
        teachname=call1.eteach.text()
        xyz=teachname.split(',')
        teach[subject]=xyz
        #print(teach)
    call1.submit1.clicked.connect(data)
    call1.show() 
    app.exec()   
#print(sub)
#print(periodno)
print(teach)    


sec={}
tx=copy.deepcopy(teach)
t=tx.copy()
call2=uic.loadUi("noofsec.ui")
def sect():
    secno=call2.secno.intValue()
    return secno
    
call2.submit2.clicked.connect(sect)
call2.show() 
app.exec()


templist=[]
secno=sect()
call3=uic.loadUi("classes.ui")
def clss():
    clss=call3.Classes.currentText()
    return clss

call3.Submit3.clicked.connect(clss)
call3.show() 
app.exec()
clss=clss()
for i in range(0,secno):
    #x=str(input("Enter section name(roman numeral with section name in lowercase w/o space or special characters):"))
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    x=clss+alpha[i]
    temp={}
    for j in sub:
        y=random.choice(t[j])
        temp[j]=y
        templist.append(y)
        if templist.count(y)>=2 and periodno[j]>=5:
            t[j].remove(y)
    sec[x]=temp
print(sec)


def tablemaker():
    row=5
    col=8
    global cons,l 
    cons={}
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
        for i in range(10):
            for i in sub:
                for k in range(0 ,len(free)):
                    while True:
                        if free[k].count(i)>2:
                            g=free[k].index(i)
                            x=random.randint(0,7)
                            y=random.choice((list(range(0,k))) + (list(range(k+1,5))))
                            a=free[y][x]
                            if a!=i:
                                free[k][g]=a
                                free[y][x]=i
                            else:
                                continue
                                
                            """
                            else:
                                if free[k].count(i)>2:
                                     g=free[k].index(i)
                                     x=random.randint(0,7)
                                     y=random.choice((list(range(0,y))) + (list(range(y+1,5))))
                                     a=free[y][x]    
                                     free[k][g]=a
                                     free[y][x]=i
                                else:
                                    continue"""
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
    print(cons)
    return cons
    
   

    
tablemaker()

def finaltable():
    teachs={}
    teachsec={}
    cons=tablemaker()
    for w in teach:
        for e in teach[w]:
            temp=[]
            for q in sec:
                if sec[q][w]==e :
                  temp.append(q)
                  teachs[e]=temp
                  t=teachs.copy()
                  teachsec[w]=t
        teachs.clear()
    
    for i in cons:
        for j in cons[i]:
            continue




def sqlinserter():
    
    import mysql.connector
    
    cons=tablemaker()
    
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
    
        
        for k in cons[n]:
            mycursor = mydb.cursor()
            d="insert into "+n+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(d,k)
            mydb.commit()
    for i in mycursor:
        print(i)
    
    mydb1 =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ayush0510",
    database="teacher"
    )
    mycursor = mydb1.cursor()
    
    for n in sec:
        
        r="create table "+n+"(subject varchar(15),teacher varchar(12))"
        print(r)
        mycursor.execute(r)
        for k in sec[n]:
            y=sec[n][k]
            l=[k,y]
           
            mycursor = mydb1.cursor()
            d="insert into "+n+" values(%s,%s)"
            mycursor.execute(d,l)
            mydb.commit()
            print('executed')
    
    
    
#sqlinserter()    
      


"""
app=QtWidgets.QApplication([])
sec={'xi':1}
for i in sec:
    call4=uic.loadUi("table.ui")
    call4.secname.setText(i)
    call4.teachers.setRowCount(7)
    call4.show() 
    app.exec()
"""







