def is_upper(string_object):
    upper = False
    if string_object[0].isupper():
        upper = True
    return upper
def edited_text(string):
    new_text = ''
    for i in range(len(string)):
        if string[i] not in ',.':
            new_text += string[i]
        elif string[i] in '.,':
            if i != len(string)- 1:
                if string[i+ 1] != ' ':
                    new_text += string[i] + ' '
            else:
                new_text += string[i]
    words_list = new_text.split()
    final_text = ''
    for word in words_list:
        if word == '.':
            final_text = final_text[:-1] + '. '
        elif word == ',':
            final_text = final_text[:-1] + ', '
        else:
            final_text += word + ' '
    final_text = final_text[:-1]
    return final_text
def special_word(textfile):
    special_words = dict()
    first_words = dict()
    words = textfile.split()
    for i in range(1, len(words)):
        if is_upper(words[i]):
            if '.' in words[i] or ',' in words[i]:
                special_words[i+ 1] = words[i][:-1] 
            else:
                special_words[i +1] = words[i]
    for i in range(len(words)):
        if '.' in words[i]:
            if i != len(words)- 1:
                if is_upper(words[i+ 1]):
                    first_words[i +2] = words[i +1]
    for k, v in first_words.items():
        if special_words[k]:
            del special_words[k]
    return special_words
def show_result(dictionary):
    final = ''
    for k, v in dictionary.items():
        final += '%i : %s\n' %(k, v)
    if final == '':
        final = 'None'
    return print(final)
text = str(input())
result = show_result(special_word(edited_text(text)))

