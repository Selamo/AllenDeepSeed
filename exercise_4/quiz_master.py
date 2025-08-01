import time
import json
import os

# Sample Questions
questions = {
    "Science": {
        "easy": [
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": 1},
            {"question": "What is H2O?", "options": ["Hydrogen", "Oxygen", "Water", "Helium"], "answer": 2},
            {"question": "How many legs do insects have?", "options": ["6", "8", "4", "2"], "answer": 0},
            {"question": "What gas do plants breathe in?", "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], "answer": 1},
            {"question": "What organ pumps blood?", "options": ["Liver", "Lung", "Heart", "Brain"], "answer": 2}
        ],
        "hard": [
            {"question": "Atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": 1},
            {"question": "Which element has the symbol 'Fe'?", "options": ["Iron", "Fluorine", "Zinc", "Gold"], "answer": 0},
            {"question": "How many bones in adult body?", "options": ["200", "206", "210", "201"], "answer": 1},
            {"question": "Unit of electrical resistance?", "options": ["Volt", "Amp", "Ohm", "Watt"], "answer": 2},
            {"question": "Light year measures?", "options": ["Time", "Speed", "Distance", "Weight"], "answer": 2}
        ]
    },
    "History": {
        "easy": [
            {"question": "Who discovered America?", "options": ["Columbus", "Einstein", "Newton", "Tesla"], "answer": 0},
            {"question": "Where is the Great Wall?", "options": ["India", "China", "Egypt", "Italy"], "answer": 1},
            {"question": "Who was the first US President?", "options": ["Lincoln", "Jefferson", "Washington", "Adams"], "answer": 2},
            {"question": "Which war ended in 1945?", "options": ["WW1", "WW2", "Cold War", "Civil War"], "answer": 1},
            {"question": "Egyptians wrote on?", "options": ["Clay", "Leaves", "Stone", "Papyrus"], "answer": 3}
        ],
        "hard": [
            {"question": "When was the French Revolution?", "options": ["1492", "1789", "1914", "1812"], "answer": 1},
            {"question": "Who wrote Magna Carta?", "options": ["King John", "Henry VIII", "Elizabeth I", "Napoleon"], "answer": 0},
            {"question": "Roman Empire fell in?", "options": ["300 AD", "476 AD", "800 AD", "1453 AD"], "answer": 1},
            {"question": "The 'Iron Curtain' separated?", "options": ["Africa", "Europe", "Asia", "Americas"], "answer": 1},
            {"question": "Who was Stalin?", "options": ["Russian leader", "Nazi", "US general", "Poet"], "answer": 0}
        ]
    },
    "Sports": {
        "easy": [
            {"question": "How many players in a football team?", "options": ["9", "11", "7", "10"], "answer": 1},
            {"question": "Which sport uses a bat?", "options": ["Tennis", "Soccer", "Cricket", "Boxing"], "answer": 2},
            {"question": "Basketball court shape?", "options": ["Circle", "Oval", "Square", "Rectangle"], "answer": 3},
            {"question": "Olympics held every?", "options": ["2", "3", "4", "5"], "answer": 2},
            {"question": "Tennis Grand Slam has how many?", "options": ["2", "3", "4", "5"], "answer": 2}
        ],
        "hard": [
            {"question": "Who won FIFA 2018?", "options": ["Germany", "France", "Brazil", "Croatia"], "answer": 1},
            {"question": "How long is an Olympic marathon?", "options": ["26.2 mi", "25 mi", "30 mi", "22 mi"], "answer": 0},
            {"question": "What is a perfect score in gymnastics?", "options": ["9", "10", "15", "100"], "answer": 1},
            {"question": "Who has most Olympic golds?", "options": ["Usain Bolt", "Phelps", "Nadia", "Bolt"], "answer": 1},
            {"question": "Where did rugby originate?", "options": ["USA", "England", "France", "Italy"], "answer": 1}
        ]
    }
}

high_scores_file = "high_scores.json"

def load_high_scores():
    if os.path.exists(high_scores_file):
        with open(high_scores_file, "r") as file:
            return json.load(file)
    return {}

def save_high_scores(scores):
    with open(high_scores_file, "w") as f:
        json.dump(scores, f, indent=2)

def ask_questions(category, difficulty):
    questions_list = questions[category][difficulty]
    score = 0
    start = time.time()
    wrong_answers = []
    total = len(questions_list)

    print(f"\nSelected: {category} ({difficulty.capitalize()})")
    for i, q in enumerate(questions_list, 1):
        print(f"\nQuestion {i}/{total}: {q['question']}")
        print_progress_bar(i-1, total)

        for idx, option in enumerate(q['options']):
            print(f"{chr(65+idx)}) {option}", end="    ")
        print()

        q_start = time.time()
        user_input = input("Your answer (A/B/C/D): ").strip().upper()
        q_end = time.time()

        elapsed = round(q_end - q_start, 2)
        selected = ord(user_input) - 65

        if selected == q["answer"]:
            print(f" Correct! (+10 points) Time: {elapsed} sec")
            score += 10
        else:
            print(f"Wrong. Correct was: {chr(65+q['answer'])}) {q['options'][q['answer']]}")
            wrong_answers.append((q, user_input))
        print_progress_bar(i, total)

    print("\ FINAL SCORE:", f"{score}/{total*10}")
    end = time.time()
    print(" Total Time:", round(end - start, 2), "seconds")

    if wrong_answers:
        print("\n📘 REVIEW INCORRECT ANSWERS:")
        for q, ans in wrong_answers:
            print(f"- {q['question']}")
            print(f"   Your answer: {ans}")
            print(f"   Correct: {chr(65+q['answer'])}) {q['options'][q['answer']]}\n")

    return score

def print_progress_bar(done, total):
    percent = int((done/total) * 100)
    bar = ("█" * (percent // 10)).ljust(10, "░")
    print(f"[{bar}] {percent}% Complete")

high_scores = load_high_scores()

print("=== QUIZ MASTER ===")
print("Categories:", ", ".join(questions.keys()))
category = input("Choose category: ").strip().title()

if category not in questions:
   print("Invalid category.")

difficulty = input("Choose difficulty (easy/hard): ").strip().lower()
if difficulty not in questions[category]:
   print("Invalid difficulty.")

score = ask_questions(category, difficulty)

    # Save personal best
key = f"{category}_{difficulty}"
if key not in high_scores or score > high_scores[key]:
    print("New personal best!")
    high_scores[key] = score
    save_high_scores(high_scores)



