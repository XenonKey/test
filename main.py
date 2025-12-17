from libs import *




# house17 = Building(1)
# house17.set_info('Pushkino', 51, 'URSTD')
# house17.get_info()
#
# school_865 = School(2)
# school_865.set_info('Chertanovo', 3405, 'Government')
# school_865.set_info(students = 553)
# school_865.get_info()
#
#
# a = UserLogging('Giorgi')
# a.log('Giorgi_1999', 12345678)


@timing
def mult_my_list(lst, x):
    """Умножает итерируемый объект на введенный аргумент"""
    new_list = []

    for i in lst:
        new_list.append(i * x)

    print(new_list)











