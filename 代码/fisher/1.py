tup = (1, 2, [1, 1, 3])
tup[2].insert(0, 0)
tup[2][2] = 2
print(tup)

my_list = []
print('list_size', my_list.__sizeof__())
my_tuple = ()
print('tuple_size', my_tuple.__sizeof__())
for i in range(5):
    my_list.append(1)
    print('list_append_%d' % i, my_list.__sizeof__())
    my_tuple = tuple(my_list)
    print('tuple_append_%d' % i, my_tuple.__sizeof__())







