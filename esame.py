from datetime import datetime
import os

class ExamException(Exception):
    pass

    
class CSVFile():

    def __init__(self, name):   
        #controllo che l'input sia una stringa
        if isinstance(name,str):
            self.name = name
        else:
            raise ExamException(f"Error! File name should be string --> name = {name}, name_type = {type(name)}")
        
        #creo un attributo che conterrà i nomi delle colonne
        self.headers_list = []
       
    def get_data(self):

        #Controllo che il file esista
        if not os.access(self.name, os.F_OK):
            raise ExamException(f"Error! File '{self.name}' could not be found.")
        #Controllo che il file possa essere letto
        if not os.access(self.name, os.R_OK):
            raise ExamException(f"Error! File '{self.name}' could not be read.")
        #Controllo che il file non sia vuoto
        if os.stat(self.name).st_size == 0:
            raise ExamException(f"Error! File '{self.name}' is empty.")

        # Inizializzo una lista vuota per salvare tutti i dati
        data = []
    
        # Apro il file in lettura
        my_file = open(self.name, 'r')

        # Leggo il file linea per linea 
        for i ,line in enumerate(my_file):

            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
                
            # Pulisco il carattere (rimuovo newline e spazi bianchi)
            elements[-1] = elements[-1].strip()
                 
            # Aggiungo alla lista gli elementi di questa linea     
            data.append(elements)
        
        #Se la lista 'data' ha almeno un elemento
        #Il primo elemento sarà l'elenco dei nomi delle colonne
        if len(data) > 1:
            self.headers_list = data.pop(0)
        else:
            raise ExamException(f"Error! File '{self.name}' does not contain values.")
        
        # Chiudo il file
        my_file.close() 
        # Quando ho processato tutte le righe, ritorno i dati
        return data


class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        #Creo una lista con i nomi delle colonne che  mi interssano
        columns_list = ['date','passengers']

        # Chiamo la get_data del genitore 
        string_data = super().get_data()

        for column in columns_list:
        #Controllo che le colonne siano presenti nel file
            if not column in self.headers_list:
                raise ExamException(f"Error! Column '{column}' in '{self.name}' file could not be found")
            #Controllo che non ci siano colonne con lo stesso nome
            elif self.headers_list.count(column) > 1:
                raise ExamException(f"Error! There are {self.headers_list.count(column)} columns named '{column}'")
        
        #Assegno la posizione alle due colonne
        date_column = self.headers_list.index('date')
        passengers_column = self.headers_list.index('passengers')
            
        # Utilizzo la funzione 'create_time_series'
        #ottengo una time series in formato (datetime.date, int)
        converted_data = create_time_series(string_data,date_column,passengers_column)

        #Trasformo i datetime in stringhe
        final_list = [[element[0].strftime('%Y-%m'),element[1]] for element in converted_data]

        return final_list

def compute_avg_monthly_difference(time_series,first_year,last_year):

    #controllo che le date siano in formato stringa
    if not isinstance(first_year,str):
        raise ExamException(f"Error! first_year should be string --> first_year = {first_year}, first_year = {type(first_year)}")

    if not isinstance(last_year,str):
        raise ExamException(f"Error! last_year should be string --> last_year = {last_year}, last_year = {type(last_year)}")
    
    #controllo se è possibile converitrli in iteri
    is_convertible = True
    try:
        first_y = int(first_year)
        last_y = int(last_year)
    except: 
        is_convertible = False

    if not is_convertible:
        raise ExamException(f'Error! Input years could not be converted into int --> first_year = {first_year} , last_year ={last_year}')
    #controllo che first_y sia minore di last_y
    elif first_y >= last_y:
        raise ExamException(f"Error! Invalid range --> Expected value: first_year < last_year")
    #controllo che entrambi siano positivi
    elif first_y < 0 or last_y <0:
        raise ExamException(f"Error! Invalid value --> Expected value: input years > 0")

    #preparo la lista e faccio i vari controlli 
    prepare_list = create_time_series(time_series)
    

    #Creo una lista con gli anni compresi tra first_year e last_year
    my_list = [item for item in prepare_list if item[0].year >= first_y and item[0].year <= last_y]
    
    #controllo che ci sia almeno un valore nella lista
    if len(my_list) == 0:
        raise ExamException(f'There are no values in the selected range {first_y} < date < {last_y}')

    #Controllo che last_year e first_year siano nella lista
    if first_y != my_list[0][0].year:
        raise ExamException(f'First_year is not in list')

    if last_y != my_list[-1][0].year:
        raise ExamException(f'Last_year is not in list')

    #Preparo lista per contenere le medie
    avg = []
    
    #Per ogni mese
    for i in range(12):
        # Preparo lista per ragruppare i dati per mese
        groupbymonth = []
        #Preparo lista per contenere le differenze
        differences = []
        for item in my_list:
            #Se il mese dell'elemento corrisponde al mese corrente
            if item[0].month == i+1:
                #aggiungo l'elemnto nella lista mensile
                groupbymonth.append(item)
        
        #Se contiene meno di due mesi allora avg = 0
        if len(groupbymonth) < 2:
            avg.append(0.0)
        else:
            #per ogni elemento della lista mensile
            for j in range(len(groupbymonth)-1):
                #se sono due anni consecutivi
                if(groupbymonth[j+1][0].year == groupbymonth[j][0].year+1):
                    #faccio la differnfa del numero dei passeggeri
                    diff = groupbymonth[j+1][1]-groupbymonth[j][1]
                    differences.append(diff)

            #se c'è solo una differenza
            if (len(differences)==1):
                avg_month = differences[0]
                print(avg_month)
            #se ci sono più differenze faccio la media
            elif (len(differences)>1):
                avg_month = sum(differences)/len(differences)
            else:
            #altirmenti la media sarà 0
               avg_month = 0.0
           
            #inserisco la media del mese nella lista finale
            avg.append(float(avg_month))
            #elimino i dati dentro le liste provvisorie per fare i calcoli per il mese successivo
   
    return avg


