def is_upper(string):
    upper = False
    if len(string) == 0:
        upper = False
    else:
        if string[0].isupper():
            upper = True
    return upper

def have_cammas_and_dots(string):
    have_camma, have_dots = False, False
    dots_counter, cammas_counter  = 0, 0
    for i in range(len(string)):
        if string[i] == '.':
            have_dots = True
            dots_counter += 1
        elif string[i] == ',':
            have_camma = True
            cammas_counter += 1
    return (have_camma, have_dots, cammas_counter, dots_counter)

def special_word(string):
    words_list = string.split()
    special_words = dict()
    first_words = dict()
    camma, dot, cammas_count, dots_count = have_cammas_and_dots(words_list[0])
    if string[0].isupper():
        if camma == False and dot == False:
            first_words[1] = words_list[0]
    update_index = 0
    for i in range(len(words_list)):
        camma, dot, cammas_count, dots_count = have_cammas_and_dots(words_list[i])
        update_index = 0

        if camma == True and dot == False:
            space_count = 0
            seperated_words_list = words_list[i].split(',')
            for every in seperated_words_list:
                if every == '':
                    space_count += 1
                    seperated_words_list.remove('')
            for j in range(len(seperated_words_list)):
                if is_upper(seperated_words_list[j]):
                    special_words[i+ j+ update_index +1] = seperated_words_list[j]
            update_index += (cammas_count - space_count)

        elif dot == True and camma == False:
            space_count = 0
            m = len(words_list[i]) 
            seperated_words_list = words_list[i].split('.')
            for every in seperated_words_list:
                if every == '':
                    space_count += 1
            if is_upper(seperated_words_list[0]):
                special_words[i+ update_index +1] = seperated_words_list[0]
            update_index += (dots_count - space_count)
            if i != len(words_list) - 1:
                if m == 1:
                    if is_upper(words_list[i+ 1]):
                        first_words[i+ update_index+ 2] = words_list[i+ 1]
                elif m > 1 :
                    if words_list[i][m -1] == '.':
                        if is_upper(words_list[i+ 1]):
                            first_words[i+ update_index+ 2] = words_list[i+ 1]
        elif camma and dot:
            space_count = 0
            c = len(words_list[i])
            first_list = words_list[i].split('.')
            seperated_words_list = [x.split(',') for x in first_list]
            if seperated_words_list[0][0] == '':
                space_count += 1
                lentgh = len(seperated_words_list[0])
                if lentgh == 1:
                    first_list[i+ update_index+ 1] = seperated_words_list[1][0]
                del seperated_words_list[0]
            if seperated_words_list[-1][-1] == '':
                space_count += 1
                del seperated_words_list[-1]    
            n = 0
            for every in seperated_words_list:
                for j in range(1, len(every)):
                    if is_upper(every[j]):
                        special_words[i +n +j +update_index +1] = every[j]
                n += len(every)
            if is_upper(seperated_words_list[0][0]):
                special_words[i +update_index+ 1] = seperated_words_list[0][0]

            update_index += (dots_count + cammas_count) - space_count
            if i != len(words_list) -1:
                if words_list[i][c- 1] == '.':
                    first_words[i +update_index +2] = words_list[i+ 1]
        elif is_upper(words_list[i]):
            special_words[i+ update_index+ 1] = words_list[i]
    
    for k, v in first_words.items():
        if special_words[k] == v:
            del special_words[k]
    return special_words
def show(dictionary):
    final = ''
    if len(dictionary) == 0:
        final += 'None'
    else:
        for k, v in dictionary.items():
            final += '%i : %s\n' %(k, v)
        return final

text = str(input())
result = show(special_word(text))
print(result)
