# Assignment

1.	Use the following API:
https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year=now&month=x&ss=on&mf=on&c=on&geo=geoname&geonameid=3448439&M=on&s=on
2.	Write a python script, which will fetch ONLY the Jewish holidays in the next Quarter. The script's output should be a Json file containing the holiday's hebrew name, and its date in a Json Array.
3.	Write a python script, which will generate a self-signed CA and server Certificates, signing the following DNS: assignment.local.
4.	Vagrant - Write a Vagrantfile, which will establish a Centos VM (Based on VirtualBox – Note you will have to install VirtualBox on your PC).
5.	Vagrant Automation should do the following:
    a.	Install a web server, based on nginx/apache.
    b.	Generate the certificates using the script you had previously created and use those certificates in conjunction with the web server you have just established.
    c.	Run the python script which will generate the holidays json array file.
    d.	Serve the outputs json array file using the web server securely (Port 443) as the main page.
6.	The final assignment answer should contain a .ps1 file, in which once we run it, it wls
7.	ill establish the VM, run the Vagrant Automation, and initiate a google-chrome instance directing to https://assignment.local.serving the output json array securely(note: you will have to automatically load the generated CA certificate into your local machine, also make sure the DNS is being available locally through the host).


## Quick Start

Execute the `.ps1` script located in vagrant directory.