def create_time_series (starting_list, date_column=0, value_column=1):

    time_series = []
    value_type_isok = True
    date_type_str_isok = True

    #controllo che time_series sia una lista 
    if not isinstance(starting_list,list):
        raise ExamException(f"Error! starting_list should be a list --> name = {starting_list}, name_type = {type(starting_list)}")

    #controllo che la lista non sia vuota
    if len(starting_list)==0:
        raise ExamException(f"Error! starting_list is empty")
    
    #Per ogni riga controllo
    for row in starting_list:
        #che la riga sia una lista
        if not isinstance(row,list):
            raise ExamException(f"Error! starting_list should be a list of lists --> starting_list elements type = {type(row)}") 
    
    #controllo che le posizioe delle colonne sia un numero intero
    if not isinstance(date_column,int):
        raise ExamException(f"Error! column_date position value should be integer")

    if not isinstance(value_column,int):
        raise ExamException(f"Error! column_value position should be integer")

    #controllo che siano due colonne distinte
    if date_column == value_column:
        raise ExamException(f"Error! Date_column and value_column have the same position")

    if date_column <0 or value_column <0:
        raise ExamException(f"Error! Columns position value should be positive")
    
    #controllo se tutti i valori sono interi
    value_type_isok = all(isinstance(row[1],int) and row[1]>0 for row in starting_list)
    
    #controllo se tutte le date sono nel formatto corretto
    try:
        date_type_str_isok = all(datetime.strptime(row[0], '%Y-%m').date() for row in starting_list)
    except Exception:
        date_type_str_isok = False
    
    #se gli elementi sono già nel formato giusto 
    if value_type_isok and date_type_str_isok:
        #e la lista è oridnata
        if not all(starting_list[i][0]<=starting_list[i+1][0]for i in range(len(starting_list)-1)):
            raise ExamException(f"List is not sorted")
        else:
            time_series = [[datetime.strptime(element[0],'%Y-%m'),element[1]] for element in starting_list]
            #ritorno la lista così come sta:
            return time_series
    #altrimenti:
    else:
        for row in starting_list:
            # Preparo una lista di supporto per salvare la riga
            converted_row = []
    
            # Ciclo su tutti gli elementi della riga
            for i,element in enumerate(row):
                #Provo a converitre in datetime gli elementi della lista
                #in posizione date_column
                if i == date_column:

                    try:
                        converted_row.append(datetime.strptime(element, '%Y-%m').date())
                        #se ci sono già degli elementi    
                    except Exception:
                        break
                #Provo a converitre in int gli elementi della lista
                #in posizione passengers_column    
                elif i == value_column:
                    try:
                        value = int(element)
                        #aggiungo il valore alla lista solo se >=0
                        if value >= 0:
                            converted_row.append(value)
                    except Exception:
                        break

            if len(converted_row) == 2:
            #Se la lista contine già dei dati
                if len(time_series)>1:
                #controllo che siano oridnati
                    if (converted_row[0]<=time_series[-1][0]):
                        raise ExamException (f"List is not sorted --> {time_series[-1][0]},{converted_row[0]} ")

                time_series.append(converted_row) 
         
    return time_series
    


#==============================
#  Corpo del programma
#==============================

#input value
file_name = 'data.csv'
first_year = '1949'
last_year = '1954'

time_series_file = CSVTimeSeriesFile(name=file_name)
time_series = time_series_file.get_data()
avg=compute_avg_monthly_difference(time_series, first_year, last_year)

print(f"Variazione media del numero di passeggeri per ogni mese: (periodo {first_year} - {last_year}")
print(avg)
