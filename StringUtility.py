class StringUtility:
  def __init__(self,string):
    self.str = string

  def __str__(self):
    return self.str
    
  def vowels(self):   
    num_vowels = 0
    for char in self.str:
      if char in "aeiouAEIOU":
        num_vowels = num_vowels+1
        if num_vowels >= 5:
          return "many"
    return str(num_vowels)
    
  def bothEnds(self):
    if len(self.str) <= 2:
      return ""
    return self.str[0:2] + self.str[len(self.str)-2:len(self.str)]
    
  def fixStart(self):
    new_result = ""
    if len(self.str) <= 1:
      return self.str
    first_letter = self.str[0:1]
    for i in self.str:
      if len(new_result) == 0:
        new_result += first_letter
      elif i == first_letter:
        new_result += "*"
      else:
        new_result += i
    return new_result
      

  def asciiSum(self):
    total = 0
    for char in self.str:
      total += ord(char)
    return total
  
  def cipher(self):
    new_result = ""
    length = len(self.str)
    if (length > 26):
      length -= 26
    for i in self.str:
      if (i == " "):
        new_result += " "
      else:
        char_value = int(ord(i))
        shifted_result = 0
        if char_value <= 90 and char_value >= 65:
          if char_value + length > 90:
            shifted_result = char_value + length - 90 + 64
          else:
            shifted_result = char_value + length
        if char_value <= 122 and char_value >= 97:
          if char_value + length > 122:
            shifted_result = char_value + length - 122 + 96
          else:
            shifted_result = char_value + length
        new_result += chr(shifted_result)
    return new_result