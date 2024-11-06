import string

def text_analysis(filename): # filename <my_textfile>.txt
    with open(filename, 'r') as file:
        text = file.read()

    #TODO: 1. Count the number of words

    #TODO: 2. Calculate the average word length

    #TODO: 3. Identify the most frequent words

    #TODO: 4. Remove all punctuation

    #TODO: 5. Convert the text to lowercase

    # print(f"Word count: {word_count}")
    # print(f"Average word length: {avg_word_length:.2f}")
    # print("Most frequent words:")
    # for word, count in most_common_words:
    #     print(f"{word}: {count}")
    # print("\nText without punctuation:")
    # print(text_without_punctuation)
    # print("\nText in lowercase:")
    # print(text_lowercase)

# Example usage:
filename = "data/task-02.txt"
text_analysis(filename)