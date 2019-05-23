from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['john'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['jeff'] = 'ruby'
favorite_languages['beth'] = 'c++'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title())