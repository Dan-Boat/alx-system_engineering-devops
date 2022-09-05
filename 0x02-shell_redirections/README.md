## Shell permissions 
* Ex1: echo Hello,World  print the Hello World followed by new line 
* Ex2: echo "\"(Öo)'" display the confused smiley special character
* Ex3: cat /etc/passwd display content in the file
* Ex4: tail /etc/passwd display the last 10 lines of the file
* Ex5: head /etc/passwd display the first 10 lines of the file 
* Ex6: head -n 3 iacta | tail -n 1 display the third line of the file 
* Ex7: echo "Best School" > "filename" create a file that contains the text "Best School"
* Ex8: ls -la > ls_cwd_content direct the output of the command ls -la to the file ls_cwd_content
* Ex9: tail -n 1 < iacta >> iacta or echo -en " " | tail -n 1 iacta >> iacta display the duplicate of the last line of the file
* Ex10: find . -name "*.js" -type f -delete Deletes all javascript files in the current directory
* Ex11: find . -mindepth 1 | -type d | wc -l Count the directories and subdirectories in the current folder
* Ex12: ls -lt | head display the 10 newest files in the current directory
* Ex13: sort | uniq -u display the sorted output of input files that appears once
* Ex14: grep -i "root" /etc/passwd display the lines in the file containing the "root" patterns
* Ex15: grep -i "bin" /ect/passwd same as ex14 but with "bin" patterns
* Ex16: grep -iA 3 root /etc/passwd display the lines containing the pattern "root" and the next 3 lines after them in the file 
* Ex17: grep -v bin /etc/passwd display the patterns of files that does not have the patterns of "bin"
* Ex18: grep -i "^[[:alpha]]" /etc/ssh/sshd_config display all the lines in the file starting with letters 
* Ex19: tr Ac Ze replace the letter A and C with Z and e for the input file
* Ex20: tr -d Cc deletes all the C and c letters in the input file
* Ex21: rev reverse inputs 
* Ex22: cut -d':' -f16 /etc/passwd display all the users and their home directories sorted by the users
* Ex 23,24,25 and 26: I used various online suggestion to provide the final answer. It was basically try and error exercise for me. 
