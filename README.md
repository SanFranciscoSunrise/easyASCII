```  
  **  **                               _     ____     ____  ___  ___ 
  **  **    ___   __ _  ___  _   _    / \   / ___|   / ___||_ _||_ _|
********** / _ \ / _` |/ __|| | | |  / _ \  \___ \  | |     | |  | | 
  **  **  |  __/| (_| |\__ \| |_| | / ___ \  ___) | | |___  | |  | | 
********** \___| \__,_||___/ \__, |/_/   \_\|____/   \____||___||___|
  **  **                     |___/                                   
  **  ** 
```

Author/s: SanFranciscoSunrise (SanFranciscoSunrise@GMail.Com)

####About the source code:
This program is very simple yet powerful and I hope helpful to those of you who like to write cover pages and other documents in various asciiformats.  I eventually plan to place it into some sort of GNU/GPL but fornow just know that it is free to spread given that you reatain credit to me and any others who may contribute in the future.

####About the program:
Convert string text into BIG ASCII formats.  Utilize easy to create font files to select a font.  Run your text output vertically, horizontally, or word-per-line.  Output to a file.

####Known Issues/ToDo:
*[-] = Known Issue, [*] = Todo, [+] = Done

*[-]  Still need to implement some sort of decision process with regaurds to file output. Giving the choice to append or overwrite a file that already exists.  It is currently just stuck in append mode (not such a bad thing given the the choice of the two).

*[-]  Need a better way to implement symbols such as !@#$%^&*()_+=-`~/.,[]{}:"<>?.  Currently about 2/3 of them can be implemented into the font file directly but about 2/3 of those seem to need quotes around the phrase for them to print out without an error, which leaves an odd situation for quotes themselves.  The other 1/3 seem  to crash the program with or without quotes.  Fixing this would be a major help towards placing the program into it's first official release.

*[*]  Please feel free to generate and submit your own font files.  Just email them over to me at SanFranciscoSunrise@Gmail.Com.  It should be self explanatory what the format is but in case it's not here goes. Characters at the top line are read in and indexed.  anything between a set of " " quotes is the translation you have drawn for the character corresponding to the index of those quotes in relation to the number of previous quotes. Thus if the top line is F 6 % the characters representation in ASCII will be between the rows of quotes as such:

     " " F " " 6 " " % "

Two caviats are that there must be an initial " single quote at the start of each row and as of now exactly 7 rows at most.  If you would like to use less then 7 rows just fit your characters into the bottom few rows or somewhere in the middle.  If you are truly confused just copy one of the sample font files and alter the text within them to your liking.  And yes there is the flexibility to do some seriously screwy things like make a backwards and/or random alphabet cipher by reversing and/or randomizing the order of the characters in the top row.

####Version History:
*[+] Beta 1 : 08/17/2015 : First public release.  Let the cross-platform testing begin.

[EOF]
