
# Virual_Desktop_Assistant
This program is a virtual desktop assistant which can perform different tasks without any physical contact by keyboard or mouse. It is controlled by your voice and you can enable it to perform different tasks by giving voice commands.

## [ Installation ]

Should have the following modules and libraries installed to run this program<br/>
➢ *Pyttsx3* (version 2.10.0) (text-to-speech conversion library)<br/>
➢ os (module to interact with operating system)<br/>
➢ SpeechRecognition (Library for performing speech recognition, with support for several engines and APIs)<br/>
➢ bs4 (library for pulling data out of HTML and XML files)<br/>
➢ requests (use to send all kinds of HTTP requests)<br/>
➢ datetime (module to manipulate date and time)<br/>
➢ random (random generator module) \ 
➢ ctypes (It provides C compatible data types, and allows calling functions in DLLs or shared libraries)<br/>
➢ google-search (Library for scraping google search results.)<br/>
➢ google (Python bindings to the google search engine)<br/>
➢ pyowm (client Python wrapper library for OpenWeatherMap web APIs)<br/>
➢ Wikipedia (library that makes it easy to access and parse data from Wikipedia.) \ ➢ Smtplib ( module which defines an SMTP client session object that can be used to send mail to any Internet machine)<br/>
➢ Pyaudio (PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library)<br/>
(First you have to install wheel file from https://www.lfd.uci.edu/~gohlke/pythonlibs/ then pip install (the name of the version you have downloaded). In case of 64-bit python 3.8 write in terminal pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl ).<br/>

## [ Features ]

1. It can perform Wikipedia search.<br/>
2. It can extract google search results.<br/>
3. It will tell you latest daily google headlines.<br/>
4. It can make you laugh by telling random jokes.<br/>
5. It can tell you time.<br/>
6. It can update you with weather conditions.<br/>
7. It can open applications in your system, you should just have to provide path to application.<br/>
8. It can change your desktop wallpaper.v
9. It is able to send emails to any email address. (First you have to on the option of less secure access. manage your google account -> security -> less secure app access then turned it on)<br/>
10. It will also greet you in the start of program execution.<br/>
11. You can open any website of your choice.<br/>
12. It can refresh your mood by playing different genre of music.

## [ Future Enhancement ]
In the future we have thought that we would build this program in GUI (Graphical User Interface). In this way it would be more user friendly and more easy to handle.
## [ How it Works ]
Our application is programmed in a such a way that it will speak and ask the user to input any command through voice. The user will give it a command in audio format and our program will run and search for the specific command given and then it will execute that part of the code containing the command and it will give output. The output can be in the form of audio, a paragraph, or web browsing. We have formed different classes containing different attributes and methods. These classes and methods perform different functions. Our main class has a while loop which contains multiple if elif statements which will continuously ask the user for command and the it will call the method of a specific class and execute it. The program will run until the user say “terminate” or “shut down”. Your input should contain the keywords like , “wikipedia” , “website” , “time” , “email” , “weather" , "news" , "joke" , "google search" , "song" , "music" , "open application" , "background".

Go to folder Virtual_Desktop_Assistant and then run the main file which is Desktop_Assistant.py

NOTE: / In file password.txt there is a list write your email as first element and password as second element both in string . You can further add emails in emailcontact.txt.
