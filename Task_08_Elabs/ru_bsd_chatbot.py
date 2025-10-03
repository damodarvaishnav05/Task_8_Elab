# So here we make rule based chatbot 

def chatbot():
    print("\n" + "\tHi i am MIRA(ChatBot), So how can i help  you!!, Type by to exit")

    # i defined while loop with true condition 
    while True: 

        u_input = input("\nYou : ").lower()  # U_input means user input 

        if u_input in ["by", "it's done", "thanku"]:
            print("Thanks a lot , Have a nice day from MIRA")  # if the user type by, it's done and thanku it ends the program
            break

        elif "hello" in u_input or "hi" in u_input:            # These are the types of conditions that i have given from 
            print("chatbot: How May i Help you!!")             # here top to bottom.

        elif "what is today's wheather" in u_input or "wheather" in u_input:
            print("Chatbot: Today wheather : Temprature 26°C, Mostly Clear")

        elif "your name" in u_input:
            print("Chatbot: My name is MIRA i am a CHATBOT!!")

        elif "can i ask you any question" in u_input:
            print("Chatbot : Yess Fearlessly you can ask any question")

        elif "who developed you" in u_input:
            print("chatbot: I am MIRA(Chatbot) My developer is Damodar vaishnav")

        elif "who won asia cup 2025" in u_input:
            print("Chatbot: Team india!!!")

        elif "give me list of any 10 mma players" in u_input:
            print("""charbot:\n
1.Conor McGregor
2.Khabib Nurmagomedov
3.Jon Jones
4.Anderson Silva    
5.Georges St-Pierre
6.Israel Adesanya
7.Francis Ngannou
8.Demetrious Johnson
9.Daniel Cormier
10.Ronda Rouse  """)
       
       
        elif "predict age" in u_input:
            print("chatbot: Sorry i'd get it")

        elif "guess task for elabs" in u_input:
            print("Chatbot: Yes this is your 8th task to make a rule_based chatbot, OK")

        elif "date and current time" in u_input or "date, time" in u_input:
            print("chatbot: Today's date: 03/10/2025, current time: 7:40 PM")

        else:
            print("Chatbot: Sorry i don't got it!!")  # if any unnecessary is types then it prints this


# This run's the program
if __name__ == "__main__":
    chatbot()