import prettytable

def main():

	with open('data.csv', 'r') as file:
		table = prettytable.from_csv(file)

		print(table)

	table.sortby = 'Lot'
	table.reversesort = True

	print(table)

	return

if __name__ == '__main__':
    main()
