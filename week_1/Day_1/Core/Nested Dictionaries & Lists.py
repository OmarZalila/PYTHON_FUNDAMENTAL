# 1-Update Values in Dictionaries and Lists
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

x[1][0] = 15
print(x)
students[0]["last_name"]="Bryant"
print(students[0])
sports_directory["soccer"][0]="Andres"
print(sports_directory["soccer"])
z[0]["y"]=30
print(z)
# 2-Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list_students) :
    for x in range(len(list_students)):
        print(students[x])
iterateDictionary(students)
# 3-Get Values From a List of Dictionaries
def iterateDictionary2(key_name,list_student):
    for x in list_student:
        print(x[key_name])

iterateDictionary2("first_name", students)
# 4-Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict_Dojo):
    print(f"{len(dict_Dojo['locations'])} LOCATIONS")
    for location in dict_Dojo['locations']:
        print(location)
    print(f"{len(dict_Dojo['instructors'])} INSTRUCTORS")
    for instructor in dict_Dojo['instructors']:
        print(instructor)

printInfo(dojo)
