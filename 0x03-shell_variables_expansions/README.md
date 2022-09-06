## Shell expansions and variables
This project covers shell variables, arithmetic, expansions, and more 

* EX0: alias ls="rm *" create alias for the command rm * with the name ls
* Ex1: echo hello $USER  print hello user 
* EX2: export PATH=$PATH:/action  export the path /action to %PATH
* EX3: echo $PATH | tr -s ":" "\n" | wc -l  count the directories in the PATH
* EX4: printenv  print all the environment variables
* EX5: set  pritn all the local and global variables including functions
* EX6: BEST="School"  create a local variable 
* EX7: export BEST="School"  create a global variable 
* EX8: echo $((128+$TRUEKNOWLEDGE))   print the addition of a value to environmental variable
* EX9: echo $((POWER/DIVIDE))  prints the division of two environmental variables 
* EX10: echo $((BREATH**LOVE))  prints the power expression of two environmental variables 
* EX11: echo $((2#$BINARY))  convert environmental variable which is binary to decimal value 
* EX12: echo {a..z}{a..z} | tr " " "\n" |grep -v "oo"  create two combination letters except oo
* EX13: printf "%.2f\n" $NUM   print the environmental variable NUM in 2 decimal place 
* EX14: printf "%x\n" $DECIMAL  display a num from base 10 to 16
* EX15: tr 'A-Za-z' 'N-ZA-Mn-za-m'  encode and decode test assume to be ASCII using the rot13 encryption
* EX16: paste -d, - - | cut -d, f1 print the first line of input file and any other line 
* EX17: printf "%o\n" $(( $((5#$(echo $WATER | tr water 01234))) + $((5#$(echo $STIR | tr 'stir.' 01234))) )) | tr 01234567 bestchol  adds two numbers stored in the environment variable WATER and STIR in the base water and stir respectively

### Resources
* [Expansions](http://linuxcommand.org/lc3_lts0080.php)
* [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
* [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
* [Shell initiation files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
* [The alias command](http://www.linfo.org/alias.html)
