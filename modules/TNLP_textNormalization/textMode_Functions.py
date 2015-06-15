import re

def convertWin_Into_UnixText(self,_file):
   """Converting the original text into UNIX-mode to avoid 
   the slipping of the boundaries"""
   
   temp = open(_file).read().decode('iso8859-1')
   if temp.find('\r') or temp.find('\n'):
      temp = re.subn('\r\n','',temp)
      temp = re.subn('\n','',temp[0])

      #Continuous whitespace replace by only one.
      spaces = re.compile(r'\s+')
      temp = spaces.sub(' ', temp[0])

      tmp_file = open(_file, 'w')
      tmp_file.write(temp.encode('iso8859-1'))
      tmp_file.write('\n')
      tmp_file.close() 
