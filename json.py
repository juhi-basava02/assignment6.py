
import json
class Employee:
    def _init_(self):
        self.emp_dic={}
    def creat_JSON(self):
        for i in range(5):
            name = input("Enter your name: ")
            dob = input('Enter your DOB: ')
            height = input('Enter your height: ')
            city = input('Enter your city: ')
            state = input('Enter your state: ')
            emp={'name':name,'dob':dob,'height':height,'city':city,'state':state}
            emp_id = len(self.emp_dic)+1
            self.emp_dic[emp_id]=emp
        with open("emps.json",'w') as f:
            json.dump(self.emp_dic,f)

    def data_print(self):
        with open("emps.json","r") as f:
             data = json.load(f)
        for i in data.values():
            l1 = []
            l1.append(i)
            print(l1)   

x =Employee()            
x.creat_JSON()
print("--------------------------------------------------")
x.data_print()

import json
class State_Capital:
    def _init_(self):
        self.st_cap={}
    def creat_JSON(self):
        for i in range(7):
            s_name = input("Enter state name: ")
            c_name = input("Enter capital name: ")
            print("-------------------")
            SC_dict={s_name:c_name}
            self.st_cap.update(SC_dict)
        with open("state_capital.json",'w') as f:
            json.dump(self.st_cap,f)

    def print_JSON(self):
        with open("state_capital.json",'r') as f:  
            data = json.load(f)
        for i,j in data.items():
            print('State:'+ i + '  Capital:'+ j)  

x = State_Capital()
x.creat_JSON()
x.print_JSON()                