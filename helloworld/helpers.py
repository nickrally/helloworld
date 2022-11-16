def readwrite(original, modified):
    with open(original, 'rb') as infile:
        with open(modified, 'wb') as outfile:
            for line in infile:
                outfile.write(line.upper())

def what_is(thing):
    print(f'What is this {thing} really?')