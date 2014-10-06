#!/usr/bin/env python

import random,sys
# Author : Sahil Dhar (SD HACKZ)
def create_ques(ch):
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
    if u in set(user_inp_list):
        return  True

    else:
        return False


def run_test(user_char,ques_list,ori_list,Question,answer,index):
    global user_inp_list
    global Q
    global  stripped_user_inp
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



    if len(stripped_user_inp) != len (stripped_answer):
        if flag == True and loss < 7  :

            if len(user_inp_list) > 1 and checkinuserinput(user_char) == False:
                score = score + 1
            else:
                score = score

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
         user_inp_list = ['a','e','i','o','u']
         movie_list.pop(index)

         main_game()




def main_game():
     if len(movie_list) != 0:
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

