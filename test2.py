Import telnetlib
Import sys
Import getpass

For n in range (18,206):
	HOST = "172.29.129." + str(n)
	 tn = telnetlib.telnet(HOST)

Tn.read_until ("username: ") 
Tn.write ("username+ \n")

If password:
Tn.read_until("password: ")
Tn.write(password+ "\n")

Tn.write ("conf t \n")

For n in range (2,20):
	Tn.write ("int loop" + str(n) +"\n")
	Tn.write ("loop details are" + str(n) +"\n")
	
Tn.write("end\n")
Tn.write("exit\n")

Print tn.read_all()

Print tn.read_all()




