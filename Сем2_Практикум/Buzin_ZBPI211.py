# 1
def fact(x):
    if type(x) == int:
        if x == 0:
            return fact(1)
        elif x == 1:
            return x
        elif x > 1:
            return x * fact(x-1)
        else:
            return print('Введите целое неотрицательное число')
    else:
        return print('Введите целое неотрицательное число')


# 2
def filter_even(li):
    if type(li) == list:
        for i in li:
            if type(i) == int:
                pass
            else:
                return print('Введите список целых чисел')
        return list(filter(lambda x: x%2 == 0, li))
    else:
        return print('Введите список целых чисел')


# 3
def square(li):
    if type(li) == list:
        for i in li:
            if type(i) == int:
                pass
            else:
                return print('Введите список целых чисел')
        return list(map(lambda x: x**2, li))
    else:
        return print('Введите список целых чисел')


# 4
def bin_search(li, element):
    if type(li) == list:
        if len(set([type(i) for i in li])) == 1 and li == sorted(li):
            for num, i in enumerate(sorted(li)):
                if i == element:
                    return num
            return -1
        else:
            return print('Введите отсортированный список элементов и элемент')
    else:
        return print('Введите отсортированный список элементов и элемент')


# 5
def is_palindrome(string):
    if type(string) == str:
        cnt = 0
        string =  "".join(i for i in string.lower() if i.isalpha())
        for i in range(len(string)//2):
            if string[i] == string[len(string) - i - 1]:
                cnt+=1
            else:
                return print('NO')
        if cnt == len(string)//2:
            return print('YES')
        else:
            return print('NO')
    else:
        return print('Введите строку')


# 6
def calculate(path2file):
    if type(path2file) == str:
        with open(path2file) as f:
            string = f.readlines()
            ll = []
            for i in string:
                a = i.split()[0]
                b = i.split()[1]
                c = i.split()[2]
                if type(int(b)) == int and type(int(c)) == int:
                    if a == '//':
                        if int(b) > 0 and int(c) > 0:
                            ll.append(eval(b+a+c))
                        else: return print(f'Для операции {a, b, c} подаются только положительные числа')
                    elif a == '%':
                        if int(b) > 0 and int(c) > 0:
                            ll.append(eval(b+a+c))
                        else: return print(f'Для операции {a, b, c} подаются только положительные числа')
                    elif a == '**':
                        if int(b) >= 0 and int(c) >= 0:
                            ll.append(eval(b+a+c))
                        else: return print(f'Для операции {a, b, c} подаются только положительные числа')
                    else:
                        ll.append(eval(b+a+c))
                else:
                    return print('Входные числа должны быть целыми')

            return ",".join(map(str, ll))
    else:
        return print('Введите строку с названием файла')
    


# 7
def substring_slice(path2file_1, path2file_2):
    if type(path2file_1) == str and type(path2file_2) == str:
        with open(path2file_1) as f1, \
             open(path2file_2) as f2:
            a = f1.readlines()
            b = f2.readlines()
        if len(a) == len(b):
            ll = []
            for i, j in zip(b, a):
                c = int(i.split()[0])
                d = int(i.split()[1]) + 1
                ll.append(j[c:d])
            return (" ".join(map(str, ll)))
        else:
            return print('В файлах разное количество строк')
    else:
        return print('Введите строки с названиями файлов')
    

# 8
import json
periodic_table = json.load(open('periodic_table.json'))
def decode_ch(string_of_elements): 
    if type(string_of_elements) == str and len(string_of_elements) == len("".join(i for i in string_of_elements if i.isalpha())):
        ll = []
        for i in string_of_elements:
            for j, k in periodic_table.items():
                if i == j:
                    ll.append(k)
        return ("".join(map(str, ll))) 
    else:
        return print('Введите строку химических символов без пробелов')


# 9
class Student:
    def __init__(self, name, surname, grades = [3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = self.name + ' ' + self.surname
        self.grades = grades
        
    def greeting(self):
        return 'Hello, I am Student'
 
    def mean_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return 'YES'
        else:
            return 'NO'
        
    def __add__(self, other):
        return self.name + ' is friends with ' + other.name
    
    def print(self):
        return print(self.fullname)
        

# 10
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
       