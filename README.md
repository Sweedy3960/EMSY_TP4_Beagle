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

## Sur la board en shh: 
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

## Utilisation
```bash
git clone https://github.com/Sensirion/python-i2c-sht](https://github.com/Sweedy3960/EMSY_TP4_Beagle)
crontab -e 
```
puis ajouter la ligne :
```bash
/15 * * * * /usr/bin/python3 /home/debian/EMSY_TP4_Beagle/tp4/tp_emsy.py
```
# Résultats:
"le cron à été set à 1 min pour ne pas perdre de temps"
## Logs:
![image](https://github.com/Sweedy3960/EMSY_TP4_Beagle/assets/89172461/2d28d24c-5bea-4c50-94a2-445ca4262dde)

## Mail:
![image](https://github.com/Sweedy3960/EMSY_TP4_Beagle/assets/89172461/20cbc0d1-eacf-4413-b113-e4a361b108e9)

## Terminal: 
```bash
python3 /EMSY_TP4_Beagle/tp4/tp_emsy.py
```
![image](https://github.com/Sweedy3960/EMSY_TP4_Beagle/assets/89172461/6cb74cde-17d7-4e88-8793-f5354b534a1e)

