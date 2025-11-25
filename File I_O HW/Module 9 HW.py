#This program prints a poem in one file
#and the reverse of the poem in a different file

import os
print(os.path.join('folder', 'poem.txt')) #print statements are to ensure that the code was done correctly
print(os.path.abspath('docs/poem.txt'))
print(os.getcwd())

records = []
'''
This function runs the whole program
'''
def main():
    with open('docs/poem.txt','r') as f: #opens the poem.txt file
        for line in f:
            line = line.strip()
            print(line)

    '''
    Writes the lines for the poem.
    '''
    with open('docs/poem.txt','a') as f:
        f.write('\n"The Road Not Taken" By: Robert Frost\n\n')
        f.write('Two roads diverged in a yellow wood,\n')
        f.write('And sorry I could not travel both\n')
        f.write('And be one traveler, long I stood\n')
        f.write('And looked down one as far as I could\n')
        f.write('To where it bent in the undergrowth;\n\n')
        f.write('Then took the other, as just as fair,\n')
        f.write('And having perhaps the better claim,\n')
        f.write('Because it was grassy and wanted wear;\n')
        f.write('Though as for that the passing there\n')
        f.write('Had worn them really about the same,\n\n')
        f.write('And both that morning equally lay\n')
        f.write('In leaves no step had trodden black.\n')
        f.write('Oh, I kept the first for another day!\n')
        f.write('Yet knowing how way leads on to way,\n')
        f.write('I doubted if I should ever come back.\n\n')
        f.write('I shall be telling this with a sigh\n')
        f.write('Somewhere ages and ages hence:\n')
        f.write('Two roads diverged in a wood, and I--\n')
        f.write('I took the one less traveled by,\n')
        f.write('And that has made all the difference.\n')

    '''
    Puts the poem into a list, as one line from the file. 
    '''
    with open('docs/poem.txt','r') as f: #
        for line in f:
            poem = line.strip()
            if poem != '':
                records.append(poem)
    print(records)
    for lines in reversed(records): #reverses the list of the poem
        print(lines)

    with open('docs/poem2.txt', 'r') as f: #opens the poem2.txt file
        for line in f:
            line = line.strip()
            print(line)

    '''
    appends the reversed list of the poem into poem2.txt
    '''
    with open('docs/poem2.txt', 'a') as f:
        for r in records:
            f.write(r + '\n')

        f.write('\n\n"The Road Not Taken" by Robert Frost, is my favorite poem because of\n'
                'the last two lines of the poem, "I took the one less traveled by,/\n'
                'And that has made all the difference." The poem talks about a person\n'
                'who is in front of a crossroad in the woods, and instead of taking the\n'
                'road that everyone takes, he takes the one "less travelled by", showing\n'
                'that he does not do what everyone else does, rather "walks his own path".\n\n'
                'Esther Arazi')


if __name__ == '__main__':
    main()