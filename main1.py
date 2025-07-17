#importing so to interact with ai and ui
import os
from dotenv import load_dotenv
import tkinter as tk 
import threading
import google.generativeai as genai # importing the google generative ai library to interact with the gemini pro model
# importing the google generative ai library to interact with the gemini pro model   
load_dotenv()#loading the environment variables from the .env file
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
#configuring the api key to the google generative ai library to interact with the gemini pro model
model=genai.GenerativeModel("gemini-1.5-flash-latest")#model qbject created for gemini pro to interact by send and receice texts
chat=model.start_chat(history=[])#start chat method to start the conversation, history class used for no previous history
#function
def send_message():
    user_input=entry.get()#getting the user input from the entry box
    if user_input.strip() == "" :#checking if the user input is empty or not
        return
    if user_input.lower() in ["exit" , "quit"]:
        root.destroy()
        return
    chat_log.insert(tk.END,"You:" +user_input+ "\n")#inserting the user input to the chat log
    entry.delete(0,tk.END)#deleting the user input from the entry box if there no command to delete the user input from the entry box

    response = chat.send_message(user_input)#send message method to send the user input to the model and get the response
    chat_log.insert(tk.END, "Bot:" +response.text+ "\n")#inserting the response to the chat log tk.END places the text at the end of the text box




root = tk.Tk()#creating the main window
root.title("Gemini Chatbot")#title of the window
root.geometry("1000x600")
root.configure(bg = "#f4f4f4")#background color of the window


chat_frame = tk.Frame(root, bg = "#f4f4f4")#creating a frame for the chat log
chat_frame.pack(fill=tk.BOTH, expand = True, padx=20, pady=(20,10))

chat_log=tk.Text(chat_frame,wrap = tk.WORD,font=("Segoe UI", 12),bg = "white", fg = "#333",bd = 0,relief = tk.FLAT,  )
#Creates a text box within chat_frame with word wrapping, modern font, white background, and flat design (no borders)

chat_log.pack(side=tk.LEFT,fill=tk.BOTH,expand=True )#packing the text box to the window with padding of 10 pixels on x and y axis
#entry frame
entry_frame=tk.Frame(root , bg = "#f4f4f4")
entry_frame.pack( padx=20, pady=(0,20), fill=tk.X)#packing the entry frame to the window with padding of 20 pixels on x and y axis

#entry box for user input


entry = tk.Entry(entry_frame, font=("Segoe UI", 12))
entry.pack(side=tk.LEFT, padx=(0,10), ipady=6,fill=tk.X, expand=True)#packing the entry box to the window with padding of 10 pixels on x and y axis 
#Create an Entry widget with specific font, padding, and expand it horizontally


entry.bind("<Return>", lambda event: send_message())#accepts the input text by click enter
#button
send_button = tk.Button(entry_frame , text="send", command=send_message,font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", padx=10, pady=6)
send_button.pack(side=tk.BOTTOM, padx=(5,10),pady=(0,10))
root.mainloop()#main loop to run the window