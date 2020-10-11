from myClasses import Psentense, Introduce

import os, time, csv

#FUNCTIONS 
def sleep(num):
    time.sleep(num)

def clear():
    os.system('clear')

#Get the name of the Csv File from the user 
psen = Psentense()

Introduce()


f_name = input("Enter the file name here => ")
clear()
f_name = str(f_name) + '.csv'


psen.printer('Csv File name is : %s\n' %f_name)


filed_names = []
#Get the field names from the user 

while True:
    try:
        qfield = int(input("Hey, How many fields do you want?!"))
        break
    except:
        print("invalid Data .")
        sleep(1)


for it in range(qfield):
    
    field_name = input("Enter Filed {} =>  ".format(it+1))
    filed_names.append(field_name)

clear()

#Cerate csv file with the fiven name in write mode 

file_content = [] #Create a list for adding field answer to it 

with open(f_name, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = filed_names)
    writer.writeheader()
                            #Get Two input for adding to the file and back to the first line 
    life_cycle = True                    
    while life_cycle == True:
        clear()
        file_content = []
        print("Enter exit for quiting the file ")
        for i in range(qfield):
            field_answer = input("Enter your answer for {} => ".format(filed_names[i]))
            if (field_answer.lower() == 'exit'):
                life_cycle = False
                break
            else:
                file_content.append(field_answer)
                                                    #After the for loop ended add the row to the file 
        zipped = zip(filed_names, file_content)
        writer.writerow({key:value for key, value in zipped}) 

    


clear()

print(" I created a file with name %s in the same diroctory."%f_name)
sleep(1.5)




