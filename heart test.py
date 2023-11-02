from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Heart DIagnosis Report")
root.geometry("600x400")

root.configure(background="pink")


q1_rb= StringVar(value="0")

Q1=Label(root, text = "Do you experiance shortness of breath while doing routine activities?")
Q1.pack()
q1_r1=Radiobutton(root, text = "Yes", variable=q1_rb, value="Yes")
q1_r1.pack()
q1_r2=Radiobutton(root, text = "No", variable=q1_rb, value="No")
q1_r2.pack()

q2_rb= StringVar(value="0")

Q2=Label(root, text = "Do you have swelling in the feet / ankles / legs (shoes feel tighter) or abdomen?")
Q2.pack()
q2_r1=Radiobutton(root, text = "Yes", variable=q2_rb, value="Yes")
q2_r1.pack()
q2_r2=Radiobutton(root, text = "No", variable=q2_rb, value="No")
q2_r2.pack()

q3_rb= StringVar(value="0")

Q3=Label(root, text = "Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
Q3.pack()
q3_r1=Radiobutton(root, text = "Yes", variable=q3_rb, value="Yes")
q3_r1.pack()
q3_r2=Radiobutton(root, text = "No", variable=q3_rb, value="No")
q3_r2.pack()

q4_rb= StringVar(value="0")

Q4=Label(root, text = "Do you experiance shortness of breath while at rest/lying down?")
Q4.pack()
q4_r1=Radiobutton(root, text = "Yes", variable=q4_rb, value="Yes")
q4_r1.pack()
q4_r2=Radiobutton(root, text = "No", variable=q4_rb, value="No")
q4_r2.pack()

q5_rb= StringVar(value="0")

Q5=Label(root, text = "Do you experiance persistant wheezing / coughing that produces white or pink blood tinged mucus?")
Q5.pack()
q5_r1=Radiobutton(root, text = "Yes", variable=q5_rb, value="Yes")
q5_r1.pack()
q5_r2=Radiobutton(root, text = "No", variable=q5_rb, value="No")
q5_r2.pack()

def fever_score():
    score = 0 
    if q1_rb.get()=="Yes":
        score = score+20
        print(score)
    if q2_rb.get()=="Yes":
        score = score+20
        print(score)
    if q3_rb.get()=="Yes":
        score = score+20
        print(score)
    if q4_rb.get()=="Yes":
        score = score+20
        print(score)
    if q5_rb.get()=="Yes":
        score = score+20
        print(score)
        
    if score <= 20:
        messagebox.showinfo("Report","You do not need a doctor. Although make sure to check in case you show any other symptoms")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report","You may have to visit a doctor. If you do not visit a doctor make sure your symptoms dont get worse")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor! Go quickly!")
        
btn = Button(root, text= "click me", command= fever_score)
btn.pack()

    

root.mainloop()