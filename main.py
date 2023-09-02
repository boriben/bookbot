file = "books/frankenstein.txt"
with open(file) as f:
    file_contents = f.read()
    
    #print(file_contents)
    
def num_words(string):
    return len(file_contents.split())

def num_chars(string):
    return {char: string.count(char) for char in set(string.lower())} # set makes this way faster!
    
def print_report(string):
    print(f"--- Begin report of {file} ---")
    print(num_words(string), "words found in the document")
    print()
    char_counts = num_chars(string)
    for char, count in sorted(char_counts.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

# print(num_words(file_contents))
# print(num_chars(file_contents))
print_report(file_contents)



