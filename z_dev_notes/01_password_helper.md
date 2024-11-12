# Python Password Pal - Brainstorm

Possible name? _Whipped Pass Py_

## Introduction to Method

The program should begin by laying out for the user how the application can help the user create a dynamic and memorbale password system for themselves that will create a unique password for each login.

The primary portion that the user must contribute are two components: 1. alphabetic string and 2. a few numbers. The user will be coached to make these selections with the idea being they will be easy for the user to remember but difficult for another person to guess.

The alpha string and numbers will then be put through a random number of letter or number replacements. This will for the "base" or "root" of the password that will then have prefixes and/or suffixes added to the base password (this will also be at the user's discretion for easy of remembering).

## Alpha Component

The first input from the user that will be used to create the base password will be a few words or a phrase. If the phrase is close to a sentence, the program will attempt to reduce the characters with simple replacements (e.g. 4 = for, u = you, etc) or take the first letter of each word to create an acronym or an initialism.

## Numerical Component

The second input from the user that will be used to create the base password will be a series of numbers. A user can enter a month and day (for example April 1st as 04/01 or June 9th as 6-9), a year (1986), or a set of numbers that are meaningful to them (3.14 or 1.618).

## Security Checks

We will ensure the length of the base password is at least 8 characters long (and recommend 10) and that there are uppercase letters, lowercase letters, numbers, and special characters. If special chracters, or numbers are utilized in the alpha component, they will be maintained. The string will be checked to see if it is all uppercase or all lowercase. If mixed casing is already in place, this will also be maintained, though casing may change during randomization.

## Randomization for Security

A random number of characters will be replaced in each component to make them more secure. At this stage we will ensure special characters are inserted and replace a few other letters or numbers with chracters that are "similar" from (e.g. A or a could be 4, I or i cold be 1, etc). This could be achieved by using a "Replacement Dictionary" which could have options for possible replacements as values for a given key. Like replacements could be stored in lists or possible tuples since they do not need to be mutable.

## Unique per Login

Lastly the user will input a few options for chracters to pull from the login domain. For example this could be the first consonant, vowel, or letter and fix it at the beginning, end, or middle of the passwrod. They may choose up to four of these type of characters based on placement within the domain (i.e. first, second, penultimate, last).

## Examples and Usage

The final portion of the program allows the user to test out their password and see how it would looke for different sites. The user could input a domain or company for which they have a login and the program will apply their settings to that login's password.

After review, the user will be given the option to return to the randomization portion of the program or start the application over from the beginning.

## MVP/POC and Further Development

The minimum viable product for this project would look like a simple Python program that goes through all the steps above. Additional features could be any of those below.

- Allow user to save a "profile" that would allow them to save their base passwords for future reference.
- Allow the user to store a number of login domains and see their base password applied.
- Allow the user to edit the login customizations of a saved base password.
- Allow the user to manipulate the base password directly? (Does this defeat the purpose of the app, even if the user would be prevented from saving unsafe passwords--e.g. missing a charter type, too short, too long, etc.)
