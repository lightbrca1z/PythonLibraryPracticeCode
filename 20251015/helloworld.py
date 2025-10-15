from prettytable import PrettyTable

print('hello world')

def main():
    table = PrettyTable()

    table.add_column('Serial Number',
                     ['P1214', 'E9545', 'N9545'])

    table.add_column('Product Name',
                     ['Pencil', 'Eraser', 'Notebook'])

    table.add_column('Lot',
                     ['100', '150', '200'])

    table.sortby = 'Lot'
    table.reversesort = True

    print(table)

if __name__ == '__main__':
    main()
