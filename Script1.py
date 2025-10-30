print ("===CYBERSECURITY TARGET SCANNER===")
target =input("Enter you ip address or a domain name")
print ("Scanning target :", target)
if ".com" in target or "192." in target:
    print("Target", target, "Looks like an ip address or a domain name")
else :
    print ("Enter a correct domain or ip address")