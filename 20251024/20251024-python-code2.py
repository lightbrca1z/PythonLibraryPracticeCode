from texttable import Texttable

def main():

	table = Texttable()

	table.set_deco(Texttable.VLINES|Texttable.HEADER)

	table.set_cols_dtype(['t','f','e','i','a'])

	table.set_cols_align(["l","r","r","r","l"])


	table.add_rows([
	["text", "float", "exp", "int", "auto"],
	["abcd", 67, 654, 89, 128.001],
	["efghijk", 67.5434, .654, 89.6, 128000.00023],
	["abcd", .023, 5e+78, 92., 1280000000]
	])

	print(table.draw())

if __name__ == '__main__':
	main()
