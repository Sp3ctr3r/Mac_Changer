import subprocess
import optparse
import re
import time 

def kullanıcı_girişi():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface",dest = "interface", help = "interface to change!" )
    parse_object.add_option("-m", "--mac", dest = "mac_address", help = "new mac address!")

    return parse_object.parse_args()


def mac_değiştir(kullanici_arayuz, kullanici_mac):
    subprocess.call(["ifconfig", kullanici_arayuz, "down"])
    subprocess.call(["ifconfig", kullanici_arayuz,  "hw", "ether", kullanici_mac])
    subprocess.call(["ifconfig", kullanici_arayuz, "up"])


#def control_mac(user_interface):
#   ifconfig = subprocess.check_output(["ifconfig", user_interface])
#   yeni_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

#    if yeni_mac:
#       return yeni_mac.group(0)
#    else:
#       return None

print("Mac değiştirici başladı!")

time.sleep(1)

print("Mac adresi değiştirildi!")

time.sleep(1)

(kullanici_girdisi, argument) = kullanıcı_girişi()
mac_değiştir(kullanici_girdisi.interface, kullanici_girdisi.mac_address)
#değişmiş_mac = control_mac(str(kullanici_girdisi.user_interface))

#if değişmiş_mac == kullanici_girdisi.mac_address:
#    print("Başarılı!")
#else:
#    print("Hata!")

