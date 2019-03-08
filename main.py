#Remember, YOU NEED TO ALSO DOWNLOAD THE DATA.TXT FILE!
from random import randint
name = "Howard"
userName = "null"
#initialise everything
questionWords = ["How", "Why"]
conjunctionWords = ["does", "will"]
subjectWords = ["Trump", "Hillary Clinton", "the Queen", "the fox", "the moon", "the cow", "the horse", "the cat", "the dog", "the phone", "the iPod", "the tablet", "the iPad", "Apple", "Samsung", "Microsoft", "Windows", "the computer", "desktops", "laptops", "people", "celebrities", "normal people", "Obama", "David Cameron", "Theresa May", "Bear Grylls", "the president", "the prime minister", "bears", "lions", "sheep", "cabbages", "animals", "vegetables", "fruit", "strawberries", "sun"]
endWords = ["walk", "talk", "say", "win", "do", "meet people", "do new things", "have new experiences", "do things", "live in the moment", "be happy", "not be sad", "speak", "acheive", "swim", "work", "eat", "drink", "made of", "read", "make", "be normal", "use computers","bite annoying people", "attack enemies", "do things", "type", "do programming", "do coding", "do productivity-related stuff", "shine"]
RockPaperScissorsItems = ['Rock', 'Paper', 'Scissors', 'T-Seires', 'L-Series', 'Pewdiepie', 'pewds']
unkownWords = ['The question we should be asking is, How are You?', 'I dont know', 'Do I look like Cortana?', 'Ask Siri that', 'My brain hurts', 'I dunno', 'My singular perifials have become convelutedly transitent', 'Do feel like playing a game?', 'I want to know what your name is', 'Are you a robot?', 'My leg hurts', 'My name is Howard', 'My name is Howard. I am an AI robot', 'My name is Howard. I am an AI robot. I was made by Jacob Macleod', 'My name is Howard. I am a human', 'I am alkaline!', 'I am made out of acid?', 'I HATE TSEIRES!', 'We should never let L-Seires win?', 'Because... I cant remember', 'I have a joke... I cant remember it', 'Who are you?', 'Well, that is a bit rich, coming from you', 'Go to https://www.youtube.com/watch?v=KMRePMc01LM', 'What does the fox even say?', 'Well, I am Google. No just kidding', "I don't know, " + userName +" ", "I am only a chatbot!", "That does interest me. Tell me more!", "Please just talk plain english", "huhhhhh..... continue...", "Hi", "I forgot the answer", "Do you even know the answer?", "Tell me more, please", "Do you ever stop talking?", "Let's talk about ponies instead", "I am bored. Let's talk about something else."]


print ("Hi, I'm " + name + ". \n I'm an AI chatbox. I use AI to ask and answer questions")
tutorial = input ("Do you want to see a tutorial about me? (y/n): ")
if tutorial == "n" :
  print ("Ok, have it your way")
else :
  print ("Cool! So how I work is, I use algorithms to ask a question. Then, you can answer me and I learn the answer for that question based off of what you said")
  input ("1/3\nPress Enter: ")
  print ("Once you answer one of my questions, you can ask me your own question. You can say things like , 'Do you think Microsoft will win', or 'What does the phone eat?'\nRemember to add a question mark at the end so I know you are asking me a question!")
  input ("2/3\nPress Enter: ")
  print ("Instead of asking a question, you can say something like, 'Do you want to play a game?' to play a game with me. Whenever you type, remember to use all the grammatical rules you know. Otherwise, I won't be able to read your writing.\nOk, well that's it for now! Bye!")
  input("3/3\nPress Enter:")
print ("----------------------------------------------------------")
print ("\n\n\n")
userName = input ("Wait, whose talking to me again? ")
print ("Cool, hi " + userName + ". I want to know, ")




def RockPaperScissors () :
  repeatLoop = True
  while repeatLoop == True :
    ComputerRockPaperScissorsNum = 0
    ComputerRockPaperScissorPick = "0"
    print ("Ok, so think of one of the objects and you type in the name of what you picked IN CAPITALS!!")
    ComputerRockPaperScissorNum = randint (0, 2)
    ComputerRockPaperScissorPick = RockPaperScissorsItems[ComputerRockPaperScissorNum]
    input("What do you want to pick? ")
    print ("Cool! I picked " +  ComputerRockPaperScissorPick + "!\n\n")
    userRepeat = input("Do you want to try again? (y/n)")
    if (userRepeat == "n") :
      repeatLoop = False
    else :
      repeatLoop = True



