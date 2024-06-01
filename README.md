# EMSY_TP4_Beagle
Utilisation de la BeagleBone processeur ARM Cortex A8 (CPU à 1 GHz et 512 MB de RAM pour la version 
utilisée, préinstallés avec une version de Linux Debian et une adresse IP fixe pour le réseau bleu, indiquée sur le boîtier (10.228.134.227)
et d'un capteur Grove [url](https://www.seeedstudio.com/Grove-Temp-Humi-Sensor-SHT40-p-5384.html)

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
git clone https://github.com/Sweedy3960/EMSY_TP4_Beagle
crontab -e 
```
puis ajouter la ligne :
```bash
*/15 * * * * /"PathTo"/python3 /"PathTo"/EMSY_TP4_Beagle/tp4/tp_emsy.py
```
# Résultats:
"le cron à été set à 1 min pour ne pas perdre de temps"
## Logs:
![image](https://github.com/Sweedy3960/EMSY_TP4_Beagle/assets/89172461/dccacf1d-7b0e-4ee9-bf71-95676a9d5f0b)


## Mail:
![image](https://github.com/Sweedy3960/EMSY_TP4_Beagle/assets/89172461/eb589dbc-1cad-425b-8f47-45fc730ba914)


## Terminal: 
```bash
python3 /"Pathto"/tp_emsy.py
```
![image](https://github.com/Sweedy3960/EMSY_TP4_Beagle/assets/89172461/6cb74cde-17d7-4e88-8793-f5354b534a1e)

