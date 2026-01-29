#we add paramiko library
import paramiko

#we describe function for execute command
def execute_command():

    # receive input from the user
	command = input('>> ')
    
    #we create loop and if input is "Quit,quit, QUIT" function will end
	while command.lower().strip() != 'quit' :
        
        #remote server execute command, stdin->send to data, stdout->command output, stderr->error message
		stdin, stdout, stderr = ssh.exec_command(command)
        
        #read for output
		output = stdout.read()
		error = stderr.read()
        
        #print output and output was encoded and we are decoding
		print(output.decode())
		print(error.decode())
        
        #again receive input from the user
		command = input('>> ')
	
	#function end
	return 0

#create a object and this name is ssh
ssh = paramiko.SSHClient()

#if we didn't set AutoAddPolicy we will receive error message and this message is include "Unknown Server" 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Metasploit ip address maybe your ip addresses different check it 
ip = '192.168.1.101'

#ssh port
port = 22

#Create try except for wrong username or password
try:
	#we need to Metasploit default username and password
	username = input("Username: ")
	password = input("Password: ")

	#connect to metasploit and we add ip, port, username, password
	ssh.connect(ip, port = port, username = username,  password = password)
	#we call function
	execute_command()

#if we have error this method catch and print error
except Exception as e:
	print("incorrect password or username and Error is: ",e)

#Server end
finally:
	ssh.close()






