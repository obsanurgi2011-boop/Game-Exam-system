# exam.py
questions = [
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "Capital of France?", "options": ["Berlin", "Paris", "Rome"], "answer": "Paris"},
]

def get_questions():
    return questions

def check_answer(question_index, answer):
    return questions[question_index]['answer'] == answer
