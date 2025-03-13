def creat_dictionary(number):
    dictionary = dict()
    for i in range(number):
        one_word_translate = input().split()
        for j in range(1, 4):
            dictionary[one_word_translate[j]] = one_word_translate[0]
    
    return dictionary
def translate(string):
    result = ''
    words = string.split()
    for i in range(len(words)):
        result += '%s '%(dictionary.get(words[i], words[i]))
    return result


n = int(input())
dictionary = creat_dictionary(n)
text = str(input())
final = translate(text)
print(final) 
