import time 



class Psentense:
    def printer(self, sentense): #Get a input from the user and Type print it out 
        sentense_len = len(sentense)
        for letter in range(sentense_len):
            print(sentense[letter], end='', flush = True);time.sleep(0.1) #print it  out word by word




class Introduce(Psentense):
    def __init__(self):
        self.printer("Hello Friend :)")
        time.sleep(1)

        print("""                        
             _______  _______   _______   _______   ______    _______          
            / ___   ) (  ____ \ (  ____ ) (  ___  ) (  __  \  (  ____ \ |\     /|
            \/   )  | | (    \/ | (    )| | (   ) | | (  \  ) | (    \/ ( \   / )
                /   ) | (__     | (____)| | |   | | | |   ) | | (__      \ (_) / 
               /   /  |  __)    |     __) | |   | | | |   | | |  __)      \   /  
              /   /   | (       | (\ (    | |   | | | |   ) | | (          ) (   
             /   (_/\ | (____/\ | ) \ \__ | (___) | | (__/  ) | (____/\    | |   
            (_______/ (_______/ |/   \__/ (_______) (______/  (_______/    \_/   
                                                                               ,Product


        """)

        time.sleep(3)








	    	    


    