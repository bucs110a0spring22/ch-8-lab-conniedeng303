# CS 110
## Lab 8 - Creating a String Library

### [Assignment Description](https://docs.google.com/document/d/1y_jvdf4tiNYyqNEkz-w9HXeigK8qQ45d-E4J1fvDBXk/edit?usp=sharing)

***

Replace anything surrounded by the `< >` symbols._

## SUMMARY:
 < First, I created a new file called StringUtility, which has the class StringUtility. I created a function to initialize the class, by setting self.str as the string.
 I created the vowel function using the help of the stackoverflow link, where it checks every letter in a string for vowels, and adding one to num_vowels if it does find one. I added the part where if the vowel count is over 5, it would return many.
 
 I then created the bothends function, which uses [n:m] to split the string into the first two and the last two characters, and then add them together into a string.
 
 For the fixstart function, I made it so if the length of self.str is = to 1, I returned it as it is. I then made it so if the new string's length is 0, I would add the first letter to is, so it doesn't get turned into a * later on in my code. If the character is = to the first letter, it would get a star, and if it doesn't then the letter would be left as it is and added to the string.
 
  For the asciiSum function, I converted the characters into ascii and then added them together.
  
  For the cipher function, I checked the length of the string, and made different if statements based on if the character is capital or not capital. To account for the wrap around, I made sure to create a equation that finds how much it would be added after Z. However, I had to add the if statement for if the length of the string exceeds 26, since if the string was longer than 26, then the equation would overflow into another character.>

## GRACE DAYS
Grace days used for this assignment: < 1 >

Grace days remaining: < 2 >/5

## KNOWN BUGS AND INCOMPLETE PARTS:
 None

## REFERENCES:
 [for my vowels function](https://stackoverflow.com/questions/19967001/count-vowels-in-string-python)

## MISCELLANEOUS COMMENTS:
 None
