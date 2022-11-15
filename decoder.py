import os
import tkinter.filedialog
from io import BytesIO
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk


class IMG_Stegno:
    output_image_size = 0

    def main(self, root):
        root.title('Image Decoder')
        root.geometry('500x600')
        root.resizable(width =False, height=False)
        frame = Frame(root)
        frame.grid()

        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=60)
        decode.grid(pady = 250)


        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)


    def back(self,frame):
        frame.destroy()
        self.main(root)

    
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'))
        label1.grid(pady=10)
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.grid(pady=60)
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()


    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing! ")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=20)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command= lambda :self.frame_3(d_F3))
            button_back.config(font=('Helvetica',14))
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()


    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data

 
    def frame_3(self,frame):
        frame.destroy()
        self.main(root)


#GUI loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
