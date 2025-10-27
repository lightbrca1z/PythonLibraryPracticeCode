from texttable import Texttable

def main():

	table = Texttable()

	#アライメント：左寄せ/右寄せ/センタリング
	table.set_cols_align(["1","r","c"])

	#縦方向の位置設定
	table.set_cols_valign(["t","m","b"])

	# table.set_deco(Texttable.HEADER)
	# table.set_deco(Texttable.BORDER)
	# table.set_deco(Texttable.HLINES)
	table.set_deco(Texttable.VLINES|Texttable.HEADER)


	table.add_rows([
	["Name", "Age", "Nickname"],
	["Mr\nXavier\nHuon", 32, "Xav"],
	["Mr\nBaptiste\nClement", 32, "Baby"],
	["Mme\nLouise\nBourgeau", 28, "Lou\n\nLoue"]
	])


	print(table.draw() + "\n")

if __name__ == '__main__':
	main()