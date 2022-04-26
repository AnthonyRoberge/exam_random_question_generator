Description:
This code generates a random list of question for the exam. 

The input parameters are:
1) nb_of_question : The number of question that should be randomly selected. This should be an integer.
2) nb_of_question_per_chapter : This is a dictionary that contain the chapter number, and the amount of question that could be selected for each chapter.

To change these parameters, you can open the random_generator.py as a text file with notepad or whatever.

The algorithm of selection goes as follow: 
1) Randomly select different chapter. Each chapter has the same chance of being selected, even though there could be a different number of questions per chapter. Keep that in mind
2) For each selected chapter, one question is randomly picked. 


To run the code, simply run the "run.bat" file, or run the random_generator.py file if you know how...





