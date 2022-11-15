
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO

from PyQt6 import uic
from PyQt6.QtWidgets import *
import smtplib

import os
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
from PIL import Image, ImageTk



class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mail_template.ui', self)
        self.show()

        self.pushButton.clicked.connect(self.login)
        # self.pushButton_2.clicked.connect(self.attach_sth)
        self.pushButton_3.clicked.connect(self.send_mail)
    

    def login(self):
        try:
            # self.server = smtplib.SMTP(self.lineEdit_3.text(), self.lineEdit_4.text())
            self.server = smtplib.SMTP("smtp.gmail.com", "587")
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            # self.server.login(self.lineEdit.text(), self.lineEdit_2.text()) 
            self.server.login("atsotx@gmail.com", "ypnatmordschfsbz")
            # ypnatmordschfsbz

            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.pushButton.setEnabled(False)

            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.textEdit.setEnabled(True)
            # self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)

            self.msg = MIMEMultipart()

        except smtplib.SMTPAuthenticationError:
            message_box = QMessageBox()
            message_box.setText('Invalid Credentials')
            message_box.exec()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit.setFocus()

        except Exception as e:
            message_box = QMessageBox()
            message_box.setText('Login Failed: '+ str(e))
            message_box.exec()

    def send_mail(self):
        dialog = QMessageBox()
        dialog.setText("Do you want to send this mail?")
        dialog.addButton(QPushButton('Yes'), QMessageBox.ButtonRole.YesRole)
        dialog.addButton(QPushButton('No'), QMessageBox.ButtonRole.NoRole)

        if dialog.exec() == 0:
            # try:
                self.msg['From'] = self.lineEdit.text()
                self.msg['To'] = self.lineEdit_5.text()
                self.msg['Subject'] = self.lineEdit_6.text()
                self.msg.attach(MIMEText(self.textEdit.toPlainText(), 'plain'))
                text = self.msg.as_string()
                if (len(text) == 0):
                    messagebox.showinfo("Alert","Kindly enter text in TextBox")  
                else:        
                    self.encode_frame(text)
                # self.server.sendmail(self.lineEdit.text(), self.lineEdit_5.text(), text)

                message_box = QMessageBox()
                message_box.setText('Mail Sent Successfully')
                message_box.exec()

                self.lineEdit_5.setText('')
                self.lineEdit_6.setText('')
                self.textEdit.setText('')

                self.lineEdit.setFocus()
            # except Exception as e:
            #     message_box = QMessageBox()
            #     message_box.setText('Sending Mail Failed: '+ str(e))
            #     message_box.exec()

    # def attach_sth(self):
    #     # options = QFileDialog.Option()
    #     filenames, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "All Files (*.*)")
    #     if filenames != []:
    #         try:
    #             for filename in filenames:
    #                 attachment = open(filename, 'rb')
    #                 filename = filename[filename.rfind('/') + 1:]
    #                 p = MIMEBase('application', 'octet-stream')
    #                 p.set_payload(attachment.read())
    #                 encoders.encode_base64(p)
    #                 p.add_header("Content-Disposition",  f"attachment; filename={filename}")
    #                 self.msg.attach(p)
    #                 if not self.label_8.text().endswith(':'):
    #                     self.label_8.setText(self.label_8.text() + ',')
    #                 self.label_8.setText(self.label_8.text() + " " +  filename)
    #         except Exception as e:
    #             message_box = QMessageBox()
    #             message_box.setText('Attaching File Failed: '+ str(e))
    #             message_box.exec()

    def encode_frame(self, text):
        # e_pg= Frame(root)

        # myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        myfile = QFileDialog.getOpenFileName(self, "Open File", "", "Image Files (*.png *.jpg *.jpeg)")
        if not myfile:
            # messagebox.showerror("Error","You have selected nothing!")
            message_box = QMessageBox()
            message_box.setText('You have selected nothing!')
            message_box.exec()
        else:
            my_img = Image.open(myfile[0])
            new_image = my_img.resize((300,200))
            # img = ImageTk.PhotoImage(new_image)
            self.enc_fun(text,my_img)
            # label3= Label(e_pg,text='Selected Image')
            # label3.config(font=('Helvetica',14,'bold'))
            # label3.grid()
            # board = Label(e_pg, image=img)
            # board.image = img
            # self.output_image_size = os.stat(myfile)
            # self.o_image_w, self.o_image_h = my_img.size
            # board.grid()
            # label2 = Label(e_pg, text='Enter the message')
            # label2.config(font=('Helvetica',14,'bold'))
            # label2.grid(pady=15)
            # text_a = Text(e_pg, width=50, height=10)
            # text_a.grid()
            # encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
            # encode_button.config(font=('Helvetica',14), bg='#e8c1c7')
            # data = text_a.get("1.0", "end-1c")
            # button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img),IMG_Stegno.back(self,e_pg)])
            # button_back.config(font=('Helvetica',14), bg='#e8c1c7')
            # button_back.grid(pady=15)
            # encode_button.grid()
            # e_pg.grid(row=1)
            # e_F2.destroy()

    def enc_fun(self,text,myImg):
        newImg = myImg.copy()
        self.encode_enc(newImg, text)
        my_file = BytesIO()
        temp=os.path.splitext(os.path.basename(myImg.filename))[0]
        # newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
        finalImg, _ = QFileDialog.getSaveFileName(self, "Save Image", ((os.path.abspath(os.getcwd()))+"/assets/"), "Image Files (*.png)")
        # if finalImg:
        #     with open(finalImg, "wb") as f:
        #         f.write(newImg)
        newImg.save(finalImg)
        attachment = open(finalImg, 'rb')
        finalImg = finalImg[finalImg.rfind('/') + 1:]
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header("Content-Disposition",  f"attachment; filename={finalImg}")
        self.msg = MIMEMultipart()
        self.msg.attach(p)
        finaltext = self.msg.as_string()
        
        self.d_image_size = my_file.tell()
        self.d_image_w,self.d_image_h = newImg.size
        self.server.sendmail(self.lineEdit.text(), self.lineEdit_5.text(), finaltext)
        # messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")
  

    def encode_enc(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def modify_Pix(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # Extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    def generate_Data(self,data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

app = QApplication([])
window = MyGUI()
app.exec()

    