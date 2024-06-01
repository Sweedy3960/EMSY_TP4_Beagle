# EMSY_TP4_Beagle
Utilisation de la BeagleBone, et d'un capteur Grove

# Logiciels utilisés
Sur le pc: 
* WinSCP: pour le transfer de fichier et la modification 
* Putty: pour ssh la board
  
Sur la board: 
* tmux
* crontab
* openssh


## Librairies utilisées 
* math
* csv
* smtplib
* os
* datetime 
  
## Drivers utilisés pour le module de Temp&Humi (SHT40)

Sensirion/python-i2c-sht [GitHub Pages](https://github.com/Sensirion/python-i2c-sht).

Sensirion/python-i2c-sht4x [GitHub Pages](https://github.com/Sensirion/python-i2c-sht4x).

Sensirion/python-i2c [GitHub Pages](https://github.com/Sensirion/python-i2c-driver).


```bash
sudo apt-get update && upgrade
git clone https://github.com/Sensirion/python-i2c-sht
git clone https://github.com/Sensirion/python-i2c-sht4x
git clone https://github.com/Sensirion/python-i2c-driver
cd python-i2c-driver
sudo python3 setup.py install
sudo python3 setup.py build 
cd ../python-i2c-sht4x
sudo python3 setup.py install
sudo python3 setup.py build 
cd ../python-i2c-sht
sudo python3 setup.py install
sudo python3 setup.py build
```
# Résultats:
"le cron à été set à 1 min pour ne pas perdre de temps"
## Logs:

## Mail:
## Terminal: 


