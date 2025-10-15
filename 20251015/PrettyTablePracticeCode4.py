from prettytable import from_html_one

def main():

	with open("data.html", "r") as file:
		html = file.read()
	
	table = from_html_one(html)
	print(table)
	
	return

if __name__ == '__main__':
    main()
