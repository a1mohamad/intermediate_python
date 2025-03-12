def counter(number):
    movies_list = []
    action_counter, comedy_counter, horror_counter, adventure_counter, romance_counter, history_counter = 0, 0, 0, 0, 0, 0
    for i in range(number):
        movie_list = [x for x in input().split()]
        del movie_list[0]
        movies_list.append(movie_list)
    for every in movies_list:
        for i in range(3):
            if every[i] == 'Action':
                action_counter += 1
            elif every[i] == 'Comedy':
                comedy_counter += 1
            elif every[i] == 'Horror':
                horror_counter += 1
            elif every[i] == 'Adventure':
                adventure_counter += 1
            elif every[i] == 'Romance':
                romance_counter += 1
            elif every[i] == 'History':
                history_counter += 1
    count_result = {'Action':action_counter, 'Adventure':adventure_counter, 'Comedy':comedy_counter, 'History':history_counter, 'Horror':horror_counter, 'Romance':romance_counter}
    count_sorted =sorted(count_result, key=lambda k :(-count_result[k], k))
    final = ''
    for i in range(6):
        final_each = '%s : %i\n' %(count_sorted[i], count_result[count_sorted[i]])
        final += final_each
    return print(final)


n = int(input())
final = counter(n)
