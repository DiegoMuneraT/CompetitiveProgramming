def firstWay():
    text = open("ArchivoTXT/wordRepetition.txt", "r") 
    d = dict()  # Dictionary

    for line in text:  # Loop through each word

        line = line.strip()  # Remove spaces and newline char
        line = line.lower()  # Lowercase to avoid mismatch
        words = line.split(" ")  # Split into words
        for word in words:  # Loop over each word
            if word in d:  # Check if the word in dict
                d[word] = d[word] + 1  # Add 1 match to the count
            else:
                d[word] = 1  # Add word to dict with 1 match

    for key in list(d.keys()):
        print(key, ":", d[key])
def secondWay():
    text = 'Banana strawberry grapes kiwi mango apple pear pear mango banana kiwi'
    d = dict()  # Create dictionary
    text = text.strip()  # Remove leading spaces
    text = text.lower()  # Lowercase to avoid mismatch
    text = text.split(" ")  # Split text into a list of words
    for word in text:  # Get each word of text
        if word in d:  # If word in dictionary
            d[word] = d[word] + 1  # Increment count
        else:
            d[word] = 1  # If word not in dictionary, add it with 1 match
    for key in list(d.keys()):  # Print content of dictionary
        print(key, ":", d[key])
print("First way: ")
#firstWay()
print("\nSecond Way: ")
secondWay()
