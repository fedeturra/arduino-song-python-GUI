from Tkinter import *
import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 9600)           #define serial port


class MiaApp:                                           #setup layout
  def __init__(self, genitore):

    #------ costanti per il controllo della disposizione
    larghezza_pulsanti = 5  

    imb_pulsantex = "5m"  
    imb_pulsantey = "5m"
    
    imb_quadro_pulsantix = "11m"       
    imb_quadro_pulsantiy = "2m"       
    imb_int_quadro_pulsantix = "3m"   
    imb_int_quadro_pulsantiy = "1m"   
    #------------------ fine costanti -------------------

    self.mioGenitore = genitore
    self.quadro_pulsanti = Frame(genitore)

    self.quadro_pulsanti.pack(  
      ipadx = imb_int_quadro_pulsantix,  
      ipady = imb_int_quadro_pulsantiy,  
      padx = imb_quadro_pulsantix,       
      pady = imb_quadro_pulsantiy,       
      )




    self.pulsante1 = Button(self.quadro_pulsanti,                               #define button 1
                            command = self.pulsante1Premuto)
    self.pulsante1.configure(text = "DO", background = "green")
    self.pulsante1.focus_force()
    
    self.pulsante1.configure(
      width = larghezza_pulsanti, 
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante1.pack(side = LEFT)
    self.pulsante1.bind("<Return>", self.pulsante1Premuto_a)

    


    self.pulsante3 = Button(self.quadro_pulsanti,                                  #define button 3
                            command = self.pulsante3Premuto)
    self.pulsante3.configure(text = "RE", background = "green")
    self.pulsante3.focus_force()
    
    self.pulsante3.configure(
      width = larghezza_pulsanti, 
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante3.pack(side = LEFT)
    self.pulsante3.bind("<Return>", self.pulsante3Premuto_a)
    
    

    

    self.pulsante4= Button(self.quadro_pulsanti,                                    #define button 4
                            command = self.pulsante4Premuto)
    self.pulsante4.configure(text = "MI", background = "green")
    self.pulsante4.focus_force()
    
    self.pulsante4.configure(
      width = larghezza_pulsanti, 
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante4.pack(side = LEFT)
    self.pulsante4.bind("<Return>", self.pulsante4Premuto_a)







    self.pulsante5 = Button(self.quadro_pulsanti,                                  #define button 5
                            command = self.pulsante5Premuto)
    self.pulsante5.configure(text = "FA", background = "green")
    self.pulsante5.focus_force()
    
    self.pulsante5.configure(
      width = larghezza_pulsanti, 
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante5.pack(side = LEFT)
    self.pulsante5.bind("<Return>", self.pulsante5Premuto_a)




    self.pulsante6 = Button(self.quadro_pulsanti,                                  #define button 6
                            command = self.pulsante6Premuto)
    self.pulsante6.configure(text = "SOL", background = "green")
    self.pulsante6.focus_force()
    
    self.pulsante6.configure(
      width = larghezza_pulsanti, 
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante6.pack(side = LEFT)
    self.pulsante6.bind("<Return>", self.pulsante6Premuto_a)





    self.pulsante7 = Button(self.quadro_pulsanti,                                   #define button 7
                            command = self.pulsante7Premuto)
    self.pulsante7.configure(text = "LA", background = "green")
    self.pulsante7.focus_force()
    
    self.pulsante7.configure(
      width = larghezza_pulsanti, 
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante7.pack(side = LEFT)
    self.pulsante7.bind("<Return>", self.pulsante7Premuto_a)




    self.pulsante8 = Button(self.quadro_pulsanti,                                   #define button 8
                            command = self.pulsante8Premuto)
    self.pulsante8.configure(text = "SI", background = "green")
    self.pulsante8.focus_force()
    
    self.pulsante8.configure(
      width = larghezza_pulsanti, 
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante8.pack(side = LEFT)
    self.pulsante8.bind("<Return>", self.pulsante8Premuto_a)








    self.pulsante2 = Button(self.quadro_pulsanti,                                  #define button 2
                            command = self.pulsante2Premuto)
    self.pulsante2.configure(text = "Annulla", background = "red")
    self.pulsante2.configure(
      width = larghezza_pulsanti,  
      padx = imb_pulsantex,  
      pady = imb_pulsantey   
      )

    self.pulsante2.pack(side = RIGHT)
    self.pulsante2.bind("<Return>", self.pulsante2Premuto_a)


  def pulsante1Premuto(self):               #action of button 1
  
    arduino.write("a")

  def pulsante2Premuto(self):               #action of button 2
    self.mioGenitore.destroy() 

  def pulsante3Premuto(self):               #action of button 3
    
    arduino.write("s")
    
  def pulsante4Premuto(self):               #action of button 4
    
    arduino.write("d")
    
  def pulsante5Premuto(self):               #action of button 5
    
    arduino.write("f")

  def pulsante6Premuto(self):               #action of button 6
   
      arduino.write("g")

  def pulsante7Premuto(self):               #action of button 7
    
      arduino.write("h")

  def pulsante8Premuto(self):               #action of button 8
    
      arduino.write("j")

  def pulsante1Premuto_a(self, event):
    self.pulsante1Premuto()

  def pulsante2Premuto_a(self, event):
    self.pulsante2Premuto()
    
  def pulsante3Premuto_a(self, event):
    self.pulsante3Premuto()

  def pulsante4Premuto_a(self, event):    
    self.pulsante4remuto()
    
  def pulsante5Premuto_a(self, event):
    self.pulsante5Premuto()

  def pulsante6Premuto_a(self, event):
    self.pulsante6Premuto()

  def pulsante7Premuto_a(self, event):
    self.pulsante7Premuto()
    
  def pulsante8Premuto_a(self, event):
    self.pulsante8Premuto()

radice = Tk()
miaApp = MiaApp(radice)
radice.mainloop()
