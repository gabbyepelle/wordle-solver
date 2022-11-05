from tkinter import *


# ------------------------HELPER FUNCTIONS----------------------#

def letter_search(letter, master_list):
    words = []
    for word in master_list:
        if letter in word:
            words.append(word)
    return words


def letter_exclude(letter, master_list):
    words = []
    for word in master_list:
        if letter not in word:
            words.append(word)
    return words


def letter_position(letter, position, master_list):
    word_list = []
    for pos, word in enumerate(master_list):
        if word[position] == letter:
            word_list.append(word)
    return word_list


# -----------------------------------MAIN FUNCTIONS ------------------------------------#
def gen_misplaced_letters():
    inc = misplaced_letters.get()
    with open('sgb-words.txt') as f:
        content = [(line.strip()) for line in f.readlines()]
    letter_list = []
    for word in content:
        for letter in inc:
            letter_list.append(letter_search(letter, content))
    # print(set.intersection(*map(set, letter_list)))
    try:
        return set.intersection(*map(set, letter_list))  # might create intersection with other functions
    except TypeError:
        return content


def gen_excluded_letters():
    exc = excluded_letters.get()
    with open('sgb-words.txt') as f:
        content = [(line.strip()) for line in f.readlines()]
    letter_list = []
    for word in content:
        for letter in exc:
            letter_list.append(letter_exclude(letter, content))
    try:
        return set.intersection(*map(set, letter_list))
    except TypeError:
        return content


def gen_correct_letters():
    inc = [first_letter.get(), second_letter.get(), third_letter.get(), fourth_letter.get(), fifth_letter.get()]
    # print(inc)
    with open('sgb-words.txt') as f:
        content = [(line.strip()) for line in f.readlines()]
    index = [inc.index(i) for i in inc if i]
    x = []
    for i, word in enumerate(content):
        for j in index:
            x.append(letter_position(inc[j], j, content))
    try:
        return set.intersection(*map(set, x))
    except TypeError:
        return content


def best_guess():
    words.delete('1.0', "end")
    a = gen_misplaced_letters()
    b = gen_excluded_letters()
    c = gen_correct_letters()
    d = set.intersection(set(a), set(b), set(c))
    for word in d:
        words.insert(END, word)
        words.insert(END, "\n")


def clear():
    excluded_letters.delete(0, "end")
    misplaced_letters.delete(0, "end")
    first_letter.delete(0, "end")
    second_letter.delete(0, "end")
    third_letter.delete(0, "end")
    fourth_letter.delete(0, "end")
    fifth_letter.delete(0, "end")
    words.delete('1.0', "end")


# ---------------------UI SETUP--------------------------#
window = Tk()
window.title("Wordle Solver")
window.geometry("1200x900")
title = Label(text="Wordle Solver")
title.config(font=("Courier", 40, "bold"), pady=15, fg="green")
title.pack()
excluded = Label(text="Excluded letters:")
excluded.pack()
excluded_letters = Entry()
excluded_letters.pack()

misplaced = Label(text="Letters that are in the word but not in the right position")
misplaced.pack()
misplaced_letters = Entry()
misplaced_letters.pack()

correct = Label(text="Enter letters that are in their correct positions: ")
correct.pack()
first = Label(text="First letter:")
first.pack()
first_letter = Entry()
first_letter.pack()

second = Label(text="Second letter:")
second.pack()
second_letter = Entry()
second_letter.pack()

third = Label(text="Third letter:")
third.pack()
third_letter = Entry()
third_letter.pack()

fourth = Label(text="Fourth letter:")
fourth.pack()
fourth_letter = Entry()
fourth_letter.pack()

fifth = Label(text="Fifth letter:")
fifth.pack()
fifth_letter = Entry()
fifth_letter.pack()

suggest_button = Button(text="Stuggest Word", fg="green", bg="green", command=best_guess)
suggest_button.pack()
reset = Button(text="Reset", fg="red", bg="red", command=clear)
reset.pack()
words = Text(window, width=25, height=25)
words.pack()

window.mainloop()
