letters = [['h','o','l','i','d','a','y'],

           ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm','i','n','g'],

           ['b','o','o','t','c','a','m','p'],

           ['f','l','o','w','c','h','a','r','t'],

           ['w', 'o', 'r', 'd', 's', 'c', 'a','p','e','s']]

 

words = [["hi","hay","day","had","lay","dal","lad","lid","hold","lady","hail"],

         ["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",

          "pong","pram","prom","ramp"],

         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",

          "comb","boom","pact","atom"],

         ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",

          "fowl","wolf","crow","half"],

         ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",

          "cope","crap","crew","crop","pace"]]


level = 0                   # In our game there is five levels so we have declare variable as level and assign value 0
score = 0                   # score variable used to store score whenever user / player  guesses correct answer the score will be increasing  
lives = 3                   # we declare lives variable and assign value 3 to it when user guesses wrong answer the lives is decresing, if lives becomes 0 the game will be end 
previous_word = ""          # previous_word variable is used to store users input whenever user enter any input it will store in this variable and compared with new_word variable to avoid duplicate values

while level<5:                 #use to iterate until condition is true 
    print(f"level {level+1}")
    print(f"Create 3 words from given letters\n {letters[level]}")
    
    count = 0               # count variable is incrementing when answer is correct, when our count is 3 then game will ask user to continue or not 
    for i in range (5):      # for is used to iterate and take input from user 5 times   
        new_word = input("word: ")

        if new_word == previous_word:       # if new_word == previous word then this will be the wrong answer 
            print("wrong guess")        
            lives=lives-1                       # lives is decrementing
            if lives ==0:
                print("game over")
                print(f"your score is: {score}")
                exit() 
        
        else:
            if new_word not in words[level]:        # if user input not in words then it will be wrong answer
                print("wrong guess")
                lives=lives-1
                if lives ==0:
                    print("game over")
                    print(f"your score is: {score}")
                    exit()     

            else:
                if new_word in words[level]:
                    count =count+1
                    score = score+1
                    previous_word = new_word
            #print(count)
                if count ==3:
                 break
    if level ==4:                       
        print("Thanks for playing")
        print(f"your final score: {score}")             # once player completing all level it will print final score 
        level =level+1
        break  
    ans = input("wants to continue: yes/no: ")      #ans taking user input if user wants to continue the game           
    
    if ans =="yes":                    
        level =level+1
    
    else: 
        print(f"your score is: {score}")
        break
    
    

    
               
           
            
    



