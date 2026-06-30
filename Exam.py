class ExamEngine:
    def __init__(self):
        self.questions = [
            {
                "q": "Capital of Ethiopia?",
                "a": ["Addis Ababa", "Nairobi", "Cairo", "Lagos"],
                "c": 0
            },
            {
                "q": "2 + 2 = ?",
                "a": ["1", "2", "4", "5"],
                "c": 2
            }
        ]
        self.index = 0
        self.score = 0

    def current(self):
        return self.questions[self.index]

    def answer(self, i):
        if i == self.current()["c"]:
            self.score += 1
        self.index += 1
        return self.index < len(self.questions)
