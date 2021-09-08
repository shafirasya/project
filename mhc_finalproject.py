def menu():
    print('>> 1. Emotion Tracker: Identify your feeling <<')
    print('>> 2. Daily Journal: Write your daily journey <<')
    print('>> 3. Find Companion: Find a friend/community support <<')
    print('>> 4. Expert Help: Consult to a psychologist <<')

def list_emotion(list1, list2):
    print('Okay, take a look at these words: ')
    count = 1
    for x in list1:
        print(count, '.', x)
        count += 1

    print('Which one is closest to describe your emotion?')
    ce2 = int(input('Enter number: ')) - 1
    print('You probably feel ' + list2[ce2])

#Emotion Tracker
def menu_1():
    print('Inhale, exhale, take your time\nWhat do you feel intensely right now?')
    emotion1 = ['Joyful', 'Powerful', 'Peaceful', 'Sad', 'Mad', 'Scared']
    count = 1
    for e1 in emotion1:
        print(count, '.', e1)
        count += 1

    ce1 = int(input('Insert the emotion number: '))

    joyful_l1 = ['Excited', 'Sensuous', 'Energetic', 'Cheerful', 'Creative', 'Hopeful']
    joyful_l2 = ['Daring', 'Fascinating', 'Stimulating', 'Amused', 'Creative', 'Optimistic']
    powerful_l1 = ['Faithful', 'Important', 'Appreciated', 'Respected', 'Proud', 'Aware']
    powerful_l2 = ['Confident', 'Discerning', 'Valuable', 'Worthwhile', 'Successful', 'Suprised']
    peaceful_l1 = ['Content', 'Thoughtful', 'Intimate', 'Loving', 'Trusting', 'Nurturing']
    peaceful_l2 = ['Relaxed', 'Pensive', 'Responsive', 'Serene', 'Secure', 'Thankful']
    sad_l1 = ['Guilty', 'Ashamed', 'Depressed', 'Lonely', 'Bored', 'Tired']
    sad_l2 = ['Remorseful', 'Stupid', 'Inferior', 'Isolated', 'Apathetic', 'Sleepy']
    mad_l1 = ['Hurt', 'Hostile', 'Angry', 'Selfish', 'Hateful', 'Critical']
    mad_l2 = ['Distant', 'Sarcastic', 'Frustated', 'Jealous', 'Irritated', 'Skeptical']
    scared_l1 = ['Confused', 'Rejected', 'Helpless', 'Submissive', 'Insecure', 'Anxious']
    scared_l2 = ['Bewildered', 'Discouraged', 'Insignificant', 'Inadequate', 'Embarrassed', 'Overwhelmed']

    if ce1 == 1:
        list_emotion(joyful_l1, joyful_l2)
    elif ce1 == 2:
        list_emotion(powerful_l1, powerful_l2)
    elif ce1 == 3:
        list_emotion(peaceful_l1, peaceful_l2)
    elif ce1 == 4:
        list_emotion(sad_l1, sad_l2)
    elif ce1 == 5:
        list_emotion(mad_l1, mad_l2)
    elif ce1 == 6:
        list_emotion(scared_l1, scared_l2)

    print('You can explore more about the feeling and go to our website to learn how to react with the emotion.\nWhatever it is, your feeling is valid! :)')

#Daily Journal
def menu_2():
    print('Make yourself comfortable, take your time')

    while True:
        input('Write your story today: ')
        ans = input('Done? Yes/No: ')
        if ans == 'Yes':
            print('Okay, your dialy journey is saved.\nHope this helps you feeling better!')
            break
        elif ans == 'No':
            print('Okay, you can continue writing.')

#Find partner
def menu_3():
    print('Do you prefer to talk in person or with a lot of people?')
    print('1. Talk in person\n2. Talk with a lot of people')
    choice = int(input('Enter the number: '))

    if choice == 1:
        print('We will find you a friend to talk!')
        ans = input('Do you have any preference? Yes/No: ')
        if ans == 'Yes':
            input('Enter your preference (gender, age, etc): ')
            print('Okay, we will search first')
        elif ans == 'No':
            print('Okay, we will randomize your friend')

        print('Wait......')
        print('Friend is found! We will send a link to your email so you can talk to your friend. Have a good conversation!')

    elif choice == 2:
        print('You can talk to our community support group!')
        print('We will send a link to your email so you can join our community support group. Have a good conversation!')

#Expert help
def menu_4():
    print('Hi! Please fill out this form first!')
    consult_date = input('Date for consultation (mm/dd/yy): ')
    consult_time = input('Time for consultation (time AM/PM): ')
    preference = input('Preference for the psychologist (if any): ')

    print('Thank you! We will find the available psychologist first')
    print('Searching.......')

    print('Psychologist is found!')
    print('You will consult with psychologist Mary on ' + consult_date + ' at ' + consult_time + '. We will remind you.')
    print('Thank you for trusting us. Remember, consult with an expert is a good thing!')

#Closing
def close():
    print('Thank you for taking care of your mental health.')
    num1 = int(input('Before you go, choose a number from 1 to 7: '))
    num2 = int(input('Choose any positive number: '))

    for n in range(num2):
        if num1 == 1: print('I am the architect of my life. I choose how it goes.')
        elif num1 == 2: print('I can and will achieve greatness.')
        elif num1 == 3: print('I am a magnet for great things.')
        elif num1 == 4: print('My goals and dreams are 100% possible, and I will achieve them.')
        elif num1 == 5: print('I am best friends with growth and success.')
        elif num1 == 6: print('I have a warrior spirit. I will not be defeated easily.')
        elif num1 == 7: print('I continuously enhance all areas of my life.')

    print('*******************************************************')
    print('        Thank you for trusting LiveWell. Bye!          ')
    print('*******************************************************')
    quit()

#Interaction
print('*******************************************************')
print('Hello! Welcome to LiveWell, your mental health checker.')
print('*******************************************************')

name = input('Hi, tell us your name: ')

print('Hello ' + name + ' how is your day?')
input('Tell us: ')
print('Thank you for sharing.')

while True:
    print('What do you want to do?')
    menu()
    choice = int(input('Insert the number: '))

    if choice == 1:
        menu_1()
        ansch = input('Do you want to do anything else? Yes/No: ')
        if ansch == 'Yes':
            continue
        elif ansch == 'No':
            close()
    elif choice == 2:
        menu_2()
        ansch = input('Do you want to do anything else? Yes/No: ')
        if ansch == 'Yes':
            continue
        elif ansch == 'No':
            close()
    elif choice == 3:
        menu_3()
        ansch = input('Do you want to do anything else? Yes/No: ')
        if ansch == 'Yes':
            continue
        elif ansch == 'No':
            close()
    elif choice == 4:
        menu_4()
        ansch = input('Do you want to do anything else? Yes/No: ')
        if ansch == 'Yes':
            continue
        elif ansch == 'No':
            close()