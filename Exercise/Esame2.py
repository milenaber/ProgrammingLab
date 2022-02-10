class Checks:
    def __init__(self, obj, obj_name = 'input'):
        self.obj = obj
        self.obj_name = obj_name

    def isnotnone(self):
        if self.obj == None :
            raise ExamException(f"Errore! Valore nullo --> {obj_name}_value = {obj_name}")
        else:
            return True

class ListChecks(Checks):
    def __init__(self,my_list):
        if isinstance(my_list,list):
             self.my_list = my_list
        else:
            raise ExamException(f"Errore! L'input non è una lista --> input_value = {my_list}, input_type = {type(my_list)}")
    
    def isnotempthy(self):
        if len(self.my_list)==0:
             raise ExamException(f"Errore! La lista è vuota --> input_value = {my_list}")
        else:
            return True
  
    def iscontainignumbers(self):   
        for item in self.my_list:
            if not (isinstance(item,int,float)):
               raise ExamException("Errore! La lista non contiene solo numeri")

        return True

    def isnotshorterthen(self,min_len):
        if len(self.my_list)<min_len:
            raise ExamException(f"Errore! La lista è troppo corta --> list_lenght = {len(self.my_list)}. Expected value: list_lenght > {min_len}")
        else:
            return True

class NumberChecks(Checks):
    def isinteger(self):
        if not (isinstance(self.obj,int)):
             raise ExamException(f"Errore! Non è un intero -->{self.obj_name} = {self.obj} , Tipo var = {type(self.obj)}")
        else:
            return True
            
    def isinotanumber(self):
        if not (isinstance(self.obj,(int,float)):
             raise ExamException(f"Errore! Non è un numero --> {self.obj_name} = {self.obj} , Tipo var = {type(self.obj)}")
        else:
            return True
    
    def isnotgretaerthen(self,maxv):
        if self.obj>maxv:
             raise ExamException(f"Errore, valore troppo grande -->{self.obj_name} = {self.obj}. Expected value {self.obj_name} <{maxv}")
        else:
            return True
    
    def isnotlessthen(self,minv):
        if self.obj<minv:
             raise ExamException(f"Errore, valore troppo piccolo --> {self.obj_name} = {self.obj}. Expected {self.obj_name}>{minv}")
        else:
            return True
            
    def isnotequalto(self,val):
        if self.obj==val:
             raise ExamException(f"Errore, valore invalido --> {self.obj_name} = {self.obj}. Expected {self.obj_name}!={val}")
        else:
            return True

class Diff:

    #Return a list with the difference of list elments
    def __init__(self,ratio = 1):
        r = NumberChecks(ratio,'ratio')
        if (r.isinotanumber() and r.isnotequalto(0) and r.isnotlessthen(0)):
            self.ratio = ratio
        
    def compute(self,numbers):
        mylist = ListChecks(numbers)
        if (mylist.isnotempthy() and mylist.iscontainignumbers() and mylist.isnotshorterthen(2)):
            i = 0
            diff_list = []
            while i < len(numbers) - 1:
                sub_list = numbers[i : i + 2]
                difference = (sub_list[1] - sub_list[0])/self.ratio
                diff_list.append(difference)
                i += 1         

            return diff_list
                
class ExamException(Exception):
    pass

#==============================
#  Corpo del programma
#==============================

#input value
my_list = [1,2,4]
ratio = 0.5

diff = Diff(ratio)
result = diff.compute(my_list)
print(result)
