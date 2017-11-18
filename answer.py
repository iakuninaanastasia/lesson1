answers={'привет': 'И тебе привет!', 'как дела': 'Лучше всех', 'пока': 'Увидимся'}
question='привет'
def get_answer(question, answers):
    answer=(answers[question]).lower()
    return answer
print(get_answer(question, answers))