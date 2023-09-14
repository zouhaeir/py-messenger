import tkinter
import customtkinter
import time 
import random

app = customtkinter.CTk()
app.geometry('800x550')
app.resizable(False,False)
 
customtkinter.set_default_color_theme("green")
 
left_frame = customtkinter.CTkFrame(app,height=520,width=150,corner_radius=9)
left_frame.place(relx=0.02,rely=0.03)

top_frame = customtkinter.CTkFrame(app,height=50,width=590,corner_radius=10)
top_frame.place(relx=0.23,rely=0.03)

message_box = customtkinter.CTkFrame(app,height=450,width=590,corner_radius=10)
message_box.place(relx=0.23,rely=0.16)

L_label = customtkinter.CTkLabel(left_frame,
                                            text="Hello There!",
                                            text_font=('ariali','12','bold'),)
L_label.place(relx=-0.09,rely=0.08,)


ls_label = customtkinter.CTkLabel(left_frame,text="We Are Leon - Super \n" + 
                                                     "Creative Agency & Minimal\n" + 
                                                     "Agency Web Templates",
                                                     justify=tkinter.LEFT,
                                                     text_font=("Arial",8,))
ls_label.place(relx=0.03,rely=0.15)

label_top = customtkinter.CTkLabel(top_frame,text='File      Edit       View       Help      Settings')
label_top.place(relx=0.03,rely=0.2)

EntryBox = customtkinter.CTkEntry(message_box,width=460,height=30)
EntryBox.place(relx=0.04,rely=0.9)

def change_appearance_mode(new_appearance):
    customtkinter.set_appearance_mode(new_appearance)
    # if new_appearance == "System":
    #     customtkinter.set_default_color_theme("green")
    

# change_appearance_mode 
option = customtkinter.CTkOptionMenu(master=top_frame, 
                                                    values=["Light", "Dark", "System"], 
                                                    command=change_appearance_mode,
                                                    width=100,
                                                    text_color="black")
option.place(relx=0.80,rely=0.2)

spacing2 = 0.13
def automatic(word):
	global spacing2
	canvas1 = customtkinter.CTkButton(message_box,
                                                    hover=False,
                                                    text_color="white",
                                                    text_font=("Roautomatico Medium",10),
                                                    text=word.title(),
                                                    corner_radius=10,
                                                    fg_color="#414041")
	canvas1.place(relx=0.50,rely=spacing2)
	EntryBox.delete(0,"end")
	spacing2 += 0.13

def boot(info):
    if info is None:
        automatic("there is no commands sir")

    elif info == 'wikipedia' :
        automatic("Searching on wiki")
        try:
            info = info.replace("Wikipedia", "")
            results = wikipedia.summary(info, sentences = 2)
            
            automatic("so, wikipedia says")
            automatic(results)
            
        except:
            automatic("Not available on wikipedia")
        
    elif 'stop' in info or 'over' in info or 'bye' in info or 'quit' in info or 'see you' in info or 'go' in info:
        f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
        automatic(random.choice(f))
        app.destroy()
        
    elif info == 'search':
        t = "i am off-line sir so i can't help you","i am not available now","chick you network and try again","sorry sir your connection is broken"
        automatic(random.choice(t))

    elif 'how are' in info or "how are u" in info:
    	y = "I'm fine, and you","I'm fine, what about you","fine, how you feeling today?"
    	automatic(random.choice(y))         

    elif 'who are you' in info or "give me your introduction" in info or "what is your name" in info:
        automatic("My name is Jarvis, I am an Assistant")

    elif "who am i" in info or "whoami" in info:
        jh = "if you are speaking then, definitely you are a human", "You are Zouhair", "You are a human", "I cant identify peoples with their vocies, may be you are Zouhair or anybody with relation of Zouhair"
        automatic(random.choice(jh))

    elif 'hello' in info or 'hi' in info:
        gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering infoormation,\n"+"how can i help?", "Online and ready"
        automatic(random.choice(gf))

    elif 'help' in info:
        gf = "I Can't Help You (:"
        automatic(gf)

    else:
        automatic(f"your command, {info} is not exists")

spacing = 0.05
def Send_Messages():
    global spacing
    canvas1 = customtkinter.CTkButton(message_box,
                                                width=140,
                                                hover=False,
                                                text_color="black",
                                                text_font=("Roautomatico Medium",10),
                                                text=EntryBox.get().title(),
                                                corner_radius=10)
    canvas1.place(relx=0.04,rely=spacing)
    boot(EntryBox.get())
    EntryBox.delete(0,"end")
    spacing += 0.13

SendBt = customtkinter.CTkButton(message_box,
                                            text="Send",
                                            width=80,
                                            height=30,
                                            text_color="black",
                                            command=Send_Messages)
SendBt.place(relx=0.84,rely=0.9)



app.mainloop()