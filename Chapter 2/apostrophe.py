message = "This is gonna be John's."
print(message)

#message = 'This is gonna be John's'
#print(message)
# can't use single quotes if there is an apostrophe

#2-3 Personal Message
name = "Tiff"
print("Hello " + name + ", would you like to learn some Python today?")

#2-4 Name Cases
name = "Tiffany"
print(name.title())
print(name.upper())
print(name.lower())

#2-5/2-6 Famous Quote
famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anyhting new."

print(famous_person + ' once said, "' + message + '"')

#2-7 Stripping Names
person = ' Jonny Phan '
print(person)
print("\t" + person)
print("\n" + person)

print(person.rstrip())
print(person.lstrip())
print(person.strip())
