def split_into_words(lines):
    words = []
    for line in lines:
        words.extend(word.strip(".,!?") for word in line.split())
    return words
