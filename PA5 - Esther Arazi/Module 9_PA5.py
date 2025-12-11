import os

DOCS_DIR = 'docs'
POEM_ORIGINAL = os.path.join(DOCS_DIR, 'poem_original.txt')
POEM_REMIX = os.path.join(DOCS_DIR, 'poem_remix.txt')

records = []

#—-------Main Program—--------
def main():

    """
       This program reads poem_original.txt and puts it into a list. It is then
       read, reversed, character and words are changed in the poem_remix.txt file,
       and writes to the poem_remix.txt file, with appropriate error handling.
    """

    try:
        #opens the poem_original.txt file and reads each line into the "records" list.
        with open(POEM_ORIGINAL, 'r', encoding = 'utf-8' ) as f: #(when I tried a different poem, the code
                                                                 # was having as issue hence the need for encoding)
            for line in f:
                line = line.strip()
                if line != '':
                    records.append(line) #adds the lines into "records" list
    except FileNotFoundError:
        print('Error: "poem_original.txt" file not found.')
        return

    try:
        #opens the poem_remix.txt file and reads it into a list.
        with open(POEM_REMIX, 'r') as f:
            for line in f:
                line = line.strip()
                print(line)
    except FileNotFoundError:
        print('Error: "poem_remix.txt" file not found.')
        return

    try:
        #writes the poem in the poem_remix.txt file.
        with open(POEM_REMIX, 'w') as f:
            reversed_lines = reversed(records) #reverse of the records list
            poem = '\n'.join(reversed_lines)   #.replace('roads', 'trails') - document the replacement
                                                # set and for loop to use one change = add the replace method
                                              # (I thought we had to do more than 1 word)
            replacements = {
                'roads': 'trails',              #list of changes
                'I': 'Me',
                '.': '!'
            }

            for old, new in replacements.items(): #replaces the words in the poem for the one in the set
               poem = poem.replace(old, new)

            f.write(poem) #prints the reversed and edited poem to screen
    except FileNotFoundError:
        print('Error: "poem_remix.txt" file not found.')

    # appends additional information to the "poem_remix.txt" file.
    try:
        with open(POEM_REMIX, 'a') as f:
            f.write('\n\n-------------------\n\n'
                    'Remixed By: Esther Arazi\n'
                    'I changed the word "roads" to "trails",'
                    ' "I" to "Me", and "." to "!" '
            )

    except FileNotFoundError:
            print('Error: "poem_remix.txt" file not found.')


if __name__ == '__main__':
    main()