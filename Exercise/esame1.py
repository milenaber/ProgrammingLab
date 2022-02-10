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
            if not (isinstance(item,(int,float))):
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
        if not (isinstance(self.obj,(int,float))):
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

class Operation:
    def __init__(self,*args,**kwargs):
       raise NotImplementedError()

    def Compute(self,*args,**kwargs):
        raise NotImplementedError()

    def check_isinteger(number):
        if not (isinstance(self.obj,int)):
             raise ExamException(f"Errore! Non è un intero -->")


class MovingAverage(Operation):
    
    def __init__(self,window_size):

        ws = NumberChecks(window_size,'finestra')
        #check_isinteger(window_size)
        self.check_isinteger(window_size)
        ws.isnotlessthen(1)
        self.window_size = window_size
        
    def compute(self,numbers):
        mylist = ListChecks(numbers)

        if (mylist.isnotempthy() and mylist.isnotshorterthen(self.window_size) and mylist.iscontainignumbers()):
                i = 0
                moving_averages = []
                while i < len(numbers) - self.window_size + 1:
                    this_window = numbers[i : i + self.window_size]
                    window_average = sum(this_window) / self.window_size
                    moving_averages.append(window_average)
                    i += 1

                return moving_averages
       

class ExamException(Exception):
    pass

#==============================
#  Corpo del programma
#==============================

#input value
my_list = [7,8,9,10]
window_size = 4

moving_average = MovingAverage(window_size)
result = moving_average.compute(my_list)
print(result)

