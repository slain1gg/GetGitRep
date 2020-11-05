def get_lenght_mas(mas):
	lenght = 0
	if mas == []:
		return 0
	for index, i in enumerate(mas):
		lenght += index
	return lenght

a = []
print(get_lenght_mas(a))