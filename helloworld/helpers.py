def readwrite(original, modified):
    with open(original, 'rb') as infile:
        with open(modified, 'wb') as outfile:
            for i, line in enumerate(infile):
                outfile.write(i + " " +line.upper())

def what_is(thing):
    print(f'What is this {thing} really?')