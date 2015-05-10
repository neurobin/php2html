# php2html
**********************
PHP to HTML converter
**********************

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

For windows, a setup.exe file is provided which can be run to install it. You might need to reboot once, after completing installation to use it from commmand prompt (cmd). No reboot is needed to run it from desktop launcher.

##How to use:

Both Windows and Linux versions of this tool can be used the same way. It can be run with cmd in windows and with terminal emulator in Linux.

     Usage: php2html [options]
   
     options are optional
     options: src dest -q -h --help -o --inplace -v --version
   
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
   
     --inplace is a dangerous option and should be avoided
     This replaces all the PHP files to resulting HTML file
     in the source directory. This doesn't require the option dest,
     neither it will prompt for it, and if dest is given as
     command line argument, it will simply ignore that
     
     -v or --version shows version information
   
     Example:
     php2html
     php2html -q src dest
     php2html src -q dest
     php2html src dest -q
     php2html src dest -q -o
     or if you are in windows, simply run the desktop launcher

##Disclaimer:

This project emerged from personal needs. I like to write webpages with PHP and host most of my project related pages on github while am not particularly interested on using Jekyll. That's the main reason I wrote this script on the first place, to do the conversion from PHP to HTML. So this may not meet the standard needs of most of the PHP web developers out there.

It comes with a copy of GPL v3 License with no warranty of any kind, so use with care.


##Contribute:

If you are a developer, you can consider contributing to this project by forking this repository and making changes for better and do a pull request, or sharing ideas and suggestions or finding bugs, anything at all, what you think will be beneficial for this project.

If you aren't a developer, but still want to contribute, then you can support the contributing developers spiritually, by starring the repository and sharing ideas. If you want to be notified of the continuous development, you can add this in your watch list in github.

If you find any problems or bugs please open an issue at https://github.com/neurobin/php2html/issues


