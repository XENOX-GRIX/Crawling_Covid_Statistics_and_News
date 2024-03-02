Name: Avik Pramanick
Roll: 23CS60R78
Web Crawling and Extracting Information-Part1

OS                      -  linux
Programming Language    -  Python3
Status                  -  Running Fine in my system.

Compiling instruction - 

Keep both task1.py and task2.py at the same directory.
Because, 
task1.py is imported in task2.py.

While compling task1.py avialble internet connection is required.

--->  python3 task1.py
--->  python3 task2.py

Input Instruction -

1) No extra space in command line is not accepted.
2) For exit , write command: exit
	Example:
		exit
3) For going back, write command:
	Example:
		back

4) For intial menu selection, menu name/lowercase name/menu no is accepted.
	Example:
		1
		Country
		country
		4
		Query
		query
		
5) For country/continent selection , (country/continent) name / lowercase name / (country/continent) no is accepted.
	Example:
		1
		USA
		usa
		17
		India
		india
		
6) For information type selection , type exact name / type no is accepted.
	Example:
		1
		Total cases
		2
		Active cases
		
7) For Query type selection , only Query type no is accepted.
	Example:
		1
		2
		3
		4
8) For Query date range input , the input date format is dd-mm-yyyy.
	Example:
		01-01-2021
		1-1-2021
		



-----------------------------------------------------------------------------------------------------

Requirements : 
Python 
matplotlib

Run main.py to get access to the menu driven program.
import worldometer_menu and call worldometer_menu.generate_files(country_list.txt) to generate all the files in the respective folders : 
Results : 
|----------> active_cases
|----------> daily_deaths
|----------> new_cases
|----------> new_recovered
(I have included a test.py to show how this works) 
