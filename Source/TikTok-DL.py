
#
# This Is Free Tool By Mr. Lyrica Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
	import os, requests, colorama, json
	from os import system
	from colorama import Fore
	system("title " + "Lyrica Was Here - @8Y - Soud#5866")
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()

logo = """
         _______   __ 
   ____ |  _  \ \ / /
  / __ \ \ V / \ V /
 / / _` |/ _ \  \ /
| | (_| | |_| | | |
 \ \__,_\_____/ \_/
  \____/
"""
print(Fore.CYAN+logo)
print(Fore.GREEN+"Made with Love by @8Y - Soud#5866 (<3 @e31l)\n\n"+Fore.RESET)

try:
	req = requests.get("https://hamod.ga/api/tiktokWithoutWaterMark.php?u="+input("Enter Tiktok Link: ")).text
	if 'link": "https' in req:
		print(f"\n[{Fore.GREEN}+{Fore.RESET}] Downloading Now")
		download = requests.get(json.loads(req)["link"],stream=True).content
		with open("@8Y-TikTok.mp4","wb") as a:
			a.write(download)
		print(f"\n[{Fore.GREEN}+{Fore.RESET}] Done Downloading\nSaved As @8Y-TikTok.mp4\n")
	else:
		print(f"\n[{Fore.RED}-{Fore.RESET}] Please Try Again Later")
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()
input("Press Enter To Exit...")