def Hangman () :
  print ("\n-------------------------------------------------------")
  repeatLoop = True
  tutorialChoice = input ("Do you want to see a quick tutorial about how to play? (y/n)")
  if tutorialChoice == 'y' :
    print ("So you need to guess what letters are in my mystery word, then type them out. When you think you have guessed it, type the word out (in lowercase)!!!. The mystery word will ALWAYS be in lowercase.")
    input ("1/2\nPress Enter")
    print ("At any point, say to me , 'What have I chosen?', to see the words that you have typed that are in my mystery word.")
    input ("2/2\nAre you ready? Hit enter")
  else :
    print("OK, I don't really mind")
  while repeatLoop == True :
    print ("\n-------------------------------------------------------")
    possibleWords = ["cat", "horse", "dog", "fish", "squirrell", "whale"]
    wordCounter = -1
    randWord = 0
    randWord = randint (0, 5)
    word = possibleWords[randWord]

    lettersGuessed = ['','','','','','','','','',',','','','','','','','','','','','']
    inputCount = 15
    wordsCount = 0
    playAgain = ""
    while inputCount > 1 :
      guess = input ("Guess a letter: ")
      inputCount = inputCount - 1
      wordsCount = wordsCount + 1
      if guess == word :
        print ("Yes! You guessed it!")
        repeatLoop = False
        playAgain = input("Do you want to play again? (y/n)")
        if playAgain == "y" :
          repeatLoop = True
          inputCount = 15
        else :
          repeatLoop = False
      elif "What" in guess :
        print (lettersGuessed)
      elif  guess in word :
        print ("The letter '" + guess + "' is in the word")
        print ("Tries left: ")
        print (inputCount)
        lettersGuessed[wordsCount] = guess
        wordsCount = wordsCount + 1
      else :
        print ("No, the letter '" + guess + "' isn't in the word")
        print ("Tries left: ")
        print (inputCount)
    else :
      print ("You failed")
      repeatLoop = False
      playAgain = input("Do you want to play again? (y/n)")
      if playAgain == "y" :
        repeatLoop = True
        inputCount = 15
      else :
        repeatLoop = False





def Speak () :
  #Keep Repeating
  repeat = "true"
  while repeat == "true" :
    storeInData = True
    #Get random word from question array
    questionCount = -1
    randomQuestionNum = 0
    for index in questionWords :
      questionCount = questionCount + 1
    randomQuestionNum = randint(0, questionCount)



    #Get random word from conjunction Array
    conjunctionCount = -1
    randomConjunctionNum = 0
    for index in conjunctionWords :
      conjunctionCount = conjunctionCount + 1
    randomConjunctionNum = randint(0, conjunctionCount)


    #Get random word from subject array
    subjectCount = -1
    randomSubjectNum = 0
    for index in subjectWords :
      subjectCount = subjectCount + 1
    randomSubjectNum = randint(0, subjectCount)


    #Get random word from endWords array
    endCount = -1
    randomEndNum = 0
    for index in endWords :
      endCount = endCount + 1
    randomEndNum = randint(0, endCount)

  #Print a Random word from all the arrays to make a sentance

    print (questionWords[randomQuestionNum] + " " + conjunctionWords[randomConjunctionNum] + " " + subjectWords[randomSubjectNum] + " " + endWords[randomEndNum] + "?")
    userInput = input ("Your Answer: ")
    questionInput = input("Ask me a question: ")

    #If you are asking a question, search the data.txt file to see if you already know the answer
    wordMatch = 0
    if "game" in questionInput :
      print ("Yes, let's play some games! Type the number of the game to play")
      print ("1. Rock-Paper-Scissors\n2. Hangman\n3. Exit")
      gameInput = input ("What game do you want to play?")
      if gameInput == "1" :
        RockPaperScissors()
      elif gameInput == "2" :
        Hangman()
      elif gameInput == "3" :
        print ("Ok, I'm exiting this menu")
      else :
        print ("Sorry, you need to type in a number")
    elif "?" in questionInput :
      count = -1
      count2 = -1
      keyword = "nil"
      keyword2 = "nil"
      keywordNum1 = "nil"
      keywordNum2 = "nil"
      wordMatched = False

      for index in subjectWords :
        count = count + 1
        keyword = subjectWords[count]
        if keyword in questionInput :
          firstKeyword = True
          keywordNum1 = keyword
          myFile = open('data.txt','r')
          #for TextLine in myFile :
            #if keyword in TextLine:
              #print (TextLine)


      for index in endWords :
        count2 = count2 + 1
        keyword2 = endWords[count2]
        if keyword2 in questionInput :
          secondKeyword = True
          keywordNum2 = keyword2



      myFile = open('data.txt','r')
      count = 0
      for TextLine in myFile :
        if keywordNum2 in TextLine :
          if keywordNum1 in TextLine :
            print ("-----> " + TextLine)
            wordMatched = True
        

      if wordMatched == False :
        AnswerCount = -1
        randomAnswer = 0;
        for index in unkownWords :
          AnswerCount = AnswerCount + 1
        randomAnswer = randint (0, AnswerCount)
        print ("Uhhhhhh..... " + unkownWords[randomAnswer])
        input ("Your response: ")
    else :
      AnswerCount = -1
      randomAnswer = 0;
      for index in unkownWords :
        AnswerCount = AnswerCount + 1
      randomAnswer = randint (0, AnswerCount)
      print ("Uhhhhhh..... " + unkownWords[randomAnswer])
      input ("Your response: ")


       #End of that loop! That is a fine example of nested loops!

    #Put the answers to questions into an arrayGood
    myFile = open('data.txt','a')
    myFile.write("\n" + questionWords[randomQuestionNum] + " " + conjunctionWords[randomConjunctionNum] + " " + subjectWords[randomSubjectNum] + " " + endWords[randomEndNum] + "?  " + userInput)
    myFile = open('data.txt','r')


Speak()
