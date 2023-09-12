# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


given_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print("original list:", given_list)
sorted_list = []

for i in range(len(given_list)):
    for j in range(i + 1, len(given_list)):

        if given_list[i][-1] > given_list[j][-1]:
            given_list[i], given_list[j] = given_list[j],given_list[i]


print("Sorted list:", given_list)



   
