favorite_languages = {
    'john' : 'python',
    'bob' : 'c++',
    'jen' : 'java'
}

print("John's favorite language is " + 
    favorite_languages['john'].capitalize() +
    ".")

# looping through key-value pairs
for key, value in favorite_languages.items():
    print("Key: " + key)
    print("Value: " + value + "\n")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + "\n")

for name in favorite_languages:
    print(name.title())

#loop through sorted keys
for name in sorted(favorite_languages):
    print(name.title())

#loop through values
print("\n\nThe following languages have been mentioned:") 
for language in sorted(favorite_languages.values()):    
    print(language.title())
