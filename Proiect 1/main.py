# Tema 2

# Exercitiul_1: Să se scrie o funcție care primește un număr nedefinit de parametrii și
#               să se calculeze suma parametrilor care reprezintă numere întregi sau reale.
# >> your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 -3)
# >> your_function() va returna 0
# >> your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4)

# Exercitiul_2: Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# >> suma tuturor numerelor de la [0, n]
# >> suma numerelor pare de la [0, n]
# >> suma numerelor impare de la [0. n]

# Exercitiul_3: Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta
#               este un număr întreg, altfel returnează valoarea 0.

#-------------------------------------------------------------------------
print('Tema 2 (nu se pune deoarece am facut-o dupa ce s-a rezolvat la curs)')

print ('Exercitiul 1:')
def my_function1 (*args, **kwargs):
    my_sum1 = 0
    for my_value1 in args:
        if type(my_value1) == int or type(my_value1) == float:
            my_sum1 += my_value1
    return my_sum1
print(my_function1(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function1())
print(my_function1(2, 4, 'abc', param_1=2))

#-------------------------------------------------------------------------
print ('Exercitiul 2:')

def my_function2(n):
    if n == 0:
        return 0, 0, 0

    total, even, odd = my_function2(n-1)
    total += n

    if n % 2 == 0:
        even += n
    else:
        odd += n

    return total, even, odd

sum_total, sum_even, sum_odd = my_function2(5)
print('total = ', sum_total)
print('even = ', sum_even)
print('odd = ', sum_odd)

#-------------------------------------------------------------------------
print ('Exercitiul 3:')

def my_function3():
    x = input('>>')

    try:
        x = int(x)
    except ValueError:
        x = 0

    return x

print(my_function3())

print('End of Homework')