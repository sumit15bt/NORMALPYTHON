fileptr = open("","a");     
#overwriting the content of the file  
fileptr.write("127.0.0.1	www.facebook.com")
print("written successfully...!!")  
#closing the opened file   
fileptr.close();  

with open("/etc/hosts",'r') as f:  
    content = f.read();  
    print(content)
