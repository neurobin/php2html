This is a simple script/tool written in python (3.4) to convert PHP scripts to static HTML pages. The goal is to convert an entire PHP website residing in localhost to a static HTML website. This conversion can be done on a directory containing a website as well as on a single PHP script. Website residing in localhost isn't necessary to perform the conversion, rather it is necessary to have the PHP scripts/website locally.

##Mechanism:

The system on which this tool will be run, must have PHP installed. It executes every PHP script with the system PHP environment and parses the output to replace markups as required and produces .html for each .php.

##Install:

The script can be run without installing if python3.4 is available:

      python3.4 php2html.py options
      
###On Linux:

The tool can be installed by running the install file provided, in any Linux System:

      chmod +x install
      ./install   //or simply drag and drop the file on terminal
      
###On Windows:

For windows, a setup.exe file is provided which can be run to install it. You might need to reboot once after completing installation, to use it from commmand prompt (cmd). No reboot is needed to run it from desktop launcher.

##How to use:

Both Windows and Linux versions of this tool can be used the same way. It can be run with cmd in windows and with terminal emulator in Linux.

In Windows it can be run from Desktop Launcher too.

###Simple Usage:

     php2html phpscript.php

###Advanced Usage: 

     php2html [options]
   
     options are optional
     options: src dest -q -h --help -o -i -v --version -a -rd
   
     src is the source path
   
     dest is the destination directory
     
     src and dest are sequential, all other options can be placed
     anywhere in the argument sequence
   
     -q means quite (won't print any output other than errors)
   
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
     php2html src dest -q -o            //this and above takes .htaccess by default as the access file
     php2html src dest -q -o -a         //This one ignores any accessfile
     php2html src dest -q -o -a.config  //This one takes .config as AccessFile
     
##Limitations:

 1. This tool only changes the relative PHP URLs to HTML URLs, no absolute URL is changed in any ways.
 2. It's recommended that you use JavaScript (`window.location.href` or such) to get the current location not PHP (`$_SERVER['PHP_SELF']`), if you are gonna use that URL in any link which you need to be converted to html link, otherwise it may produce unexpected results.
 3. Use relative URL path as much as you can. If any relative URL is specified with absolute path (with `http://` or `www`.), it will be ignored and won't be converted to HTML URL path.

##Disclaimer:

This project emerged from personal needs. I like to write webpages with PHP and host most of my project related pages on github while am not particularly interested on using Jekyll. That's the main reason I wrote this script on the first place, to do the conversion from PHP to HTML. So this may not meet the standard needs of most of the PHP web developers out there.

It comes with a copy of GPL v3 License with no warranty of any kind, so use with care.


##Contribute:

If you are a developer, you can consider contributing to this project by forking this repository and making changes for better and do a pull request, or sharing ideas and suggestions or finding bugs, anything at all, what you think will be beneficial for this project.

If you aren't a developer, but still want to contribute, then you can support the contributing developers spiritually, by starring the repository and sharing ideas. If you want to be notified of the continuous development, you can add this in your watch list in Github.

If you find any problems or bugs please open an issue [here](https://github.com/neurobin/php2html/issues) 



