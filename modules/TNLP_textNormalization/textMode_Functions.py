import re

def convertWin_Into_UnixText(self,_file):
   """Converting the original text into UNIX-mode to avoid 
   the slipping of the boundaries"""
   
   temp = open(_file).read().decode('iso8859-1')
   if temp.find('\r'):
      temp = re.subn('\r\n','\n',temp)
      tmp_file = open(_file, 'w')
      tmp_file.write(temp[0].encode('iso8859-1'))
      tmp_file.close() 
