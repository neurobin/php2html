<div id="description"></div>
This is a simple script/tool written in **python (3.4)** to convert PHP scripts to static HTML pages. The goal is to convert an entire PHP website residing in localhost to a static HTML website altogether. This conversion can be done on a directory containing a website as well as on a single PHP script.

<div id="mechanism"></div>
##Mechanism:

The system on which this tool will be run, must have PHP installed. It executes every PHP script with the system PHP (CLI) environment and parses the output to replace markups as required and produces <span class="quote">.html</span> for each <span class="quote">.php</span>.

<div id="install"></div>
##Install:

The script can be run without installing if python3.4 is available:
```bash
./php2html
```
###On Unix/Linux:

The tool can be installed by running the install file provided, in any Linux System:
```bash
chmod +x install
./install   #Must be run within the package directory (with `./` at the beginning)
```      

Or just copy the `php2html` script to `/usr/bin`

###On Windows:

For windows, You can rename the file with a `.py` extension and run it within python environment. Or you can use <a href="https://pypi.python.org/pypi/cx_Freeze">cxfreeze</a> to make a binary build for standalone executable. I may not provide any binary build of this tool anymore.

<div id="how-to-use"></div>
##How to use:

Both Windows and Linux versions of this tool can be used the same way (In windows make sure to add the executable path in the PATH environment variable). It can be run with cmd in windows and with terminal emulator in Linux.


###Simple Usage:
```bash
php2html phpscript.php
php2html . destination_directory  # This will convert entire site in current directory to html
```
>Always run this command from within the Document Root of your website (`public_html` or `www` or whatever it is), otherwise unexpected results might occur.

###Advanced Usage: 

Usage: `php2html src dest [options]`
   
options: src dest -q -h --help -o -i -v --version -a.htaccess -rd
   
`src`         : the source path.
                 src can not be a directory other than current directory,
                 to pass current directory as src, either use . or ./
   
`dest`        : the destination directory.
   
`-q`          : means quite (won't print any output other than errors)
`-q`          : can be placed anywhere in the argument sequence.
   
`-h`          : shows this help menu
`--help`      : shows this help menu
   
`-o`          : overwrites destination directory
                 This mode is not dependent on the existance of destination
                 directory
   
`-i`          : is a dangerous option and should be avoided
                 This replaces all the PHP files to resulting HTML file
                 in the source directory. This doesn't require the option dest,
                 neither it will prompt for it, and if dest is given as
                 command line argument, it will simply ignore that
   
`-v`          : shows version information
`--version`   : shows version info
   
`-a.htaccess` : processes the .htaccess file.
                 Other access file can be processed by changing the
                .htaccess part to the actual name of the used AccessFile.
                 There must not be any white space between -a and .htaccess
                 If you pass only -a, it will neither look for any AccessFile and
                 nor it will try to process them.
                 If you don't pass -a as an option, it will look for .htaccess file
                 by default
   
`-rd`         : reserve Directory Structure. By default empty directory will not
                 be copied to the destination directory. If -rd is specified, empty directory
                 will also be copied to the destination to preserve directory structure
   
`-ed`         : Exclude directory. The directory passed with this options won't be included
                 in new html site.
   
`-ef`         : Exclude file. The file specified by this option won't be included in new html site.
   
<div id="example"></div>

```
Example:
php2html
php2html . dest                        # . is the current dir
php2html -q src.php dest
php2html src.php -q dest
php2html src.php dest -q
php2html src.php dest -q -o            # This and above takes .htaccess by default as the access file
php2html src.php dest -q -o -a         # This one ignores any accessfile
php2html src.php dest -q -o -a.config  # This one takes .config as AccessFile
```

<div id="limitations"></div>
##Limitations:

 1. This tool only changes the relative PHP URLs to HTML URLs, no absolute URL is changed in any ways.
 2. It's recommended that you use JavaScript (`window.location.href` or such) to get the current location not PHP (`$_SERVER['PHP_SELF']`), if you are gonna use that URL in any link which you need to be converted to html link, otherwise it may produce unexpected results.
 3. If you want to use PHP variables: `$_SERVER['PHP_SELF']` or `$_SERVER['DOCUMENT_ROOT']` see the <a href="#tips-and-trics">tips & tricks</a> section.
 4. Use relative URL path as much as you can. If any relative URL is specified with absolute path (with `http://` or `www`.), it will be ignored and won't be converted to HTML URL path.



<div id="tips-and-trics"></div>
##Tips & Trics:

If you want to use `$_SERVER['PHP_SELF']` or `$_SERVER['DOCUMENT_ROOT']` in a page, add the following lines at the top of the page:

```
<?php 
error_reporting(E_ERROR | E_PARSE);
chdir(rtrim(dirname($_SERVER['PHP_SELF']),'/')); 
//These pieces of codes must be the top most lines of the page.
   $__CURDIR=dirname($_SERVER['PHP_SELF']);
   $__SELF=basename($_SERVER['PHP_SELF']);
   $pat='/(\/|^)[^\/]*/';
   $__CURDIR = preg_replace('/^\.\//', '', $__CURDIR);
   $__CURDIR = preg_replace('/^\//', '', $__CURDIR);
   if($__CURDIR=='.'||$__CURDIR=='./'||$__CURDIR=='/'||$__CURDIR=='')
   {$__RDOCROOT='./';$__CURDIR='./';}
   else {$__RDOCROOT=preg_replace($pat,'../',$__CURDIR);$__CURDIR.="/";}
   $__SELF=$__CURDIR.$__SELF;
   //$__RDOCROOT and $__CURDIR contains a / at end. It's necessary
?>
```

1. Now you can use `$__RDOCROOT` or `$GLOBALS['__RDOCROOT']` (inside a funcion, class or namespace) in place of `$_SERVER['DOCUMENT_ROOT']`.
2. `$__CURDIR` or `$GLOBALS['__CURDIR']` (inside a funcion, class or namespace) in place of `getcwd()` or current directory.
3. `$__SELF` or `$GLOBALS['__SELF']` (inside a funcion, class or namespace) in place of `$_SERVER['PHP_SELF']`.

All these new variables are relative paths not absolute ones.

<div id="disclaimer"></div>
##Disclaimer:

This project emerged from personal needs. I like to write webpages with PHP and host most of my project related pages on github while am not particularly interested on using Jekyll. That's the main reason I wrote this script on the first place, to do the conversion from PHP to HTML. So this may not meet the standard needs of most of the PHP web developers out there.

It comes with a copy of <span class="quote">GPL v3 License</span> with no warranty of any kind, so use with care.

<div id="contribute"></div>
##Contribute:

If you are a developer, you can consider contributing to this project by forking this repository and making changes for better and do a pull request, or sharing ideas and suggestions or finding bugs, anything at all, what you think will be beneficial for this project.

If you aren't a developer, but still want to contribute, then you can support the contributing developers spiritually, by starring the repository and sharing ideas. If you want to be notified of the continuous development, you can add this in your watch list in Github.

If you find any problems or bugs please open an issue [here](https://github.com/neurobin/php2html/issues) 

