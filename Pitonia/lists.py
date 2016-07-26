sample_list = ["3123", 23, 12, "gosho"];
sample_list[-1] = "changed last element"
print(sample_list)

for x, i in enumerate(sample_list):
	print(sample_list[x])

# #Blank matrix
def make_matrix(n):
	return [[0 for i in range(n)] for j in range(n)]

matrix = make_matrix(5)
matrix[-1] = 5
print(matrix)


tuple_1 = (1, 2, 3, 4)
tuple_2 = (3, 4, 2, 5)
tuple_combined = tuple_1 + tuple_2
print(tuple_combined)
del tuple_1, tuple_2
# print(tuple_2) will not work :)

simple_set = { "123", "123", 123, "asdasd"}
simple_set.add("added")
print(simple_set)
input("Pre...");