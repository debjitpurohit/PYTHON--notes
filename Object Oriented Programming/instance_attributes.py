class Employee:
    company ="Google"
    location ="gurgaon"

debu = Employee()
guru = Employee()
print(debu.company)
print(debu.location)

#-->changing object atributs
guru.company ="YouTube" 
guru.location ="NewYork"
print(guru.company)
print(guru.location)

#-->changing class atributs
debu.company ="Microsoft"
debu.location = "Bangalore"
print(debu.company)
print(debu.location)