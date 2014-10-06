#!/usr/bin/env python

# Author : Sahil Dhar (SD HACKZ)
# Description : A commandline Game [hangman] in pure python

import random,sys

def create_ques(ch):
    """
    Function to create question in the requested format 
    like if the name is Die Hard this function will return word with
    only vowels and replace other chars by _(underscore)
        _ie/_a__
    
    """
    strtoprint = ""
    for chars  in ch.lower():
            if chars == 'a' or chars == 'e' or chars == 'i'or chars == 'o' or chars == u'':
                strtoprint = strtoprint+chars
            elif chars == " ":
                  strtoprint =  strtoprint+"/"
            else:
                   strtoprint = strtoprint+"_"
    return  strtoprint


def checkinuserinput(u):
    
    """
    Boolean function implemented to check the same input given by the user
    """
    if u in set(user_inp_list):
        return  True

    else:
        return False


def run_test(user_char,ques_list,ori_list,Question,answer,index):
    """
    All the main activity of game including checking of user input adding 
    scores is carried out here.
    """
    
    global user_inp_list        #global list maintaing the user inputs for checking the same input
    global Q                    # global variable holding the new and old formatted questions
    global  stripped_user_inp   #stripping out the symbols from the latest Question generated
    global score;global loss 
    flag = False



    for ind,l in enumerate(ori_list):
            if user_char != "" and l.lower() == user_char.strip(" ").lower():
                ques_list[ind] = l
                flag = True


            elif user_char != "\n" and user_char != "":
                pass


    Q = "".join(c for c in ques_list)
    stripped_user_inp = "".join(s for s in Q if s != "_" and s != "/")
    stripped_answer = "".join(k for k in answer if k != " " and k != "\n")


    if len(stripped_user_inp) != len (stripped_answer): # matches user input with actual answer 

        if flag == True and loss < 7  :

            if len(user_inp_list) > 1 and checkinuserinput(user_char) == False: #check for repeated input
                score = score + 1
            else:
                score = score # if repeated input found score will remain same

        elif flag == False and loss < 7:
            if len(user_inp_list) > 1 and checkinuserinput(user_char) == False :
                loss = loss + 1
            else:
                loss = loss
        user_inp_list.append(user_char)
        print "Question ---> ",Q,"\n\n Total Score : ",str(score),"\t Wrong Attempts : ",chances[0:loss]
    else:
         score = score + 1
         print "You Got the Answer : ",Q.replace("/"," "),"\n\n" 
         user_inp_list = ['a','e','i','o','u'] # initializing again to initial list removing all user input for next ques
         movie_list.pop(index) # removing the item from the list so to avoid repeated ques

         main_game()




def main_game():
     if len(movie_list) != 0: #check for the end of game i.e movie_list is empty or not
        index = random.randint(0,len(movie_list) - 1)
        answer =  movie_list[index]
        Q = create_ques(answer)
        Q_list = [s for s in Q if s != " " ];ori_list=[x for x in answer]
        print "Total Score : %d\tWrong Attempts : %s "%(score,chances[0:loss])
        print "Question ---> ",Q
        while loss < 7:
            inp = raw_input("\nGuess Letter : ")
            run_test(inp,Q_list,ori_list,Q,answer,index)
            if loss == 7 :
                    print " You Can't make it (GAME OVER) "
                    sys.exit(0)
            elif len(movie_list) < 1:
                    print "\n COngratulations You win the Game !!! "
                    sys.exit(0)
        # else:
        #     print "\n COngratulations You win the Game !!! "

if __name__=='__main__':
    movie_list = [];chances = 'HANGMAN';loss =0;score=0; user_inp_list = ['a','e','i','o','u']
    with open( 'movies.txt','r+') as fdsc:
        for movie in fdsc.readlines():
            movie_list.append(movie.strip("\n").strip(" "))

    main_game()

