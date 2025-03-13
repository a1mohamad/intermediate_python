Jerry is sending the final list of names of the successful candidates of 
the Computer Olympiad to the results review committee so that the committee 
can print the entry cards for the final competitions. However, because a 
specific format for registering names was not defined during the exam, the 
participants did not write their names in a standard way. In addition, the 
language in which the competition was participated in is written after each 
name, and the gender of the person is specified at the beginning of each name. 
The standard form of names is such that the first letter of the name is 
capitalized and the rest of the letters of the name are lowercase. We want to 
write a program that reads the number, name, gender, and language of the 
successful candidates from the input, separates the names based on gender, 
standardizes them, and writes the language in which the person participated 
in the competition in front of each name. (In the output, the female gender is 
printed first, and then the male gender. The names in each gender are printed 
in English alphabetical order.)

input:

4
m.hosSein.python
f.miNa.C
m.aHMad.C++
f.Sara.java

output:

f Mina C
f Sara java
m Ahmad C++
m Hossein python
