"""

*********************************************************************************************************

The following code is written in Python (3.4.1)

*********************************************************************************************************

Author: Jahidul Hamid
Copyright: 2015, All rights reserved

*********************************************************************************************************

License: GPL v3+
This code is released under GPL v3+ License

*********************************************************************************************************

*******************************************************************
This project is under development stage
Any suggestion or modification to make it better is warmly welcome
*********************************************************************************************************

*********************************************************************************************************
Required features:

1. Any language(not just english) should be supported
2. Should be OS independent
3. Should be memory efficient
4. Should be as minimal as possible

Mechanism:

1. It first converts a php script to static html page: (php script.php)
2. Then it modifies the generated html page to convert it a fully working
and complete html by replacing markups as needed.
*********************************************************************************************************

"""

#########################################################################################################

import os,re,sys,unicodedata,platform,subprocess,shutil,errno

#########################################################################################################

##Global Variables:

src=""
dest=""



#########################################################################################################

print (platform.system()+"\n"+platform.release());

#########################################################################################################





#########################################################################################################
def processHTML(data,outfilepath):
  #with open(filepath, 'r') as file:
    #data = mmap.mmap(file.fileno(), 0,prot=mmap.PROT_READ)
    #file.close();
    #data=data[0:].decode("utf-8");
    data=data.encode("unicode-escape");
    #print(data);
    #print(line.decode("unicode-escape"));
    out= re.findall( b"<[\s\\\\t\\\\n]*a[\s\\\\t\\\\n]+[][\\\\\s\w\\\\./+@\"'=:,;~&^$-]*[\s\\\\t\\\\n]*href[\s\\\\t\\\\n]*=[\s\\\\t\\\\n]*\"[\s\\\\t\\\\n]*(?!http://)(?!www.)[][\\\\\s\w\\\\./+@\"':,;~&^$-]+\.php", data);
    data=data.decode("unicode-escape");
    if out:
      #print ("search --> out.group() : ", out);
      for match in out:
         string=match.decode("unicode-escape");
         print(string);
         newstring=string[0:len(string)-3]+"html";
         data=data.replace(string,newstring)
         #print(data);
      print("*****Success!****")
    else:
      print ("Nothing to be done!!");
    outfile=open(outfilepath,"w");
    outfile.write(data);
    outfile.close();
#########################################################################################################      
  
  
  
  
  
#########################################################################################################  
def runPHP(src):
    if(src[len(src)-4:]==".php"):
        
        src=os.path.abspath(src)
        dest=src[0:len(src)-3]+"html"
        os.chdir(os.path.dirname(src))
        proc = subprocess.Popen("php "+src, shell=True, stdout=subprocess.PIPE)
        output = proc.stdout.read().decode("utf-8")
        #print(output);
        #outfile=open(dest,"w");
        #outfile.write(output);
        print("*****PHP ran successfully*****")
        processHTML(output,dest)
    else:
        print("-----php file not found, skipped-----")
#########################################################################################################





#########################################################################################################
def parseLinuxHome(path):
    if(platform.system()=="Linux"):
       #print("reached");
       pattern=re.compile("~.*");
       if(pattern.match(path)):
          from os.path import expanduser;
          home = expanduser("~");
          path=home+path[1:];
          #print("*****Path: "+path+"*****");
    return path;
#########################################################################################################





#########################################################################################################
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)
            sys.exit()
#########################################################################################################





#########################################################################################################

def clean(dest):
  for subdir, dirs, files in os.walk(dest):
    for file in files:
        if(file[len(file)-4:]==".php"):
            filepath=os.path.join(subdir, file)
            filepath=os.path.abspath(filepath)
            os.remove(filepath)





#########################################################################################################





#########################################################################################################

def getInput():
  global src,dest
  while(True):
    src=input("Enter source path: ")
    src=src.strip("\r\n")
    src=parseLinuxHome(src)
    src=os.path.abspath(src)
    if(os.path.exists(src)):
         
         print("*****Found: "+src)
         break;
    else:
         print("Source path doesn't exist")
         
  while(True):
    dest=input("Enter destination directory: ")
    dest=dest.strip("\r\n")
    dest=parseLinuxHome(dest)
    dest=os.path.abspath(dest)
    if not os.path.isdir(dest):
         if (dest==src):
             print("src and destination can't be same")
         else:
             print("*****Project will be saved in: "+dest);
             break;
    else:
         print("Error: Destination directory exists")
#########################################################################################################




#########################################################################################################          

def startConvert(dest):
  for subdir, dirs, files in os.walk(dest):
    for file in files:
        if(file[len(file)-4:]==".php"):
            filepath=os.path.join(subdir, file)
            subdir=os.path.abspath(subdir)
            filepath=os.path.abspath(filepath)
            #print (filepath)
            #html=filepath[0:len(filepath)-3]+"html"
            #os.chdir(subdir)
            runPHP(filepath)
            #print(html);
            os.chdir(dest)
             



#########################################################################################################

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################

"""
Now the main task will begin
"""

#Get input from user: source path and destination path
getInput();

#Copy source to destination: We will not make any cahnges to source
copy(src,dest)

#Start conversion process
startConvert(dest)

#Clean (remove php files)
clean(dest)













