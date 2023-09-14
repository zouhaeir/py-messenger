import tkinter
import customtkinter # Type this in your terminal (pip install customtkinter)
import time 
import random
import sqlite3

customtkinter.set_default_color_theme("green")

uid = 1

class Messenger(customtkinter.CTk):
    """ 
        Messenger Made By Python Programming Language
          - Version: 0.0.1
          - Aouthr: Zouhair Khalid
          - Mail: zouhairkhalid26@gmail.com   
    """
    USERID = 6

    def __init__(self):
        super().__init__()

        # Initialize window
        self.geometry('800x550')
        self.resizable(False,False)

        # ------------- Left frame -------------

        self.frame_left = customtkinter.CTkFrame(master=self,height=520,width=150,corner_radius=9)
        self.frame_left.place(relx=0.02,rely=0.03)

        # ------------- Top frame -------------

        self.frame_top = customtkinter.CTkFrame(master=self,height=50,width=590,corner_radius=10)
        self.frame_top.place(relx=0.23,rely=0.03)

        # ------------- Message frame -------------

        self.frame_msg = customtkinter.CTkFrame(master=self,height=450,width=590,corner_radius=10)
        self.frame_msg.place(relx=0.23,rely=0.16)

        # ------------- Labels -------------

        self.heading_label = customtkinter.CTkLabel(master=self.frame_left,
                                            text="Hello There!",
                                            text_font=('ariali','12','bold'),)
        self.heading_label.place(relx=-0.09,rely=0.08,)

        self.info_label = customtkinter.CTkLabel(master=self.frame_left,text="We Are Leon - Super \n" + 
                                                    "Creative Agency & Minimal\n" + "Agency Web Templates",
                                                    justify=tkinter.LEFT,
                                                    text_font=("Arial",8,))
        self.info_label.place(relx=0.03,rely=0.15)

        self.nav_label = customtkinter.CTkLabel(master=self.frame_top,text='File      Edit       View       Help      Settings')
        self.nav_label.place(relx=0.03,rely=0.2)

        self.theme = customtkinter.CTkOptionMenu(master=self.frame_top, 
                                                    values=["Light", "Dark", "System"], 
                                                    command=self.change_appearance_mode,
                                                    width=100,
                                                    text_color="black")
        self.theme.place(relx=0.80,rely=0.2)
        self.time_label = customtkinter.CTkLabel(master=self.frame_top, width=50)
        self.time_label.place(relx=0.64,rely=0.2)
        self.clock()

        # ------------- Submit -------------

        self.input_box = customtkinter.CTkEntry(master=self.frame_msg,width=460,height=30)
        self.input_box.place(relx=0.04,rely=0.9)

        self.send_btn = customtkinter.CTkButton(master=self.frame_msg,
                                                text="Send",
                                                width=80,
                                                height=30,
                                                text_color="black",
                                                command=self.Send_Messages)
        self.send_btn.place(relx=0.84,rely=0.9)

        self.space = 0.05
        self.space2 = 0.13

    def clock(self):
        self.time = time.strftime('%H:%M:%S %p')
        self.time_label.configure(text=self.time)
        self.time_label.after(1000, self.clock)

    def change_appearance_mode(self, new_appearance):
        customtkinter.set_appearance_mode(new_appearance)

    def Send_Messages(self):
        self.question = customtkinter.CTkButton(master=self.frame_msg,
                                                width=140,
                                                hover=False,
                                                text_color="black",
                                                text_font=("Roresponseo Medium",10),
                                                text=self.input_box.get().title(),
                                                corner_radius=10)
        self.question.place(relx=0.04,rely=self.space)
        self.chat(self.input_box.get().lower())
        self.space += 0.13

    def chat(self, info):
        self.info = info
        if self.info == "":
            self.response("there is no commands sir")
        elif self.info == 'wikipedia' :
            self.response("Searching on wiki")
            try:
                self.info = self.info.replace("Wikipedia", "")
                results = wikipedia.summary(self.info, sentences = 2)
                self.response("so, wikipedia says")
                self.response(results)
                
            except:
                self.response("Not available on wikipedia")
            
        elif 'stop' in self.info or 'over' in self.info or 'bye' in self.info or 'quit' in self.info or 'exit' in self.info or 'go' in self.info:
            f = "bye sir", "OK bye sir", "see you again sir", "bye bye", "Waiting for Activation sir", "As your wish, but I don't want to go sir!"
            self.response(random.choice(f))
            self.destroy()
            
        elif self.info == 'search':
            t = "i am off-line sir so i can't help you","i am not available now","chick you network and try again","sorry sir your connection is broken"
            self.response(random.choice(t))

        elif 'how are' in self.info or "how are u" in self.info:
            y = "I'm fine, and you","I'm fine, what about you","fine, how you feeling today?"
            self.response(random.choice(y))         

        elif 'who are you' in self.info or "give me your introduction" in self.info or "what is your name" in self.info:
            self.response("My name is Jarvis, I am an Assistant")

        elif "who am i" in self.info or "whoami" in self.info:
            jh = "if you are speaking then, definitely you are a human", "You are Zouhair", "You are a human", "I cant identify peoples with their voices"
            self.response(random.choice(jh))

        elif 'hello' in self.info or 'hi' in self.info:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gathering informations"
            self.response(random.choice(gf))

        elif 'help' in self.info:
            gf = "I Can't Help You (:"
            self.response(gf)

        else:
            self.response(f"your command, {self.info} is not exists")

    def response(self, word):
        self.word = word
        self.answer = customtkinter.CTkButton(master=self.frame_msg,
                                                        hover=False,
                                                        text_color="white",
                                                        text_font=("Roautomatico Medium",10),
                                                        text=word.title(),
                                                        corner_radius=10,
                                                        fg_color="#414041")
        self.answer.place(relx=0.50,rely=self.space2)
        self.space2 += 0.13
        self.database()
        self.input_box.delete(0,"end")

    def database(self):
        self.data = sqlite3.connect('history.db')
        self.cursor = self.data.cursor()
        self.cursor.execute('create table if not exists History(msg text, answer text, time integr, uid integr)')
        self.cursor.execute(f'insert into History(msg, answer, time, uid) values("{self.input_box.get()}", "{self.word}", "{time.strftime("%d, %B, %Y")}", {Messenger.USERID})')
        
        self.data.commit()
        self.data.close()


if __name__ == '__main__':
    app = Messenger()
    app.mainloop()
