import re

text_file = input("input the path to your text file   ")
common_words_file = input("input the path to your common words file  ")
n = int(input("input your value for n  "))

common_words = {}
with open(common_words_file, 'r') as f:
  for line in f:
      cleaned_word = line.strip()
      cleaned_word = re.sub("[^a-zA-Z]+", "", cleaned_word)
      common_words[ line.strip()] = True


lines = []
with open(text_file, 'r') as f:
  
  for line in f:
    curr_line = line.strip()
    if curr_line == '' or None:
      continue
    else:
      lines.append(curr_line)


appearances = {}
for line in lines:
  curr_words = line.split(" ")

  for word in curr_words:
    word = re.sub("[^a-zA-Z]+", "", word)
    word = word.lower()
    if word not in common_words and word != "i":
      
      if word not in appearances:
        appearances[word] = 1
      else:
        appearances[word]+=1


list_of_appearances = list(appearances.items())
list_of_appearances.sort(key = lambda x: x[1])
list_of_appearances =list_of_appearances[::-1]

print("===    ====")

counter = 0
for word, appearances in list_of_appearances:
  if counter >= n or counter >= len(list_of_appearances):
    break


  if word != '' and word != None:
    print(f"{appearances}    {word}")

    counter+=1