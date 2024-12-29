import random
import matplotlib.pyplot as plt

# Dictionary to store user information, progress, and scores
user_data = {}

#this function creates a dictionary that stores french word as key and english word as its value and returns the dictionary
def dict_vocab(vocab):
    vocabulary = {}
    with open(vocab, 'r') as file:
        for line in file:
            french, english = line.strip().split(',')
            vocabulary[french] = english
    return vocabulary

#registers the user and adds username to user_data with a dictionary of score and progress(list) as its list
def register():
    username = input("Enter your username: ").strip()
    if username in user_data:
        print("User already exists. Please log in.")
        return username
    else:
        user_data[username] = {'score': 0, 'progress': []}
        print("User registered successfully!")
        return username

#logins the user
def login():
    username = input("Enter your username: ").strip()
    if username in user_data:
        print("Login successful!")
        return username
    else:
        print("User not found. Please register.")
        return None
    
#saves progress i.e adds score and appends progress of the user acc to tests and practice
def save_progress(username, score):
    user_data[username]['score'] += score
    user_data[username]['progress'].append(score)

#displays the dictionary of french words with its translations in english   
def display_vocabulary(vocabulary):
    print("French\t\tEnglish")
    print("=======================")
    for french, english in vocabulary.items():
        print(french+ "   \t\t    " +english)

#function to plot graph of user data acc to different test scores
def plot_graph(username):
    plt.plot(range(1, len(user_data[username]['progress']) + 1), user_data[username]['progress'])
    plt.xlabel('Test Number')
    plt.ylabel('Score')
    plt.title('Progress of '+username)
    plt.show()

#this method selects a random french word from dict by random.choice method and asks user its translation and increases the score if its correct
def practice(vocabulary):
    if not vocabulary:
        print("Vocabulary is empty. Please check your vocabulary file.")
        return
    french_word = random.choice(list(vocabulary.keys()))
    correct_eng_word = vocabulary[french_word]
    user_word = input("What is the English translation of " +french_word+" ?").strip().lower()
    if user_word ==correct_eng_word.lower():
        print("Correct!")
        return 1
    else:
        print("Wrong! The correct translation is" +correct_eng_word+".")
        return 0
#function that takes a 10 mark test and returns the score
def test(vocabulary):
    questions = random.sample(list(vocabulary.keys()), 10)
    score = 0
    for i, french_word in enumerate(questions, start=1):
        print(f"Question{i}:")
        correct_eng_word = vocabulary[french_word]
        user_word = input("What is the English translation of "+ french_word+ "?").strip().lower()
        if user_word ==correct_eng_word.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct translation is "+correct_eng_word+".")
    return score
#main method
def main():
    print("Welcome to the French Learning Platform!")
    
    #vocabulary variable stores the dictionary returned through this function
    vocabulary = dict_vocab('vocab.txt')
    
    username = None 

    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Learn")
        print("4. Practice")
        print("5. Take Test")
        print("6. View Progress")
        print("7. Quit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            username=register()
        elif choice == '2':
            username = login()
        elif choice == '3':
            display_vocabulary(vocabulary)
        elif choice == '4':
            score = practice(vocabulary)
            if username:
                save_progress(username, score)
        elif choice == '5':
            if username:
                score = test(vocabulary)
                save_progress(username, score)
                print(f"Your score for the test is: {score}")
        elif choice == '6':
            if username:
                plot_graph(username)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

main()