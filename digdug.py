import dns.resolver
import sys
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
if(re.search(regex, sys.argv[1])):
	resolver = dns.resolver.Resolver()
	resolver.nameservers = [sys.argv[1]]
	answer=resolver.resolve("givemetheflag.com","TXT")
	print(answer.response.answer[0][0]) 
else:
	print("Invalid Ip address")
