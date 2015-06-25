                                     //defines the values of the notes
int vel = 500;    
int DO = 262;
int RE = 294;
int MI = 330;
int FA = 349;
int SOL= 392;
int LA =440;
int SI= 494;
int pin =13 ;                         //defines buzzer pin
char s = 0;                           //defines char who read to the serial port


void setup(){
pinMode(pin,OUTPUT);
Serial.begin(9600);                  //initialize serial port
}


  
void loop(){

   if(Serial.available()) {
   char  s = Serial.read();          // read to the serial port
 
   if (s=='a'){                      // compares letters 
   tone (pin,DO,vel);}               // write into arduino the note corresponding a letter
   
    if (s=='s'){
   tone (pin,RE,vel);}
  
    if (s=='d'){
   tone (pin,MI,vel);}
   
    if (s=='f'){
   tone (pin,FA,vel);}
   
    if (s=='g'){
   tone (pin,SOL,vel);}
   
    if (s=='h'){
   tone (pin,LA,vel);}
   
    if (s=='j'){
   tone (pin,SI,vel);}
   

}  
   
}
