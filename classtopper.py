import csv
st_db=[]
with open("Student_marks_list.csv",'r') as file:
    csvreader = csv.reader(file)
    header=next(csvreader)
    top_three = {1:[],2:[],3:[]}
    top_in_all = {'Maths':[],'Biology':[],'English':[],'Physics':[],'Chemistry':[],'Hindi':[]}
    single_student_average = 0
    list_of_students =[]
    first = 0
    second  = 0
    third = 0
    Maths_top = 0
    Biology_top = 0
    English_top = 0
    Physics_top = 0
    Chemistry_top = 0 
    Hindi_top = 0
    
    for student_marks in csvreader:
        Maths= int(student_marks[1])
        Biology = int(student_marks[2])
        English = int(student_marks[3])
        Physics = int(student_marks[4])
        Chemistry =int(student_marks[5])
        Hindi =int(student_marks[6])
        
        if Maths > Maths_top:
            Maths_top = Maths
            list_of_students = []
            list_of_students.append(student_marks[0])
            top_in_all['Maths'] = list_of_students
        elif Maths == Maths_top:
            top_in_all['Maths'].append(student_marks[0]) 

        if Biology > Biology_top:
            Biology_top = Biology
            list_of_students = []
            list_of_students.append(student_marks[0])
            top_in_all['Biology'] = list_of_students
        elif Biology == Biology_top:
            top_in_all['Biology'].append(student_marks[0]) 

        if English > English_top:
            English_top = English
            list_of_students = []
            list_of_students.append(student_marks[0])
            top_in_all['English'] = list_of_students
        elif English == English_top:
            top_in_all['English'].append(student_marks[0]) 

        if Physics > Physics_top:
            Physics_top = Physics
            list_of_students = []
            list_of_students.append(student_marks[0])
            top_in_all['Physics'] = list_of_students
        elif Physics == Physics_top:
            top_in_all['Physics'].append(student_marks[0]) 

        if Chemistry > Chemistry_top:
            Chemistry_top = Chemistry
            list_of_students = []
            list_of_students.append(student_marks[0])
            top_in_all['Chemistry'] = list_of_students
        elif Chemistry == Chemistry_top:
            top_in_all['Chemistry'].append(student_marks[0]) 
        if Hindi > Hindi_top:
            Hindi_top = Hindi
            list_of_students = []
            list_of_students.append(student_marks[0])
            top_in_all['Hindi'] = list_of_students
        elif Hindi == Hindi_top:
            top_in_all['Hindi'].append(student_marks[0]) 

        single_student_total = 0
        single_student_average = Maths + Biology+English+Physics+Chemistry+Hindi / 6
        if single_student_average >= third:
            if single_student_average > third:
                if single_student_average >= second:
                    if single_student_average > second:
                        if single_student_average >= first:
                            if single_student_average > first:
                                first = single_student_average
                                list_of_students = []
                                list_of_students.append(student_marks[0])
                                top_three[1] = list_of_students
                          
                            else:
                                top_three[1].append(student_marks[0])  
                        else:
                            second = single_student_average
                            list_of_students = []
                            list_of_students.append(student_marks[0])
                            top_three[2] = list_of_students

                    else:
                     top_three[2].append(student_marks[0])
                        
                else:
                    third = single_student_average
                    list_of_students = []
                    list_of_students.append(student_marks[0])
                    top_three[3] =  list_of_students

            else:
                top_three[3].append(student_marks[0])
                   

if len(top_in_all['Maths']) ==1 :
    print("Topper in Maths is " + top_in_all['Maths'][0])
else:
    print("Topper in Maths are",end=' ')
    print(','.join(sorted([name for name in top_in_all['Maths'] ]))) 

if len(top_in_all['Biology']) ==1 :
    print("Topper in Biology is " + top_in_all['Biology'][0])
else:
    print("Topper in Biology are",end=' ')
    print(','.join(sorted([name for name in top_in_all['Biology'] ]))) 

if len(top_in_all['English']) ==1 :
    print("Topper in English is " + top_in_all['English'][0])
else:
    print("Topper in English are",end=' ')
    print(','.join(sorted([name for name in top_in_all['English'] ]))) 

if len(top_in_all['Physics']) ==1 :
    print("Topper in Physics is " + top_in_all['Physics'][0])
else:
    print("Topper in Physics are",end=' ')
    print(','.join(sorted([name for name in top_in_all['Physics'] ]))) 

if len(top_in_all['Chemistry']) ==1 :
    print("Topper in Chemistry is " + top_in_all['Chemistry'][0])
else:
    print("Topper in Chemistry are",end=' ')
    print(','.join(sorted([name for name in top_in_all['Chemistry'] ]))) 

if len(top_in_all['Hindi']) ==1 :
    print("Topper in Hindi is " + top_in_all['Hindi'][0])
else:
    print("Topper in Hindi are",end=' ')
    print(','.join(sorted([name for name in top_in_all['Hindi'] ]))) 

print("Best Students in the class are",end=" ")
print(','.join(sorted([name for name in top_three[1] ])),end=",") 
print(','.join(sorted([name for name in top_three[2] ])),end=",") 
print(','.join(sorted([name for name in top_three[3] ]))) 




#BIG O NOTATION
#SPACE COMPLEXITY=0(N)
#TIME COMPEXITY=0(N)