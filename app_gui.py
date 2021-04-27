import tkinter as tk
window = tk.Tk()
window.title("Editor PRO 2")

buttonFrame = tk.Frame(window)
buttonFrame.pack(fill=tk.Y, side=tk.LEFT)

textFrame = tk.Frame(window)
textFrame.pack(side=tk.RIGHT)

saveButton = tk.Button(buttonFrame,text="save", bg="green", width=10)
saveButton.grid(row=1, column=0, pady=5, sticky="ew")

openButton = tk.Button(buttonFrame, text="open", bg="green", width=10)
openButton.grid(row=0, column=0, pady=5, sticky="ew")

deleteButton = tk.Button(buttonFrame, text="delete", bg="red", width=10)
deleteButton.grid(row=2, column=0, sticky="ew")

textArea = tk.Text(textFrame)
textArea.grid(sticky="news")

window.mainloop()
