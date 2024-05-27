# TEMA_DE_CASA_AD


Prerequisites:

Assuming that you use Windows 10/11 you could run successfully the application.
In order to run the main application you have to accomplish some basic things before:




Installing Part :

-	Install Python/Check if Python is installed on your machine(preferably, 64bit version, and Python 3.10.4 or above, otherwise it will probably not work),


      The link for Python 3.10.4 is : 
        https://www.python.org/downloads/release/python-3104/
    
      The tutorial for installing it is :
 	    https://phoenixnap.com/kb/how-to-install-python-3-windows

-	Install C on your computer:
  
      Tutorial : https://code.visualstudio.com/docs/cpp/config-mingw


-	Install Visual Studio Code as code editor for this application, setup C compiler and Python Interpreter(Make sure both of the languages are declared globally into “Edit System Environment Variables”, otherwise the compilation and debugging process will not work). Of course, you can run the project in other code editors, environments, IDEs and other applications, but be sure that the files are linked between them. 

    Link for Visual Studio Code( be sure that you choose Windows and 64bit) : 
        https://code.visualstudio.com/download

-	Install Latex on your computer, using this tutorial(it is another form of latex, good for windows) : https://miktex.org/howto/install-miktex

-	For Latex, install also strawberry Perl in order to compile the latex part of the project(I recommend install “.msi” package) : 
        https://strawberryperl.com/

After you accomplished the tasks above, you need to install the required python modules that I’ve used in my project.

First, open you Command Prompt.
You will use the commands below, and you will run them one by one into the Command Prompt :

    pip install tkinter
    pip install customtkinter
    pip install numpy
    pip install matplotlib
    pip install pandas
    pip install pylatex

NOTE : You will see that in my project I have more modules than these. However, they are coming preinstalled on your machine, when you install python.





Running Part : 

In order to run it into Visual Studio Code, You will open the folder that contains the application, and run “main.py”.
This file will open a GUI window with multiple buttons :
-	Generate Data(will generate a csv files with random sets of data, before be sure you input correct values into the Data input window that is generated when clicking the button)
-	Results(Here another window will appear, when clicking on the Py button you will see the chart with python data, and after you close the chart you will see the output text file data)
-	Technical Report(this button will open the technical report)
-	Github Repository(This button will open the online github repository)
-	HELP( this will open README.md from the online github repository)

NOTE : When you click on a button be sure you finish the operation and start another one… It is recommended to do that to avoid any errors related to CPU processes.

And the operations from the “main.py” GUI window, please do them exactly as the order from above, again just to avoid any errors, and just to be safe.

**DOUBLE NOTE You will see another subdirectory into the root folder, which is called “experimental_data”.
There I tested the 10 testcases for the “technical_report.pdf”,using another files for reading 10 csv files separately… with one testcase each.
If you want, you can compile the files from “experimental_data” folder, but be sure you are linking them, as I said on the first page.
***TRIPLE NOTE : When you want to test my application, take into consideration that can handle only a csv file at a run … You can generate as many csv files as you want, but the scripts will take for analyzing just the last created.

*However… If you want to run the files into the Command Prompt, then you will use : 

First, be sure that you are into the root directory of the application : 

Use “cd” command to enter the root directory (for me it’s TEMA_DE_CASA_AD, assuming that you know already where is the root folder, you have to link also the general Destination first… For example: if you have the root directory into Downloads, you will use cd to enter into Downloads folder):

    cd TEMA_DE_CASA_AD

Now, you are in the root folder.

Then, if you want to test the main application you just run(exactly as below) :
  python main.py 
After this you just use the application, assuming that you understood all instructions from above.

**If you want to test the experimental data(assuming that you are in root folder of your project, otherwise use cd to enter your root folder):


     cd experimental_data

     python results.py 
(we compute data through python and output it into the the “results_py.txt”)


     gcc results.c -o results.exe
  (we compute data through C and output it into the the “results_c.txt”)

     python results_c_chart.py
   (here I make the charts for the C algorithm, in python the part with created the function it was implemented, but in C I have to use python to make those charts… it is easier than looking and implementing a chart library in C)


    python technical_report.py     
(only if you want to recompile the technical report, but it is not mandatory, use it only if you accidentally deleted “technical_report.pdf”)



  For other problems, please send me an e-mail : necsulea.andrei.h7u@student.ucv.ro
=

