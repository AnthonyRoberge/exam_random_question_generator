import random

# Exam total number of question
nb_of_question = 5

# The amount of question written for each chapter
nb_of_question_per_chapter = {'1.1': 7,
                          '1.2': 7,
                          '2.1': 6,
                          '2.2': 5,
                          '2.3': 5,
                          '3': 4,
                          '4.1': 6,
                          '4.2': 4,
                          '5.1': 6,
                          '5.2': 4,
                          '5.3': 5,
                          '6.1': 4,
                          '6.2': 4}

# Random choice of chapter
chapter_sample = random.sample(nb_of_question_per_chapter.keys(), nb_of_question)

# For each random chapter, this will choose a random question.
for chapter in chapter_sample:
    question_nb = random.sample(range(1, nb_of_question_per_chapter[chapter]), 1)[0]
    print('Chapter ' + chapter + ',\tQuestion # ' + str(question_nb))

