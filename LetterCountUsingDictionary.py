x = {} # start with an empty dictionary
with open('scarlet.txt', 'r') as fileref:
 for line in fileref:
  for c in line:
    x[c] = x.get(c,0) + 1

print(x)


sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split(' ')
word_counts = {}
print (words)
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print (word_counts)   



stri = "what can I do"
char_d = {}

for char in stri:
    char_d[char] = char_d.get(char, 0) + 1

print (char_d)    
 
 
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

# initialize variable best_key_so_far to be the first key in d
max_value = 0
best_key_so_far = ''
for k in d:
     if d[k] > max_value:
         max_value = d[k]
         best_key_so_far = k 
print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))


placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for char in placement:
    d[char] = d.get(char, 0) + 1

print(d)    
low_value = -1
min_value = ''

for k in d:
     if low_value == -1:
        low_value = d[k]
        min_value = k
     else:
        if d[k] < low_value:
           low_value = d[k]
           min_value = k
            
print("key " + min_value + " has the least value, " + str(d[min_value]))


product = "iphone and android phones"

lett_d = {}
for char in product:
  lett_d[char] = lett_d.get(char, 0) + 1

print (lett_d)
high_value = 0
max_value = ''
for k in lett_d:
     if lett_d[k] > high_value:
         high_value = lett_d[k]
         max_value = k 
print("key " + max_value + " has the highest value, " + str(lett_d[max_value]))



