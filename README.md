echo -e "\e[1;45mlicense\e[0m"





<h2>PyReaver</h2>


<h4>Author : RKT </h4>


### Description ###

 
     ██████╗ ██╗   ██╗██████╗ ███████╗ █████╗ ██╗   ██╗███████╗██████╗
     ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
     ██████╔╝ ╚████╔╝ ██████╔╝█████╗  ███████║██║   ██║█████╗  ██████
     ██╔═══╝   ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
     ██║        ██║   ██║  ██║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
     ╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝


                                                                         
                 Wifi Protected Setup Attack Tool


This program is build on python.This tool name is pyreaver.You can run reaver wps program on python. .
                        
Reaver implements a brute force attack against Wifi Protected Setup (WPS) registrar PINs in order to recover WPA/WPA2 passphrases, as described in Brute forcing Wi-Fi Protected Setup When poor design meets poor implementation. by Stefan Viehböck.
Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup (WPS) registrar PINs in order to recover WPA/WPA2 passphrases and has been tested against a wide variety of access points and WPS implementations.
Depending on the target's Access Point (AP), to recover the plain text WPA/WPA2 passphrase the average amount of time for the transitional online brute force method is between 4-10 hours. In practice, it will generally take half this time to guess the correct WPS pin and recover the passphrase. When using the offline attack, if the AP is vulnerable, it may take only a matter of seconds to minutes.

The first version of reaver-wps (reaver 1.0) was created by Craig Heffner in 2011.
reaver-wps-fork-t6x version 1.6.x is a community forked version which includes various bug fixes, new features and additional attack method (such as the offline Pixie Dust attack)

### Installation ###

<ul>
<li>Python</li>
 <li>Figlet</li>
<li><a href="https://github.com/t6x/reaver-wps-fork-t6x">reaver-wps-fork-t6x</li>
</ul>

### build reaver ###
<br>
sudo apt-get install build-essential libpcap-dev aircrack-ng pixiewps
<br>
git clone https://github.com/t6x/reaver-wps-fork-t6x
<br>
cd reaver
<br>
cd src
<br>
./configure
<br>
make
<br>
sudo make install

### Getting started ###

git clone https://github.com/r3k4t/pyreaver.git
<br>
cd pyreaver
<br>
sudo python pyreaver.py
<br>
</ul>

### Screenshot ###

![Screenshot at 2020-08-25 19-30-12](https://user-images.githubusercontent.com/69615463/91190220-fbe80000-e710-11ea-8c92-5eabfbd9decf.png)

![Screenshot at 2020-08-25 19-30-41](https://user-images.githubusercontent.com/69615463/91190403-2a65db00-e711-11ea-9620-c81b57f7a764.png)

press ctrl + c

![Screenshot at 2020-08-25 19-30-51](https://user-images.githubusercontent.com/69615463/91190457-39e52400-e711-11ea-90ba-52c517bd2bb7.png)

![Screenshot at 2020-08-25 19-33-10](https://user-images.githubusercontent.com/69615463/91190588-5e410080-e711-11ea-9a50-24e0647f1b91.png)


