# French vocabulary file (vocab.txt)
# Example content:
# maison,house
# chat,cat
# ...
import random

user_scores = {'user1': 0, 'user2': 0}

def load_vocabulary(vocab):
    vocabulary = {}
    with open("vocab.txt", 'r') as file:
        for line in file:
            french, english = line.strip().split(',')
            vocabulary[french] = english
    return vocabulary

vocabulary = load_vocabulary('vocab.txt')


def take_test(vocabulary):
    test_questions = random.sample(list(vocabulary.keys()), 10)  
    for french_word in test_questions:
        correct_translation = vocabulary[french_word]
        user_translation = input(f"What is the English translation of '{french_word}'? ").strip().lower()
        if user_translation == correct_translation.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct translation is '{correct_translation}'.")
    return "Your score is"+ score



import matplotlib.pyplot as plt
def plot_user_progress():
         users = list(user_scores.keys())
         scores = list(user_scores.values())
         plt.plot(users, scores)
         plt.xlabel('Users')
         plt.ylabel('Scores')
         plt.title('User Progress')
         plt.show() 


import random

def french_to_english_exercise(vocabulary):

    if not vocabulary:
        print("Error: Vocabulary is empty. Please check your vocabulary file.")
        return
    french_word = random.choice(list(vocabulary.keys()))
    correct_translation = vocabulary[french_word]
    user_translation = input(f"What is the English translation of '{french_word}'? ").strip().lower()
    if user_translation == correct_translation.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct translation is '{correct_translation}'.")

def display_vocabulary(vocabulary):
    print("French\t\tEnglish")
    print("=======================")
    for french, english in vocabulary.items():
        print(f"{french}\t\t{english}")




def main():
    print("Welcome to the French Learning Platform!")
    username = input("Enter your username: ").strip()
    
    score = 0 
    
    vocabulary = load_vocabulary('vocab.txt')

    while True:
        print("\nMenu:")
        print("1. Learn Words")
        print("2. Practice")
        print("3. Test")
        print("4. View user progress")
        print("5. Quit")
        
        choice = input("Enter your choice: ").strip()
        if choice=='1':
            display_vocabulary(vocabulary)
        elif choice == '2':
            french_to_english_exercise(vocabulary)
        elif choice == '3':
            take_test(vocabulary)
            user_scores['user1'] += score
        elif choice == '4':
             plot_user_progress()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
