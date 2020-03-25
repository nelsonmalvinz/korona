import os,sys,requests,json

class aftar():
	def __init__(self):
		self.api="https://api.kawalcorona.com/{}"
		self.id="indonesia/provinsi"
		self.all="Country"
		os.system("clear")
		print("[ Corona Information By Nelson ]")
		print("- Type help for more information tools\n")
		self.menu()
		
	def ambil_info(self,info):
		data=requests.get(info).text
		return json.loads(data)
		
	def bantuan(self):
		print("\n[ Information ]\t")
		print("- Command         Description")
		print
		print("~ Provinsi         -see a case in the province")
		print("~ Indonesia        -See a case in indonesia")
		print("~ World            -See a case in world")
		print("~ World (all)      -See a case in world")
		print("~ World (country)  -See a case in country")
		print("~ Exit             -Exiting This Program")
		print("~ Api              -https://api.kawalcorona.com/")
		print("~ Author           -Nelson Malvinz\n")
		
	def perint(self,data,negara=False,Provinsi=False,world=False):
		if negara:
			data = data[0]
			print
			print("[+] Region : %s"%data["name"])
			print("[+] Positive : %s"%data["positif"])
			print("[+] Recovered : %s"%data["sembuh"])
			print("[+] Deaths : %s"%data["meninggal"])
			print
		if Provinsi:
			print("[+] Province : %s"%data["attributes"]["Provinsi"])
			print("[+] Positive : %s"%str(data["attributes"]["Kasus_Posi"]))
			print("[+] Recovered : %s"%str(data["attributes"]["Kasus_Semb"]))
			print("[+] Deaths : %s"%str(data["attributes"]["Kasus_Meni"]))
			print
		if world:
			print("[+] Country : %s"%data["attributes"]["Country_Region"])
			print("[+] Last Update : %s"%data["attributes"]["Last_Update"])
			print("[+] Confirmed : %s"%data["attributes"]["Confirmed"])
			print("[+] Positive : %s"%data["attributes"]["Active"])
			print("[+] Recovered : %s"%data["attributes"]["Recovered"])
			print("[+] Deaths : %s"%data["attributes"]["Deaths"])
			print
		
		
	def menu(self):
		self.g=raw_input("[*] Menu >> ").lower()
		if self.g =="help":
			self.bantuan()
		elif self.g =="indonesia":
			data=self.ambil_info(self.api.format("indonesia"))
			self.perint(data,negara=True)
		elif self.g =="provinsi":
			print("\n\t( Corona on province )\n")
			data=self.ambil_info(self.api.format(self.id))
			for f in data:
				self.perint(f,Provinsi=True)
		elif self.g =="exit":
			print("[!] Exit")
		elif self.g =="world":
			print("\n\t( Corona on the world )\n")
			while True:
				self.j=raw_input("[World] Menu >> ").title()
				if self.j =="All":
					data=self.ambil_info("https://api.kawalcorona.com")
					for x in data:
						self.perint(x,world=True)
				elif "Exit" in self.j:
					exit()
				elif self.j in "Help":
					self.bantuan()
				else:
					data = self.ambil_info("https://api.kawalcorona.com")
					for x in data:
						if self.j in x["attributes"]["Country_Region"]:
							self.perint(x, world=True)			
		
aftar()