Barry , due to her lack of English proficiency, has to attend these 
meetings with a translator. Since bringing someone else to translate 
would be expensive, Barry decides to look for an alternative. Now you 
need to help Barry and write a translator that reads the dictionary 
and the corresponding sentence from the input and translates the sentence 
according to the language in which it is expressed. In the translation 
process, if a word does not exist in the dictionary, print the word itself 
in the output.

The first line of the input contains a number n, which represents the number 
of words in the dictionary for its translation. Each of the next n lines 
contains four words, the second to fourth words being the translation of 
the first word. Each word is translated into three different languages. 
The second word is the English translation, the third word is the French 
translation, and the fourth word is the German translation of the first word. 
The last line contains a sentence that needs to be translated from one of 
the languages ​​English, French or German into the language of the first word. 
A sentence consists of several words separated by a space. For more information, 
see the sample input and sample output. (If the translation of the desired 
word consists of two parts, consider it without the space. For example, 
the word laprogrammation in the sample input below is la programmation, 
with the space between its two parts ignored. )

The final sentence may be a combination of words from three languages.

input:

4
man I je ich
kheili very très sehr
alaghemand interested intéressé interessiert 
barnamenevisi programming laprogrammation Programmierung
I am very interested in programming

output:

man am kheili alaghemand in barnamenevisi