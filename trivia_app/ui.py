from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(background="#FFFFFF")
        self.word_label = (self.canvas.create_text
            (
            150,
            125,
            width=280,
            text="question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(pady=20, padx=20, image=true_image, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(pady=20, padx=20, image=false_image, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text="score: 0", background=THEME_COLOR, fg="white", font=("Courier", 10, "bold"))
        self.score_label.grid(column=1, row=0)

        self.get_next_question()




        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.word_label, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.word_label,text= f"your score is {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)



    def false_clicked(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





