import time 

name = input("Enter your name: ")
welcome = "Welcome to the Harry Potter Fill in the Blanks Game, " + name + "!"
instructions = "Here's how to play: your goal is to fill in the blanks of the Harry Potter quote of your choice. If successful, you may continue to the next quote of your choice! Have fun playing!"


blanks = ["__1__","__2__","__3__", "__4__"]


quote1 = '''It takes a great deal of __1__ to stand up to our __2__, but just as much to __3__" up to our __4__.'''

quote2 = '''Do not pity the __1__, Harry. Pity the __2__, and, above all those who __3__ without __4__.'''

quote3 = '''We’ve all got both __1__ and __2__ inside us. What matters is the part we __3__ to act on. That’s who we __4__ are.'''

quote4 = '''__1__ are, in my not-so-humble opinion, our most __2__ source of magic. Capable of both __3__ injury, and __4__ it.'''

quote5 = '''Of course it is happening inside your __1__, __2__, but why on __3__ should that mean that it is not __4__'''

quote6 = '''__1__ inspires __2__, envy engenders __3__, spite spawns __4__'''

quote7 = '''The happiest __1__ on earth would be able to use the Mirror of __2__ like a normal __3__, that is, he would look into it and see himself __4__ as he is. Does that help'''

quote8 = '''Hogwarts is __1__!” shouted Professor __2__. “Man the __3__, protect us, do your duty to our __4__!'''

quote9 = '''There were near __1__, many of them. We __2__ about them afterwards. We were __3__, thoughtless — carried away with our own __4__'''

quote10 = '''Just __1__ you have the __2__ range of a __3__ doesn’t mean we all __4__'''

ans_quote1 = ["bravery", "enemies", "stand", "friends"]
ans_quote2 = ["dead", "living", "live", "love"]
ans_quote3 = ["light", "dark", "choose", "really"]
ans_quote4 = ["Words", "inexhaustible", "inflicting", "remedying"]
ans_quote5 = ["head, Harry", "earth", "real"]
ans_quote6 = ["Greatness", "envy", "spite", "lies"]
ans_quote7 = ["man", "Erised", "mirror", "exactly"]
ans_quote8 = ["threatened", "McGonagall", "boundaries", "school"]
ans_quote9 = ["misses", "laughed", "young", "cleverness"]
ans_quote10 = ["because", "emotional", "teaspoon", "have"]



game_data = {

    '1': {
        'quiz': quote1,
        'answers': ans_quote1,
        'message': "You have chosen Quote 1!"
    },
    '2': {
        'quiz': quote2,
        'answers': ans_quote2,
        'message': "You have chosen Quote 2!"
    },
    '3': {
        'quiz': quote3,
        'answers': ans_quote3,
        'message': "You have chosen Quote 3!"
    },
    '4': {
        'quiz': quote4,
        'answers': ans_quote4,
        'message': "You have chosen Quote 4!"
    },
    '5': {
        'quiz': quote5,
        'answers': ans_quote5,
        'message': "You have chosen Quote 5!"
    },
    '6': {
        'quiz': quote6,
        'answers': ans_quote6,
        'message': "You have chosen Quote 6!"
    },
    '7': {
        'quiz': quote7,
        'answers': ans_quote7,
        'message': "You have chosen Quote 7!"
    },
    '8': {
        'quiz': quote8,
        'answers': ans_quote8,
        'message': "You have chosen Quote 8!"
    },
    '9': {
        'quiz': quote9,
        'answers': ans_quote9,
        'message': "You have chosen Quote 9!"
    },
    '10': {
        'quiz': quote10,
        'answers': ans_quote10,
        'message': "You have chosen Quote 10!"
    }

}

def get_quote(): 
    pick_quote = input("Type in which quote you would like to solve. Type in a number from 1-10: ")
    while pick_quote not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        pick_level = input("Invalid input, please try again. Choose a number from 1-10")
    print(game_data[pick_quote]['message'])
    return pick_quote


def check_answer(user_answer, answers_list, answers_index):
    if user_answer == answers_list[answers_index]:
        return "right_answer"
    return "Wrong"
    pass

def lost():
    print("You lost..... :(")
    time.sleep (3)

def win():
    print("You win!!")
    time.sleep (3)
    play_harry()

def play_harry():
    print(welcome)
    print(instructions)
    quote = get_quote()
    quiz = game_data[quote]['quiz']
    print(quiz)
    answers_list =  game_data[quote]['answers']
    blanks_index = 0
    answers_index = 0
    guesses = 3

    while blanks_index < len(blanks):
        user_answer = input("Answer to question " + blanks[blanks_index] + ": ")
        if check_answer(user_answer,answers_list,answers_index) == "right_answer":
            print("\n Correct! Good job!\n")
            quiz = quiz.replace(blanks[blanks_index], user_answer.upper())
            blanks_index += 1
            answers_index += 1
            guesses = 3
            print(quiz)
            if blanks_index == len(blanks):
                return win()

        else:
            guesses -= 1
            if guesses == 0:
                return lost()
                break
            print("Wrong answer. Please try again. You have " + str (guesses) + " guesses left!")

play_harry()



