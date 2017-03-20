# File: TestCipher.py

# Description: This program tests encryption methods, first the substitution cipher, then the vigenere cipher.

# Student Name: Jacob Martinez	

# Student UT EID: jam22426

# Partner Name: Blake Kappel	

# Partner UT EID: bak792

# Course Name: CS 313E

# Unique Number: 51730

# Date Created: 2/4/2015

# Date Last Modified: 2/7/2015

##########################################################################

# Encodes the string using the substitution method
def substitution_encode(strng):
  strng = strng.lower()
  # Two lists created to use their equal indices to determine the substituted letters
  alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  cipher = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p']
  # Initializes string that will be concatenated to created the encoded string
  eword = str("")
  # Concatenates the corresponding substitution char for each char in the string
  for i in strng:
    if i.isalpha():
      eword += cipher[alpha.index(i)]
    else: 
      eword += i
  return (eword)

# Decodes the encoded string with reverse substitution; same struction used in substitution_encode
def substitution_decode(strng):
  strng = strng.lower()
  alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  cipher = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p']
  dword = str("")
  for j in strng:
  	if j.isalpha():
  	  dword += alpha[cipher.index(j)]
  	else:
  	  dword += j
  return (dword)
  
# Encodes a given string using the vigenere way. 
def vigenere_encode(strng, passwd):
  strng = strng.lower()
  passwd = passwd.lower()
  # List containing all letters in order with len == 26; will refer to the item's indices to retrieve the letters
  alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  #Initialize empty string to be concatenated to as the characters are being encoded
  encoded_str = ''
  # Initialize a counter that holds the value of the password string index to be used next
  psw_idx = 0
  for s in strng:
    if s.isalpha():
      # Index counter resets upon reaching the len of the passwd string to reset at first passwd char
      if psw_idx == len(passwd):
        psw_idx = 0
      # The actual formula for the vigenere method involves adding indices (of the letters from the string and password) of the alpha list
      # Combined index variable; sum of alpha index of s and alpha index of the passwd char that holds the specified psw_idx position in the passwd string
      com_idx = alpha.index(s) + alpha.index(passwd[psw_idx]) 
      if com_idx < 26:
        encoded_str += alpha[com_idx]
        psw_idx += 1
      # Due to the structure of the substitution that is taking place, must adjust if com_idx > (letters in the alphabet) so that it loops back around to the beginning letter and so on
      else:
        com_idx = com_idx % 26
        encoded_str += alpha[com_idx]
        psw_idx += 1
    # Non-alpha chars left alone
    else:
      encoded_str += s
  return (encoded_str)

# Decoding the string using an inverse vigenere method; very much similar to the vigenere_encode
def vigenere_decode(strng, passwd):
  strng = strng.lower()
  passwd = passwd.lower()
  alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  decoded_str = ''
  psw_idx = 0
  for s in strng:
    if s.isalpha():
      if psw_idx == len(passwd):
        psw_idx = 0
      com_idx = alpha.index(s) - alpha.index(passwd[psw_idx])
      if com_idx < 0:
        com_idx = (alpha.index(s) + 26) - alpha.index(passwd[psw_idx])
      decoded_str += alpha[com_idx]
      psw_idx += 1
    else:
      decoded_str += s
  return (decoded_str)


def main():
  # open file for reading
  in_file = open ("cipher.txt", "r")
  
  # line count variable to be subtracted from; used in case of multiple test sequences
  line_count = sum(1 for line in open('cipher.txt'))
  
  while line_count > 0:
    # print header for substitution cipher
    print ()
    print ("Subsitution Cipher")
  
    # read line to be encoded
    line = in_file.readline()
    line = line.strip()
  
    # encode using substitution cipher
    encoded_str = substitution_encode (line)
  
    # print result
    print ("Plain Text to be Encoded: " + line)
    print ("Encoded Text: " + encoded_str)
    line_count -= 1
  
    # read line to be encoded
    line = in_file.readline()
    line = line.strip()
    
    # decode using substitution cipher
    decoded_str = substitution_decode (line)
  
    # print result
    print ("Encoded Text to be Decoded: " + line)
    print ("Decoded Text: " + decoded_str)
    print ()
    line_count -= 1
  
    # print header for vigenere cipher
    print ("Vigenere Cipher")
   
    # read line to be encoded and pass phrase
    line = in_file.readline()
    line = line.strip()
    passwd = in_file.readline()
    passwd = passwd.strip()
  
    # encode using vigenere cipher
    encoded_str = vigenere_encode (line, passwd)
  
    # print result
    print ("Plain Text to be Encoded: " + line)
    print ("Pass Phrase (no spaces allowed): " + passwd)
    print ("Encoded Text: " + encoded_str)
    line_count -= 2
  
    # read line to be decoded and pass phrase
    line = in_file.readline()
    line = line.strip()
    passwd = in_file.readline()
    passwd = passwd.strip()
  
    # decode using vigenere cipher
    decoded_str = vigenere_decode (line, passwd)
  
    # print result
    print ("Encoded Text to be Decoded: " + line)
    print ("Pass Phrase (no spaces allowed): " + passwd)
    print ("Decoded Plain Text: " + decoded_str)
    line_count -= 2

  in_file.close()


main()