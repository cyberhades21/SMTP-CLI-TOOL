from Parse.Argument  import Argument
import smtplib as sm
import sys

s=Argument(sys.argv) 
print(s.options)
print(s.commands)
print(s.optionvalues)
print(s.get_optionvalues('--brightness')) 