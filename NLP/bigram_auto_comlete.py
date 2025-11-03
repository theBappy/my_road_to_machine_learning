import re

training_corpus = input(
    """
    Insert the training corpus here (can be multiline)
"""
)


def text_clean_and_tokenize(training_corpus):
    text = training_corpus.lower().split("\n")
    text = [re.sub("[^a-zA-Z0-9 -]", "", i) for i in text]
    text = ["<s> " + i + " </s>" for i in text]
    tokenized_text = " ".join(text).split()
    return tokenized_text


def auto_complete(starting_word, training_corpus):
    tokenized = text_clean_and_tokenize(training_corpus)
    max_freq = 0
    freq_dict = {}
    for i in range(len(tokenized)):
        if tokenized[i] == starting_word:
            if tokenized[i + 1] in freq_dict:
                freq_dict[tokenized[i + 1]] += 1
            else:
                freq_dict[tokenized[i + 1]] = 1

    max_prob_word = ""
    for i in freq_dict:
        if max_freq <= freq_dict[i]:
            max_freq = freq_dict[tokenized[i + 1]]
            max_prob_word = i
    return max_prob_word


if __name__ == "__main__":
    word = [input("Insert a word: ")]

    for i in range(6):
        word.append(auto_complete(word[i], training_corpus))

    print(" ".join(word))
