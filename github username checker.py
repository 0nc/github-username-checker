import requests,threading,time,os
from colorama import Fore, init, Style
init(convert = True)

os.system("cls")

print(f"""{Fore.WHITE} > gh Username Checker\n > Load usernames into usernames.txt\n > https://ogusers.com/squish""")

totalthreads = int(input(" > How many threads? Do something low - github has high ratelimits\n > "))
total = len(open("usernames.txt").readlines()) # gets amount of lines in usernames.txt
threadsopen = 0
valids = 0
invalids = 0
def check(user):
	global valids
	global invalids
	global threadsopen
	global total
	try:
		res = requests.get(f"https://github.com/{user}")
		if res.status_code == 200:
			invalids += 1
			print(f"{Fore.RED} > {user} Taken")

		if res.status_code == 429:
			invalids += 1
			print(f"{Fore.RED} > {user} Ratelimited when checking")

		if res.status_code == 404:
			f = open("valids.txt", "a")
			f.write(f"{user}\n")
			f.close()	
			valids += 1
			print(f"{Fore.GREEN} > {user}")


		os.system(f"title Github Username Checker / Checked [{valids+invalids}] Out Of [{total}] / Valids : [{valids}] / Invalids : [{invalids}]")
	except Exception as error:
		print(f" > Error accessing github.com ! Maybe turn your thread count down?\n > Error : {error}")

	threadsopen -= 1


with open("usernames.txt", 'r') as f:
	for u in f.readlines():
		try:
			threading.Thread(target = check, args = (u.strip(),)).start()
			threadsopen = threadsopen + 1
		except:
			pass
		time.sleep(0.01)

		while threadsopen >= totalthreads: #this prevents too many threads happening
			time.sleep(0.1)

	while threadsopen != 0: #waiting until all threads finish
		time.sleep(0.1)

	print(f"{Fore.WHITE} > Done checking\n > Found {valids} untaken usernames out of {total} usernames loaded")
	input(" > ") 
		





