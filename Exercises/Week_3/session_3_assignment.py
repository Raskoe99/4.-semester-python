from operator import index
from re import A

#   Exercise 1
print()
print("Exercise 1: Organization model")
directors = ["Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"]
managers = ["Tine", "Trunte", "Rane"]
employees = ["Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"]

'''who in the board of directors is not an employee?
who in the board of directors is also an employee?
how many of the management is also member of the board?
All members of the managent also an employee
All members of the management also in the board?
Who is an employee, member of the management, and a member of the board?
Who of the employee is neither a memeber or the board or management?'''

setDirectors = set(directors)
setManagers = set(managers)
setEmployees = set(employees)

print("Part of board and not an employee: ", setDirectors.difference(setEmployees))
print("Part of board and an employee: ", setDirectors.intersection(setEmployees))
print("Part of management and the board: ", setManagers.intersection(setDirectors))
print("Part of management and an employee: ", setManagers.intersection(setEmployees))
print("Part of management, the board and an employee: ", setManagers.intersection(setDirectors.intersection(setEmployees)))
print("Employee, neither part of management nor the board: ", setEmployees.difference(setDirectors.difference(setManagers)))




print()


#   Exercise 2
print("Exercise 2: Dictionary to tuple")
dictPreTuple = {'a' : 'Alpha', 'b' : 'Beta', 'g' : 'Gamma'}
postTuple = [(k, v) for k, v in dictPreTuple.items()]
print("Finished tuple: ", postTuple)
print()

#   Exercise 3
print("Exercise 3: Set comparisons")
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

print ("Union: ", set1.union(set2))
print ("Symmetric difference: ", set1.symmetric_difference(set2))
print ("Difference: ", set2.difference(set1)) #Returns empty set if switched, due to set1 having no unique characters
print ("Disjoint: ", set1.intersection(set2))
print()

#   Exercise 4
print("Exercise 4: Date decoder")

def dateDecoder(dateString) :
    day = dateString[0:dateString.index("-")]
    month = dateString[dateString.index("-")+1:dateString.index("-",3):]
    year = dateString[dateString.index("-",3)+1:len(dateString)]

    if month == "JAN" :
        month = "January"
    if month == "FEB" :
        month = "February"
    if month == "MAR" :
        month = "March"      
    if month == "APR" :
        month = "April"
    if month == "MAY" :
        month = "May"    
    if month == "JUN" :
        month = "June"
    if month == "JUL" :
        month = "July"
    if month == "AUG" :
        month = "August"
    if month == "SEP" :
        month = "September"
    if month == "OCT" :
        month = "October"
    if month == "NOV" :
        month = "November"
    if month == "DEC" :
        month = "December"
    
    year = "20" + year   # Gad ikke arbejde med date-objekter for at løse dette problem

    return [('day', day),('month', month), ('year', year)]

print(dateDecoder("12-OCT-05"))
