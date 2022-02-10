class MovingAverage:
    
    def __init__(self,window_size):

        if not isinstance(window_size, int):
            raise ExamException("Il valorede della finsestra deve esser un'intero")
        
        if window_size<1:
            raise ExamException("il valore della finiestra deve essere maggiore di 1")
            
        self.window_size = window_size
        
    def compute(self,numbers):
        if not isinstance(numbers, list):
            raise ExamException("L'input non è una lista") 

        if len(numbers) == 0:
            raise ExamException("La lista deve contenere almeno un elemento")

        if (len(numbers) < self.window_size):
            raise ExamException("La lunghezza della, lista deve essere maggiore del valore della finestra")

        for item in numbers:
            if not isinstance(item, (int,float)):
                raise ExamException("La lista contiene elementi con non sono numeri")
            
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
window_size = 2

moving_average = MovingAverage(window_size)
result = moving_average.compute(my_list)
print(result)

