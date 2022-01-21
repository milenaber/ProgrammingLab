import math

#Verify if an item is a number
def isaNumber (item):
    if (isinstance(item, int) or isinstance(item, float)):
         return True
    else:
         return False

#Sum list elements if they are numbers, if the list contein 0 numbers return none
def sum_list (the_list):
    s = 0
    check = 0
    for item in the_list:
        if (isaNumber(item)):
            s = s + item
            check = check + 1
    if check > 0:
         return s
    else:
        return None
    

#Verify if list is containig only numbers
def isListContainigNumber (the_list):
    b= True
    for item in the_list:
        if (isaNumber(item)==False):
            b=False
            return b
    return b

#Print position and element of a list if it's not a number
def itemsandpos(the_list) :
    for i, item in enumerate(the_list):
         if (isaNumber(item)==False):
             print('{}-{}'.format(i+1,item))
          
#***Main***
my_list = [1,2,'ciao', math.pi, 3.5e2,6.7,'fgrg',None,'',.8,-9]

onlynumbers = isListContainigNumber (my_list)
tot = sum_list (my_list)

if tot is not None:
    print ('La somma dei numeri è: {}\n'.format(tot))
    if (onlynumbers == False):
        print('ATTENZIONE! I seguenti elementi non sono stati considerati per la somma:')
        itemsandpos(my_list)
else:
     print ('ATTENZIONE! La lista non contiene numeri')
     print ('Numero elelmenti lista: {}'.format(len(my_list)))


