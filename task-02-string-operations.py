import string

def text_analysis(filename): # filename <my_textfile>.txt
    with open(filename, 'r') as file:
        text = file.read()

    #TODO: 1. Count the number of words
    words = text.split()
    word_count = len(words)

    #TODO: 2. Calculate the average word length
    total_length = sum(len(word) for word in words)
    avg_word_length = total_length / word_count

    #TODO: 3. Identify the most frequent words
    from collections import Counter
    word_counts = Counter(word.lower().strip(string.punctuation) for word in words)
    most_common_words = word_counts.most_common(10)

    #TODO: 4. Remove all punctuation
    text_without_punctuation = "".join(c for c in text if c not in string.punctuation)

    #TODO: 5. Convert the text to lowercase
    text_lowercase = text_without_punctuation.lower()

    print(f"Word count: {word_count}")
    print(f"Average word length: {avg_word_length:.2f}")
    print("Most frequent words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
    print("\nText without punctuation:")
    print(text_without_punctuation)
    print("\nText in lowercase:")
    print(text_lowercase)

# Example usage:
filename = "data/task-02.txt"
text_analysis(filename)