matches = dict()
results = []
teams = ['iran-spain', 'iran-portugal', 'iran-morocco', 'spain-portugal', 'spain-morocco', 'portugal-morocco']
for i in range(6):
    results.append(input().split('-'))
    results[i][0], results[i][1] = int(results[i][0]), int(results[i][1])
    matches[teams[i]] = results[i]


iran_wins = 0
iran_loses = 0
iran_draws = 0
spain_wins = 0
spain_loses = 0
spain_draws = 0
morocco_wins = 0
morocco_loses = 0
morocco_draws = 0
portugal_wins = 0
portugal_loses = 0
portugal_draws = 0
iran_points = 0
spain_points = 0
morocco_points = 0
portugal_points = 0
iran_goal_difference = 0
spain_goal_difference = 0
morocco_goal_difference = 0
portugal_goal_difference = 0


if matches['iran-spain'][0] > matches['iran-spain'][1] :
    iran_wins += 1
    spain_loses += 1
    iran_points += 3
    iran_goal_difference += (matches['iran-spain'][0] - matches['iran-spain'][1])
    spain_goal_difference += (matches['iran-spain'][1] - matches['iran-spain'][0])
elif matches['iran-spain'][0] == matches['iran-spain'][1]:
    iran_draws += 1
    spain_draws += 1
    iran_points += 1
    spain_points += 1
else:
    iran_loses += 1
    spain_wins += 1
    spain_points += 3
    spain_goal_difference += (matches['iran-spain'][1] - matches['iran-spain'][0])
    iran_goal_difference += (matches['iran-spain'][0] - matches['iran-spain'][1])



if matches['iran-morocco'][0] > matches['iran-morocco'][1]:
    iran_wins += 1
    morocco_loses += 1
    iran_points += 3
    iran_goal_difference += (matches['iran-morocco'][0] - matches['iran-morocco'][1])
    morocco_goal_difference += (matches['iran-morocco'][1] - matches['iran-morocco'][0])
elif matches['iran-morocco'][0] == matches['iran-morocco'][1]:
    iran_draws += 1
    morocco_draws += 1
    iran_points += 1
    morocco_points += 1
else:
    iran_loses += 1
    morocco_wins += 1
    morocco_points += 3
    morocco_goal_difference += (matches['iran-morocco'][1] - matches['iran-morocco'][0])
    iran_goal_difference += (matches['iran-morocco'][0] - matches['iran-morocco'][1])



if matches['iran-portugal'][0] > matches['iran-portugal'][1]:
    iran_wins += 1
    portugal_loses += 1
    iran_points += 3
    iran_goal_difference += (matches['iran-portugal'][0] - matches['iran-portugal'][1])
    portugal_goal_difference += (matches['iran-portugal'][1] - matches['iran-portugal'][0])
elif matches['iran-portugal'][0] == matches['iran-portugal'][1]:
    iran_draws += 1
    portugal_draws += 1
    iran_points += 1
    portugal_points += 1
else:
    iran_loses += 1
    portugal_wins += 1
    portugal_points += 3
    iran_goal_difference += (matches['iran-portugal'][0] - matches['iran-portugal'][1])
    portugal_goal_difference += (matches['iran-portugal'][1] - matches['iran-portugal'][0])



if matches['spain-portugal'][0] > matches['spain-portugal'][1]:
    spain_wins += 1
    portugal_loses += 1
    spain_points += 3
    spain_goal_difference += (matches['spain-portugal'][0] - matches['spain-portugal'][1])
    portugal_goal_difference += (matches['spain-portugal'][1] - matches['spain-portugal'][0])
elif matches['spain-portugal'][0] == matches['spain-portugal'][1]:
    spain_draws += 1
    portugal_draws += 1
    spain_points += 1
    portugal_points += 1
else:
    portugal_wins += 1
    spain_loses += 1
    portugal_points += 3
    spain_goal_difference += (matches['spain-portugal'][0] - matches['spain-portugal'][1])
    portugal_goal_difference += (matches['spain-portugal'][1] - matches['spain-portugal'][0])

if matches['spain-morocco'][0] > matches['spain-morocco'][1]:
    spain_wins += 1
    morocco_loses += 1
    spain_points += 3
    spain_goal_difference += (matches['spain-morocco'][0] - matches['spain-morocco'][1])
    morocco_goal_difference += (matches['spain-morocco'][1] - matches['spain-morocco'][0])
elif matches['spain-morocco'][0] == matches['spain-morocco'][1]:
    spain_draws += 1
    morocco_draws += 1
    spain_points += 1
    morocco_points += 1
else:
    spain_loses += 1
    morocco_wins += 1
    morocco_points += 3
    spain_goal_difference += (matches['spain-morocco'][0] - matches['spain-morocco'][1])
    morocco_goal_difference += (matches['spain-morocco'][1] - matches['spain-morocco'][0])


if matches['portugal-morocco'][0] > matches['portugal-morocco'][1]:
    portugal_wins += 1
    morocco_loses += 1
    portugal_points += 3
    portugal_goal_difference += (matches['portugal-morocco'][0] - matches['portugal-morocco'][1])
    morocco_goal_difference += (matches['portugal-morocco'][1] - matches['portugal-morocco'][0])
elif matches['portugal-morocco'][0] == matches['portugal-morocco'][1]:
    portugal_draws += 1
    morocco_draws += 1
    portugal_points += 1
    morocco_points += 1
else:
    morocco_wins += 1
    morocco_points += 3
    portugal_loses += 1
    portugal_goal_difference += (matches['portugal-morocco'][0] - matches['portugal-morocco'][1])
    morocco_goal_difference += (matches['portugal-morocco'][1] - matches['portugal-morocco'][0])

print('Spain wins:%i , loses:%i , draws:%i , goal_difference:%i , points:%i' %(spain_wins, spain_loses, spain_draws, spain_goal_difference, spain_points))
print('Iran wins:%i , loses:%i , draws:%i , goal_difference:%i , points:%i' %(iran_wins, iran_loses, iran_draws, iran_goal_difference, iran_points))
print('Portugal wins:%i , loses:%i , draws:%i , goal_difference:%i , points:%i' %(portugal_wins, portugal_loses, portugal_draws, portugal_goal_difference, portugal_points))
print('Morocco wins:%i , loses:%i , draws:%i , goal_difference:%i , points:%i' %(morocco_wins, morocco_loses, morocco_draws, morocco_goal_difference, morocco_points))