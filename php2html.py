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

import os,re,sys,unicodedata,platform,subprocess,shutil,mmap
import imp,random
try:
    import readline
except ImportError:
    import pyreadline as readline



#########################################################################################################
histfile = os.path.join(os.path.expanduser("~"), ".php2html_hist")
try:
    readline.read_history_file(histfile)
except IOError:
    pass
import atexit
atexit.register(readline.write_history_file, histfile)
del histfile
#########################################################################################################

##Global Variables:

src=""
dest=""

###Options
showversion=False
verbose=True
overwrite=False
inplace=False
accessFile=".htaccess"
reserveDirectoryStructure=False

###

###Default PHP command
phpCommand="php"

###
productVersion="3.0.0"

##

##ignore directories and files, these directories and files won't be copied
ignoreDirPatterns=[".git"]
ignoreFilePatterns=[]

##

#########################################################################################################





#########################################################################################################
def showVersionInfo():
    print("""Name: php2html
Version: """+productVersion+"""
Description: PHP To HTML Converter
Categories: Development
Author: Neurobin
AuthorFullName: Jahidul Hamid
Lincense: GPL v3
Bug report URL: https://github.com/neurobin/php2html/issues""")







#########################################################################################################





#########################################################################################################
def parseLinuxHome(path):
    if(platform.system()=="Linux"):
       pattern=re.compile("~.*");
       if(pattern.match(path)):
          from os.path import expanduser;
          home = expanduser("~");
          path=home+path[1:];
    return path;
#########################################################################################################






#########################################################################################################
def parseArgs():
  global src,dest,verbose,overwrite,inplace,reserveDirectoryStructure,accessFile
  count=0
#########################################################

  #Exclusive for loop, trying to find VIP options
  for i in range(len(sys.argv)):
    if(sys.argv[i]=="-h" or sys.argv[i]=="--help"):
        help()
        sys.exit()
  for i in range(len(sys.argv)):
    if(sys.argv[i]=="-v" or sys.argv[i]=="--version"):
        showVersionInfo()
        sys.exit()
#########################################################

#########################################################
  #Trying to find general options 
  for i in range(len(sys.argv)):
        
    if(sys.argv[i]=="-q"):
        verbose=False 
        continue
        
    if(sys.argv[i]=="-i"):
        inplace=True 
        continue
        
    if(sys.argv[i]=="-o"):
        overwrite=True 
        continue
    if(re.match("-a",sys.argv[i])):
        accessFile=sys.argv[i][2:]
        continue
        
    if(re.match("-rd",sys.argv[i])):
        reserveDirectoryStructure=True
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
#########################################################


#########################################################################################################


#########################################################################################################

def help():
   print("""\n\n*******************************************
   
   php2html : Version """+productVersion+"""
   
   Usage: php2html [options]
   
   options are optional
   options: src dest -q -h --help -o -i -v --version -a.htaccess -rd
   
   src is the source path
   
   dest is the destination directory
   
   -q means quite (won't print any output other than errors)
   -q can be placed anywhere in the
   argument sequence.
   
   -h shows this help menu
   --help shows this help menu
   
   -o overwrites destination directory
   This mode is not dependent on the existance of destination
   directory
   
   -i is a dangerous option and should be avoided
   This replaces all the PHP files to resulting HTML file
   in the source directory. This doesn't require the option dest,
   neither it will prompt for it, and if dest is given as
   command line argument, it will simply ignore that
   
   -v or --version shows version information
   
   -a.htaccess processes the .htaccess file.
   Other access file can be processed by changing the
   .htaccess part to the actual name of the used AccessFile.
   There must not be any white space between -a and .htaccess
   If you pass only -a, it will neither look for any AccessFile and
   nor it will try to process them
   
   If you don't pass -a as an option, it will look for .htaccess file
   by default
   
   -rd reserve Directory Structure. By default empty directory will not
   be copied to the destination directory. If -rd is specified, empty directory
   will also be copied to the destination to preserve directory structure
   
   Example:
   php2html
   php2html -q src dest
   php2html src -q dest
   php2html src dest -q
   php2html src dest -q -o            #this and above takes .htaccess by default as the access file
   php2html src dest -q -o -a         #This one ignores any accessfile
   php2html src dest -q -o -a.config  #This one takes .config as AccessFile
   
********************************************\n""")


#########################################################################################################





#########################################################################################################
def processHTML(data,outfilepath):
    data=data.encode("unicode-escape");
    out= re.findall( b"<[\s\\\\t\\\\n]*a[\s\\\\t\\\\n]+[][\\\\\s\w\\\\./+@\"'=:,;~&^$-]*[\s\\\\t\\\\n]*href[\s\\\\t\\\\n]*=[\s\\\\t\\\\n]*\"[\s\\\\t\\\\n]*(?!http://)(?!www.)[][\\\\\s\w\\\\./+@\"':,;~%&^$-]+\.php", data);
    data=data.decode("unicode-escape");
    if out:
      for match in out:
         string=match.decode("unicode-escape");
         #print(string);
         newstring=string[0:len(string)-3]+"html";
         data=data.replace(string,newstring)
         #print(data);
      if(verbose):print("*****HTML Parsing: Success *****")
    else:
      if(verbose):print("*****HTML Parsing: Everythings OK..Nothing to be done!!...skipped...");
    outfile=open(outfilepath,"w");
    outfile.write(data);
    if(data!=""):
        if(verbose):print("*****Created file: "+outfilepath+"\n");
    else:
        if(verbose):print("-----Created empty file: "+outfilepath+"\n");
    outfile.close();
