def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        pass # pass operator allows the exception to occur without giving a message
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['Chapter 10 - Files and Exceptions/no_file.txt','Chapter 10 - Files and Exceptions/programming.txt' , 'Chapter 10 - Files and Exceptions/pi_digits.txt']

for file in filenames:
    count_words(file)
