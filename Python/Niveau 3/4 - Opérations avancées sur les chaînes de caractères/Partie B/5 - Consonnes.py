voyelles = [ord(x) for x in "aeiouy"]

for ascii in range(ord("a"), ord("z") + 1):
	if ascii not in voyelles:
		print(chr(ascii) + " ", end="")
