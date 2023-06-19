person = {
    'firstname' : 'John',
    'lastname' : 'Doe',
    'age' : 25,
    'favorite_colors': ['blue', 'green'],
    'salary' : 5000
}
print(person)

print(person['age'])
person['salary'] = 15000
print(person)
person[12] ='test value'
person['Mobile'] = '0780633911'

#person.pop('favorite_colors')
print(person)

del person['salary']
print(person)

print(len(person))
print(person.values())

