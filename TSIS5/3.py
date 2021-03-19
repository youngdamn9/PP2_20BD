def file_append(file_name):
    from itertools import islice
    with open('abc.txt', 'w') as f:
        f.write('Alan Saudabekov\n')
        f.write('KBTU: FIT\n')
        f.write('Alan Experience\n')
        f.write('Lepeshka Mayonez')
    txt = open(file_name)
    print(txt.read())

file_append('abc.txt')