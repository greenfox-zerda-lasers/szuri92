import csv
import sys

class ToDoApp:

    def __init__(self):
            self.file_name = 'C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-05/day-5/tasks.csv'
            self.mode = sys.argv
            self.loop()

    def file_opener(self, permission):
        try:
            f = open(self.file_name, permission)
        except FileNotFoundError:
            f = open(self.file_name, 'a')
        return f
    def csv_to_list(self):
            f = self.file_opener('r')
            csv_f = csv.reader(f, delimiter = ';')
            lista = list(csv_f)
            f.close
            return lista

    def csv_delete(self):
        f = self.file_opener('w')
        csv_w = csv.writer(f)
        f.close()

    def write_task(self, a_task):
        f = self.file_opener('a')
        lista = ['doing']
        lista.append(a_task)
        writer = csv.writer(f, delimiter=';', lineterminator ='\n')
        writer.writerow(lista)
        f.close()

    def read_list(self):
        f = self.file_opener('r')
        csv_f = csv.reader(f, delimiter = ';')
        lista = list(csv_f)
        if len(lista) <= 0:
            print('No todos toady! :)')
        for i in range(len(lista)):
            if lista[i][0] == 'done':
                print( str( i + 1 ) + ' - [X] ' + lista[i][1])
            else:
                print( str( i + 1 ) + ' - [ ] ' + lista[i][1])


    def delete(self, number):
        lista = self.csv_to_list()
        lista.remove(lista[number-1])
        self.csv_delete()
        c = self.file_opener('a')
        csv_a = csv.writer(c, delimiter =';', lineterminator = '\n')
        for i in range(len(lista)):
            csv_a.writerow(lista[i])
        c.close()

    def check_task(self, number):
        lista = self.csv_to_list()
        self.csv_delete()
        for i in range(len(lista)):
            if i == number-1:
                lista[i][0] = 'done'
        c = self.file_opener('a')
        csv_a = csv.writer(c, delimiter =';', lineterminator = '\n')
        for i in range(len(lista)):
            csv_a.writerow(lista[i])
        c.close()
##### FILEFUNCTIONS ABOVE

    def loop(self):
        if len(self.mode) <= 1:
            print('Python Todo application')
            print('=======================\n')
            print('Command line arguments:')
            print(' -l   Lists all the tasks')
            print(' -a   Adds a new task')
            print(' -r   Removes an task')
            print(' -c   Completes an task')
        elif len(self.mode) == 2:
            if self.mode[1] == '-l':
                self.read_list()
            elif self.mode[1] == '-a':
                print('Unable to add: No task is provided')
            elif self.mode[1] == '-r':
                print('Unable to remove: No index is provided')
            elif self.mode[1] == '-c':
                print('Unable to check: No index is provided')
            else:
                print('Unsupported argument')
        elif len(self.mode) == 3:
            if self.mode[1] == '-a' and self.mode[2] !='':
                self.write_task(self.mode[2])
            elif self.mode[1] == '-r' and self.mode[2] !='':
                try:
                    self.delete(int(self.mode[2]))
                except ValueError:
                    print('Unable to remove: Index is not a number')
            elif self.mode[1] == '-c' and self.mode[2] !='':
                try:
                    self.check_task(int(self.mode[2]))
                except ValueError:
                    print('Unable to check: Index is not a number')



valami = ToDoApp()
