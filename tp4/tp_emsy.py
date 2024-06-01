__author__ = "Jonathan Braun"
__version__ = "1.0"
__maintainer__ = "Jonathan Braun"
__email__ = "jonathan.braun@eduvaud.ch"
__status__ = "Prototype"
__date__ = "February 2023"

#-----------------------------------------------------
# Importing libraries and modules
#-----------------------------------------------------
from datetime import datetime                                                             # Library for date and time related stuff
import math                                                                 # Library for math stuff
import csv 
import smtplib                                                                 # Library for csv handling stuff
import os
from sensirion_i2c_driver import I2cConnection                              # Sensor driver
from sensirion_i2c_sht.sht4x import Sht4xI2cDevice                          # Sensor driver
from sensirion_i2c_driver.linux_i2c_transceiver import LinuxI2cTransceiver  # Sensor driver

#-----------------------------------------------------
# Declaring the sensor object
#-----------------------------------------------------
sht40 = Sht4xI2cDevice(I2cConnection(LinuxI2cTransceiver('/dev/i2c-2')))

#-----------------------------------------------------
# Declaring functions
#-----------------------------------------------------
def read_sensor():
    try:
        t, rh = sht40.single_shot_measurement()
        # Watch out! t and rh are variable that contain not only the values but also the units.
        # You can print the values with the units (print(t)) or you can also recover only the value
        # by specifying which one: t.degrees_celsius or rh.percent_rh
    except Exception as ex:
        print("Error while recovering sensor values:", ex)
    else:
        return t, rh

    return 0 # In case something went wrong

def calculate_dew_point(temp, humidity):
    lambd = 243.12
    beta = 17.62

    rho = math.log1p(humidity/100) #marche po 
    rho2 = math.log(humidity/100)
    rha = ((beta *temp)/(lambd +temp))
    alors = lambd * (rho2 + rha)
    voila = alors/(beta-(rho2 + rha))
   #version lib meteocalc
   #pa = humidity/ 100. * math.exp(beta  * temp / (lambd  + temp))
   #dp = lambd  * math.log(pa) / (beta - math.log(pa))
    return voila 

def send_email(receiver, subject, message):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("ETML.ES.EMSY@gmail.com","cely neve caly akjz")
        sender = "ETML.ES.EMSY@gmail.com"

        headers = {
            'Content-Type': 'text/html; charset=utf-8',
            'Content-Disposition': 'inline',
            'Content-Transfer-Encoding': '8bit',
            'From': sender,
            'To':receiver,
            'Date': datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
            'X-Mailer': 'python',
            'Subject': subject
        }
        # create the message
        msg = 'Bonjour! Ceci est un mail dalerte.'
        for key, value in headers.items():
            msg += "%s: %s\n" % (key, value)

        # add contents
        msg += "\n%s\n" % (message)

        try:
            server.sendmail(headers['From'], headers['To'], msg.encode("utf8"))
            server.quit()
            print("Email sent successfully!")
        except Exception as ex:
            print("aie", ex)

def csv_write_row(data_row):
     try:
     # Write csv here
         with open('/home/debian/EMSY_TP4_Beagle/tp4/TempLog.csv', 'a', newline='') as csvfile:
            writter = csv.writer(csvfile)
            writter.writerow([datetime.now().date(),datetime.now().time(), data_row[0], data_row[1], data_row[2]])
            csvfile.close()

     except Exception as ex:
         return 0, ex
     else:
         return 1

#-----------------------------------------------------
# Main script
#-----------------------------------------------------
if __name__ == "__main__":  # Runs only if called as a script but not if imported
    subject = "Ceci est un email d alerte"
    message = "Bonjour! Ceci est un mail dalerte." 
    pathcsv = "TempLog.csv"

    print("Hello and welcome to EMSY")
    temperature, humidity = read_sensor()
    print ("temperature = "  +str(round(int(temperature.degrees_celsius),2)))
    print("humidite = " +str(round(humidity.percent_rh,2)))
    dew_point = calculate_dew_point(temperature.degrees_celsius, humidity.percent_rh)
    print("point de rosee = "+ str(round(dew_point,2)))
    time = datetime.now().strftime('%d %b %Y %H:%M     ')
    if csv_write_row([round(temperature.degrees_celsius,2),round(humidity.percent_rh,2),round(dew_point,2)]) :
       print("logs done")

   
if temperature.degrees_celsius >= 28:
   #exec_script()
   subject = "Ceci est un email d alerte"
   message = "Bonjour! Ceci est un mail dalerte."

   send_email("dfasdfasdf193@gmail.com", subject, message)







