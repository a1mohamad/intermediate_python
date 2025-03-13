We want to write a program that prints the index words (words that start with 
a capital letter) from a text along with the word number (the most frequent 
word). If no word with this property is found in the text, print None in the 
output. Words that are at the beginning of a sentence should not be considered 
as index words. (Start the word number from one)

Numbers are not considered index words. The only symbol used in a sentence other 
than a period is a comma. Be sure to remove any period or comma at the end of a word.

input:

The Persian League is the largest sport event dedicated to the deprived areas of Iran. 
The Persian League promotes peace and friendship. This video was captured by one of 
our heroes who wishes peace.

output:

2:Persian
3:League
15:Iran
17:Persian
18:League