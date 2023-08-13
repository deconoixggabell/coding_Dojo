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
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for i in range(0, len(list)-1):
        output = ""
        for key,val in list[i].items():
            output += f"{key} - {val},"
        print(output)

            # print(f" {'first_name'} - {'last_name'}")
iterateDictionary(students)

# part 3

def iterateDictionary2(key_name,list):
    for i in range(0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)
            
iterateDictionary2('first_name',students)
print(' ')
iterateDictionary2('last_name', students)

# part 4
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(dict):
    for key,val in dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])
printinfo(dojo)