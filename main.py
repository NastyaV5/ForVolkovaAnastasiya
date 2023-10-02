char_frequency = {}
text = input('Введите текст: ')
text = text.lower()    
punctuation = ['.', ',', '!', '?']

for i in punctuation:
  text = text.replace(i, '')

words = text.split()
# print(words)

print(len(set(words)))

longest_word = words[0]
shortest_word = words[0]
for word in words:
  if len(word) > len(longest_word):
    longest_word = word
  if len(shortest_word) > len(word):
    shortest_word = word
print('Самое длинное слово:', longest_word)
print('Самое короткое слово:', shortest_word)

for d in text:
  if d in char_frequency:
    char_frequency[d] += 1
  else:
    char_frequency[d] = 1


for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")