zenPython = 'This!,* is! test string with long string'
words = zenPython.split()
words = [x.strip("!,@#$%^&*").lower() for x in words]
unique_words = set(words)
word_frequency = {i:words.count(i) for i in unique_words}
frequent_words = {k:v for k,v in word_frequency.items() if v>5}
print(frequent_words)
