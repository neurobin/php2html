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
Targeted features:

1. Any language(not just english) should be supported (in php scripts)
2. Should be OS independent
3. Should be memory efficient
4. Should be as minimal as possible

Mechanism:

1. It first converts a PHP script to static html page: (php script.php)
2. Then it modifies the generated HTML page to convert it to a fully working
and complete HTML by replacing markups as needed.
*********************************************************************************************************

"""

#########################################################################################################

import os,re,sys,unicodedata,platform,subprocess,shutil,errno

#########################################################################################################

##Global Variables:

src=""
dest=""
verbose=True

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
def parseArgs():
  global src,dest,verbose
  count=0
  #Exclusive for loop, trying to find VIP options
  for i in range(len(sys.argv)):
    if(sys.argv[i]=="-h" or sys.argv[i]=="--help"):
        help()
        sys.exit()
  #Trying to find general options 
  for i in range(len(sys.argv)):
        
    if(sys.argv[i]=="-q"):
        verbose=False 
        continue
    
    if(count==0 and i>0):
        count+=1;
        src=sys.argv[i]
        src=parseLinuxHome(src)
        src=os.path.abspath(src)
        if not os.path.exists(src):
            print("Error: Source path doesn't exist")
            src=""
        
    elif(count==1 and i>0):
        count+=1
        dest=sys.argv[i]
        dest=parseLinuxHome(dest)
        dest=os.path.abspath(dest)      
        if os.path.exists(dest):
            print("Error: Destination directory exists")
            dest=""



#########################################################################################################


#########################################################################################################

def help():
   print("""\n\n*******************************************
   php2html : version 1.0
   
   Usage: php2html [options]
   
   options are optional
   options: src dest -q -h --help
   
   src is the source path
   
   dest is the destination directory
   
   -q means quite (won't print any output other than errors)
   -q can be placed anywhere in the
   argument sequence.
   
   -h shows this help menu
   --help shows this help menu
   
   Example:
   php2html
   php2html -q src dest
   php2html src -q dest
   php2html src dest -q
   
   For windows, php2html would be php2html.exe
********************************************\n""")


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
      for match in out:
         string=match.decode("unicode-escape");
         #print(string);
         newstring=string[0:len(string)-3]+"html";
         data=data.replace(string,newstring)
         #print(data);
      if(verbose):print("*****HTML Parsing: Success!****")
    else:
      if(verbose):print ("*****HTML Parsing: Everythings OK..Nothing to be done!!...skipped...");
    outfile=open(outfilepath,"w");
    if(verbose):print ("*****Creating file: "+outfilepath+"\n");
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
        if(verbose):print("*****Running PHP: Success*****")
        processHTML(output,dest)
    else:
        if(verbose):print("-----This file is not a valid PHP file, skipped-----")
#########################################################################################################







#########################################################################################################
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Error: Directory not copied. %s' % e)
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
  if(src==""):
     while(True):
        src=input("Enter source path: ")
        src=src.strip("\r\n")
        src=parseLinuxHome(src)
        src=os.path.abspath(src)
        if(os.path.exists(src)):
             if(verbose):print("*****Found: "+src)
             break;
        else:
             print("Error: Source path doesn't exist")
  if(dest==""):       
     while(True):
        dest=input("Enter destination directory: ")
        dest=dest.strip("\r\n")
        dest=parseLinuxHome(dest)
        dest=os.path.abspath(dest)
        if not os.path.exists(dest):
             if (dest==src):
                 print("Error: Source and destination can't be the same")
             else:
                 if(verbose):print("*****Project will be saved in: "+dest);
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
def isSingleMode():
    global src,dest
    if(src!=""):
        if not os.path.isdir(src):
            return True
        else:
            return False
    else:
        return False
        

#########################################################################################################

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################

#*******************************************************************************************************#
#Parse Arguments
parseArgs()

#*******************************************************************************************************#

if(verbose):
    print ("\n\n******Operating System: "+platform.system()+"\n******Release: "+platform.release());
    print("""\n\n****************php2html: version 1.0**********************
**************************Lexicon**************************
***** means Success message
----- means Warning message
Error: means Error
***********************************************************\n\n""")

#########################################################################################################

"""
Now the main task will begin
"""
if not isSingleMode():
    #if single file mode is false:
    #Get input from user: source path and destination path
    getInput();

    #Copy source to destination: We will not make any cahnges to source
    copy(src,dest)

    #Start conversion process
    startConvert(dest)

    #Clean (remove php files)
    clean(dest)
    
else:
    #if single file mode is true:
    runPHP(src)













