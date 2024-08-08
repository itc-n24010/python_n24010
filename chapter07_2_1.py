def list_del_nth(list, index):
    try:
        del list[index]
    except IndexError:
        print('Index Not Found')
    except:
        print('Unexpected Error')
    else:
        print('Successfully')

my_list = ['t', 'a', 'm', 'k', 'i']
list_del_nth(my_list, '2')
list_del_nth(my_list, 5)
list_del_nth(my_list, 0)

print(my_list)