#########################################################################################################      




#########################################################################################################
def processAccessFile(srcfile,outfilepath):
    with open(srcfile, 'r') as f:
        data = mmap.mmap(f.fileno(), 0,prot=mmap.PROT_READ)
        data=data[0:].decode("utf-8")
        out = re.findall(r"(?!http://)(?!www.)[][ \t\w\./+@\"':,;~%&^$-]+\.php", data)
        if out:
            for match in out:
                string=match;
                newstring=string[0:len(string)-3]+"html";
                data=data.replace(string,newstring)
            if(verbose):print("*****AccessFile Parsing: Success *****")
        else:
            if(verbose):print("*****AccessFile Parsing: Everythings OK..Nothing to be done!!...skipped...");
        outfile=open(outfilepath,"w");
        outfile.write(data);
        if(data!=""):
            if(verbose):print("*****Created file: "+outfilepath+"\n");
        else:
            if(verbose):print("-----Created empty file: "+outfilepath+"\n");
        outfile.close();
#########################################################################################################




#########################################################################################################

def getYesNo():
    yn=input("[Y/n]: ")
    if(yn=="Y" or yn=="y"):
        return True
    else:
        return False
        
def checkDefaultPHP():
    global phpCommand
    if(platform.system()!="Windows"):
        try:
            proc = subprocess.Popen("which"+" "+phpCommand, shell=True, stdout=subprocess.PIPE)
            output = proc.stdout.read().decode("utf-8")
            if(output!=""):
                phpCommand="php"
            else:
                phpCommand=""
            
        except:
            phpCommand=""
            
    if(platform.system()=="Windows"):
        winphp=["C:\\wamp\\bin\\php\\php5.5.12\\php.exe"]
        for i in winphp:
            if os.path.exists(i):
                if not os.path.isdir(i):
                    phpCommand=i
                    break
                else:
                    phpCommand=""
            else:
                phpCommand=""
        

def getCustomPHPCommand():
    print("-----PHP wasn't found on this system-----")
    while True:
        path=input("Enter PHP executable path: ")
        if os.path.exists(path):
            if not os.path.isdir(path):
                path=os.path.abspath(path)
                break
            else:
                print("Error: This is a directory")
                path=""
        else:
            print("Error: File not found")
            path=""
    return path

def getPHPCommandBySearch():
    global phpCommand
    if(platform.system()=="Windows"):
        if(verbose):print("Trying to find PHP, if installed")
        lookfor = "php.exe"
        for root, dirs, files in os.walk(os.path.abspath(os.sep)):
            if ":\\Users" in root:
                continue
            if(verbose):print("Searching on: ", root)

            if lookfor in files:
                phpCommand=os.path.join(root, lookfor)
                if(verbose):print("\n\n*****Found: "+phpCommand)
                if(verbose):
                    print("You need to confirm that the php path is correct")
                    if not getYesNo():
                        phpCommand=getCustomPHPCommand()
                break
    if(platform.system()!="Windows"):
        print("Trying to find PHP, if installed")
        lookfor = "php"
        for root, dirs, files in os.walk(os.path.abspath(os.sep)):
            if lookfor in files:
                phpCommand=os.path.join(root, lookfor)
                print("\n\n*****Found: "+phpCommand)
                print("You need to confirm that the php path is correct")
                if not getYesNo():
                        phpCommand=getCustomPHPCommand()
                break 
                
    if(phpCommand==""):
        phpCommand=getCustomPHPCommand()

            
def getPHPCommand():
    global phpCommand
    checkDefaultPHP()
    if(phpCommand==""):
        if(platform.system()!="Windows"):
            print("Error: PHP wasn't found")
            print("Want to enter PHP executable path? if not I will search for it")
            if getYesNo():
                phpCommand=getCustomPHPCommand()
            else:
                getPHPCommandBySearch()
                
        if(platform.system()=="Windows"):
            if(verbose):
                print("Error: PHP wasn't found")
                print("Want to enter PHP executable path? if not I will search for it")
                if getYesNo():
                    phpCommand=getCustomPHPCommand()
                else:
                    getPHPCommandBySearch() 
            if not verbose:
                getPHPCommandBySearch()






#########################################################################################################
  
  
  
  
  
