A database is designed to contain the names, heights, and weights 
of employees of a company. We want to write a program that reads 
the information from this database file and prints the employees 
in order of height in the output along with their names and weights.
(If they are of equal  height, print the person who weighs less higher)
It is guaranteed that no two people are the same height and weight.

The format of the database table information is as follows:

Sample input: (The following information is defined in the database and 
this is an example and the number of people can be different)

Height			Weight			Name

180			75			Terry

190			90			Jason

175			75			Mohammad

175			60			Rose

output:

Jason 190 90
Terry 180 75
Rose 175 60
Mohammad 175 75