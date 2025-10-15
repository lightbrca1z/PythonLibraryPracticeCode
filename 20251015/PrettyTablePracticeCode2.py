from prettytable import PrettyTable

print('hello world')

def main():
    table = PrettyTable(
    	['Serial Number', 'Product Name', 'Lot'])

    table.add_row(['P1214', 'Pencil', '100'])
    table.add_row(['E9545', 'Eraser', '150'])
    table.add_row(['N7811', 'Notebook', '200'])

    table.align['Serial Number'] = '1'
    table.padding_width = 2

    print(table)

if __name__ == '__main__':
    main()
