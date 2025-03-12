The teams in Group B of the World Cup are Iran, Portugal, Spain, and Morocco. 
We want to Write a program that, upon receiving the results of the games, 
prints the team name, number of wins and losses, goal difference, and points 
in one line. Each team is printed in order of points on one line. (If the 
points are equal, the number of wins is taken into account. If both the number 
of wins and points are equal, they are printed in alphabetical order.)

Note: A team gets zero points if it loses, one point if it draws, and three points 
if it wins.
Goal difference is the difference between goals scored and goals conceded by 
a team

Read the results of the games in the following order: (In the sample input, the 
number on the left corresponds to the team on the right.)
Iran – Spain
Iran – Portugal
Iran – Morocco
Spain – Portugal
Spain – Morocco
Portugal – Morocco

input:

2-2
2-1
1-2
2-2
3-1
2-1

output:

Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3