## Shuffle challenge
This challenge is inspired by security through obscurity.

```
Type: Obfuscation
Description: I put the flag in ascii art, I then inserted the line number into a random place in each line in this format '::123::' and then shuffled the lines
Format: plain text with spaces
```

As a security engineer, you will no-doubt encounter systems that are protected in some way by obfuscation and things just being made complicated.  Getting around these measures will require you to patiently unwrap the levels of confusion.  This exercise is to use tools to unjumble a text file.  Programmers may wish to make their own tools to do this.

We have created some vertical ASCII art.  That is, art made of of keyboard characters.  It is similar to the example below which is entirely made out of the characters \ | _ and /:
```
   _____   
  /  _  \  
 /  /_\  \ 
/    |    \
\____|__  /
        \/ 
__________ 
\______   \
 |       _/
 |    |   \
 |____|_  /
        \/ 
___________
\__    ___/
  |    |   
  |    |   
  |____|   
```
However to make things confusing for those trying to find our secret message we inserted line numbers into each line in a random position.  And then we shuffled all the lines! Mwahaha!

THE file need to unshuffle is ```file.txt```
* Also, I added the sol.java as solution for this challenge
* Flag found is : MAKING ASCII ART IS A KEY PART OF THE HACKERS TOOLKIT