def match_result(game):
    team1_result, team2_result= [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    team1, team2, result = (game[0].split('-'))[0], (game[0].split('-'))[1], game[1]
    team1_result.append(team1)
    team2_result.append(team2)
    if result[0] > result[1]:
        team1_result[0], team1_result[1], team2_result[3] = 3, 1, 1
        team1_result[4], team2_result[4] = (result[0] - result[1]), (result[1] - result[0])
    elif result[0] == result[1]:
        team1_result[0], team1_result[2], team2_result[0], team2_result[2] = 1, 1, 1, 1
    else:
        team2_result[0], team2_result[1], team1_result[3] = 3, 1, 1
        team2_result[4], team1_result[4] = (result[1] - result[0]), (result[0] - result[1]) 
    return team1_result, team2_result
def box_score(matches):   
    final_results = [match_result(x) for x in matches.items()]
    iran, spain, portugal, morocco = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]
    for data in final_results:
        for i in range(2):
            if 'iran' in data[i]:
                iran = [x + y for x, y in zip(iran, data[i][:5])]
            elif 'spain' in data[i]:
                spain = [x + y for x, y in zip(spain, data[i][:5])]
            elif 'portugal' in data[i]:
                portugal = [x + y for x, y in zip(portugal, data[i][:5])]
            elif 'morocco' in data[i]:
                morocco = [x + y for x, y in zip(morocco, data[i][:5])]
    final_dict = {'Iran': iran, 'Morocco': morocco, 'Portugal': portugal, 'Spain': spain}
    final_sorted = sorted(final_dict, key=lambda k:(-final_dict[k][0], -final_dict[k][1], k))
    final =''
    for i in range(4):
        final_each = '%s wins:%i , draws:%i , loses:%i , goal_difference:%i , points:%i\n' %(final_sorted[i],final_dict[final_sorted[i]][1], final_dict[final_sorted[i]][2], final_dict[final_sorted[i]][3], final_dict[final_sorted[i]][4], final_dict[final_sorted[i]][0] )
        final += final_each
    return print(final)

matches = dict()
games = ['iran-spain', 'iran-portugal', 'iran-morocco', 'spain-portugal', 'spain-morocco', 'portugal-morocco']
for i in range(6):
    matches[games[i]] = [int(x) for x in input().split('-')]
final = box_score(matches)