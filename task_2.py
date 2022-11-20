import csv
st_db=[]
with open("Student_marks_list.csv",'r') as file:
    csvreader = csv.reader(file)
    header=next(csvreader)
    for row in csvreader:
        st_db.append(row)


def top(p,subject):
    s=''
    p=int(p)
    max=0
    name=[]
    for i in st_db:
        if int(i[p])>int(max):
            max=i[p]
            name.clear()
            name.append(i[0] )
        elif int(i[p])==int(max):
            name.append(i[0] )
          
    if len(name)==1:
        print("Topper in",subject,"is",name[0])
        print()
    else:
        print("Topper in",subject,"are",end=' ')
        print(','.join(sorted([name for name in name ])))  
        print()
top(1,'Maths')            
top(2,'Biology')    
top(3,'English')    
top(4,'Physics')    
top(5,'Chemistry')
top(6,'Hindi')    


def average():
    avr=0
    al=[]
    name=[]
    for i in st_db:
        st=i[0]
        t_m=0
        for j in range(1,len(i)):
            t_m+=int(i[j])
        avr=t_m/6
        al.append([st,avr])
   
    first = sorted(set([avr for st, avr in al]))[-1]
    second= sorted(set([avr for st, avr in al]))[-2]
    third= sorted(set([avr for st, avr in al]))[-3]
    
    
  
    print("Best Students in the class are",end=" ")
    print("",','.join(sorted([st for st, avr in al if avr == first])),end=",")
    print(','.join(sorted([st for st, avr in al if avr == second])),end=",")
    print(','.join(sorted([st for st, avr in al if avr == third])),end=".")
    print()
average()


#BIG O NOTATION
#SPACE COMPLEXITY=0(N)
#TIME COMPEXITY=0(N)