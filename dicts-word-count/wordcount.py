"""Count words in file."""


# put your code here.
input_file = open("twain.txt")
total_words_list = []
for line in input_file:
    line = line.rstrip()
    words_list = line.split(' ')

    total_words_list.extend(words_list)
    
    
word_count_dict = {}

for word in total_words_list:
    word_count_dict[word] = word_count_dict.get(word, 0) + 1
    

# for word in word_count_dict:
#     print(word, word_count_dict[word])
    
for word, count in word_count_dict.items():
    print(word, count)