# php2html
**********************
PHP to HTML converter
**********************

This is a simple script/tool written in python (3.4) to convert PHP scripts to static HTML pages. The goal is to convert entire PHP website
residing in localhost to a static HTML website. This convertion can be done on an entire website as well as on a single PHP script. Website
residing in localhost isn't necessary to perform the conversion, rather it is necessary to have the PHP scripts/website locally.

Mechanism:

The system on which this tool will be run, must have PHP installed. It executes every PHP script with the system PHP environment and 
parses the output to replace markups as required and produces .html for each .php.

Install:

The script can be run without installing if python3.4 is available:
    python3.4 php2html.py options

The tool can be installed by running the install file provided in any Linux System.
    chmod +x install
    ./install   //or simply drag and drop the file on terminal

How to use:

     Usage: php2html [options]
   
     options are optional
     options: src dest -q -h --help
   
     src is the source path
   
     dest is the destination directory
   
     -q means quite (won't print any output other than errors)
     -q can be placed anywhere in the
     argument sequence.
   
     -h shows help menu
     --help shows help menu
   
     Example:
     php2html
     php2html -q src dest
     php2html src -q dest
     php2html src dest -q

Disclaimer:

This project emerged from personal needs. I like to write webpages with PHP and I host most of my project related pages on github and I
don't want to write my codes with Jekyll. That's the reason I wrote this script to do the convertion from PHP to HTML for me.
So this may not meet the standard needs of most PHP developers out there. And it comes with a copy of GPL v3 License with no warranty
of any kind, so use with care.


Contrubute:

If you are a developer, you can consider contributing to this project by forking this repository and making changes for better and
do a pull request, or sharing ideas and suggestions or finding bugs, anything at all, what you think will be beneficial for
 this project.

If you aren't a programmer or developer, but still want to contribute, then you can support the contributing developers spiritually, 
by starring the reporitory. If you want to be notified of the continuous development, you can add this in your watch list in github.

If you find any problems or bugs please open an issue at https://github.com/neurobin/php2html/issues


