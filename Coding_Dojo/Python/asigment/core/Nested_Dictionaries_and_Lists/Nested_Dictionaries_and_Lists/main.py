x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Part 1
x[1][0] = 15
print(x)

z[0]["y"] = 30
print(z)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = "andres"
print(sports_directory)

# Part 2
def iterateDictionary(students):
    while students:
        print(students)
        break
iterateDictionary(students)

# part 3 - 1
def iterateDictionary2(students):
    while students:
        first_name1 = students[0]['first_name']
        first_name2 = students[1]['first_name']
        print(first_name1, first_name2)
        break
iterateDictionary2(students)

# part 3 - 2
def iterateDictionary3(students):
    while students:
        last_name1 = students[0]['last_name']
        last_name2 = students[1]['last_name']
        print(last_name1, last_name2)
        break
iterateDictionary3(students)

# part 4
def printinfo(dict):
    for key,val in dict.items():
        print(f"{len(val)} {key.upper}")
        for i in range(0,len.val):
            print(val[i])


dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(dojo)
