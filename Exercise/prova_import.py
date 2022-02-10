from ck import ListChecks, NumberChecks

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


#==============================
#  Corpo del programma
#==============================

#input value
my_list = [2,4,8,'ciao']
ratio = 0.5

diff = Diff()
result = diff.compute(my_list)
print(result)
