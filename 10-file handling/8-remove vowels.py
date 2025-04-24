remove_words = {'a', 'an', 'the'}

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        cleaned_line = ' '.join([word for word in words if word.lower() not in remove_words])
        outfile.write(cleaned_line + '\n')

print("Words 'a', 'an', and 'the' removed. Cleaned text saved to 'output.txt'.")