#########################################################################################################  
def runPHP(src,dest):
    global phpCommand
    if not "php" in phpCommand:
        print("Error: PHP command isn't valid, Exiting..")
        sys.exit()
    if(src[len(src)-4:]==".php"):
        src=os.path.abspath(src)
        htmlfilename=os.path.basename(src)[0:len(os.path.basename(src))-3]+"html"
        destfile=os.path.join(dest,htmlfilename)
        os.chdir(os.path.dirname(src))
        proc = subprocess.Popen(phpCommand+" "+src, shell=True, stdout=subprocess.PIPE)
        output = proc.stdout.read().decode("utf-8")
        if(output!=""):
            if(verbose):print("*****Running PHP: Success *****")
        else:
            if(verbose):print("-----Running PHP: PHP returned an empty result!!-----")
        processHTML(output,destfile)
    else:
        if(verbose):print("-----This file is not a valid PHP file, skipped-----")
#########################################################################################################







#########################################################################################################

def createEmptyTree(src, dest):
    global ignoreDirPatterns
    src_prefix = len(src) + len(os.path.sep)
    for root, dirs, files in os.walk(src):
        for pattern in ignoreDirPatterns:
            if pattern in root:
                break
        else:
            #If the above break didn't work, this part will be executed
            for dirname in dirs:
                for pattern in ignoreDirPatterns:
                    if pattern in dirname:
                        break
                else:
                    #If the above break didn't work, this part will be executed
                    dirpath = os.path.join(dest, root[src_prefix:], dirname)
                    try:
                        os.makedirs(dirpath,exist_ok=True)
                    except OSError as e:
                        print("Error: Couldn't create directory "+dirpath)
                continue;#If the above else didn't executed, this will be reached
            
        continue;#If the above else didn't executed, this will be reached



#########################################################################################################





#########################################################################################################

def clean(dest):
  if(verbose):print("\n*****Cleaning*****")
  for subdir, dirs, files in os.walk(dest):
    for file in files:
        if(file[len(file)-4:]==".php"):
            filepath=os.path.join(subdir, file)
            filepath=os.path.abspath(filepath)
            os.remove(filepath)
  if(verbose):print("*****done*****")





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
  if(dest=="" and inplace==False):       
     while(True):
        dest=input("Enter destination directory: ")
        dest=dest.strip("\r\n")
        dest=parseLinuxHome(dest)
        dest=os.path.abspath(dest)
        if not overwrite:
            if not os.path.exists(dest):
                if (dest==src):
                    print("Error: Source and destination can't be the same\n Use -i option if you want to replace/overwrite source")
                else:
                    if(verbose):print("*****Project will be saved in: "+dest);
                    break;
            else:
                print("Error: Destination directory exists")
                
        else:
            if (dest==src):
                print("Error: Source and destination can't be the same\nUse -i option if you want to replace/overwrite source")
            else:
                break
#########################################################################################################




#########################################################################################################          

def startConvert(src,dest):
    global ignoreDirPatterns,ignoreFilePatterns
    if(verbose):print("Starting conversion process.....\n\n")
    src_prefix = len(src) + len(os.path.sep)
    for root, dirs, files in os.walk(src):
        for pattern in ignoreDirPatterns:
            if pattern in root:
                break
        else:
            #If the above break didn't work, this part will be executed
            for file in files:
                for pattern in ignoreFilePatterns:
                    if pattern in file:
                        break
                else:
                    #If the above break didn't work, this part will be executed
                    dirpath = os.path.join(dest, root[src_prefix:])
                    if not reserveDirectoryStructure:
                        try:
                            os.makedirs(dirpath,exist_ok=True)
                        except OSError as e:
                            print("Error: Couldn't create directory "+dirpath)
                    filepath=os.path.join(root,file)
                    if(file[len(file)-4:]==".php"):
                        filepath=os.path.abspath(filepath)
                        runPHP(filepath,dirpath)
                        os.chdir(dest)
                    elif(file==accessFile):
                        processAccessFile(filepath,os.path.join(dirpath,file))
                    else:
                        if(src!=dest):
                            shutil.copy(filepath,dirpath)
                continue;#If the above else didn't executed, this will be reached
            
        continue;#If the above else didn't executed, this will be reached
             



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


##Check For PHP installation
getPHPCommand()



if(verbose):
    print ("\n\n******Operating System: "+platform.system()+"\n******Release: "+platform.release());
    print("""\n\n****************php2html: Version """+productVersion+""" **********************
**************************Lexicon**************************
***** means Success message
----- means Warning message
Error: means Error
***********************************************************\n\n""")

#########################################################################################################

"""
Now the main task will begin
"""
##Check if dest is passed in command line argument, must be before getInput()
if(os.path.isdir(dest)==True and overwrite==False ):
    dest=""
elif(os.path.exists(dest)):
    if not os.path.isdir(dest):
        print("Error: Invalid argument, Destination must be a directory...")
        dest=""
if(src==dest and inplace==False):
    dest=""
    
if not isSingleMode():
    getInput();
    #Create directory structure if reserveDirectoryStructure=True
    if(reserveDirectoryStructure):createEmptyTree(src,dest)

    if not inplace:
        startConvert(src,dest)
    else:
        startConvert(src,src)
        clean(src)
    
else:
    #if single file mode is true:
    runPHP(src,os.path.dirname(src))
