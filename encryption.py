import time
import sys 
import threading as t



def encrypt(text):
  
       new_text=""
       
              
       alphabet = ["a","b", "c","d","e","f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
       cap_alpha=[x.upper() for x in alphabet]
       for i in text:
         if i in cap_alpha:
           new_text +=cap_alpha[25-cap_alpha.index(i)]
         elif i in alphabet:
            new_text +=alphabet[25-alphabet.index(i)]
         else:
           new_text +=i 
        
       lst.append(new_text)     
      

  
    
    


if __name__=="__main__":
    start_time = time.time()
    lst=[]
    try:
      file_path=sys.argv[1]
      with open(file_path,'r') as file:
           text=file.read()
    except IndexError:
        print("Please enter the text file name with extention after python file" )
    except FileNotFoundError:
        print("Please check the data file name and location.")   
    finally:    
        
        #encrypt(text)   
        
        n1=int(len(text)/4)

        t1 = t.Thread(target=encrypt, args=(text[0:n1],))
        t2 = t.Thread(target=encrypt, args=(text[n1:2*n1],))
        t3 = t.Thread(target=encrypt, args=(text[2*n1:3*n1],))
        t4 = t.Thread(target=encrypt, args=(text[3*n1:len(text)],))


        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join() 
        t3.join() 
        t4.join() 
     
        
        new_text="".join(lst)
        new_file ="Encrypt_"+file_path
        with open(new_file,'w') as file:
                     file.write(new_text)

        end_time = time.time()
        print (end_time-start_time)
          
          
   
   