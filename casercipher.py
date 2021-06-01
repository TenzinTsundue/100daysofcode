# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def code(message, shift, direction):
	for i in range(len(message)):
		item = message[i]
		if item not in alphabet:
			print(item, end="")
		else: 
			if direction == 'incode':
				encoded_letter_position = (alphabet.index(item) + shift)%26
				encode_letter = alphabet[encoded_letter_position]
				# print("The encoded message is ",end="")
				print(encode_letter, end="")
			elif direction == 'decode':
				encoded_letter_position = (alphabet.index(item) - shift)%26
				encode_letter = alphabet[encoded_letter_position]
				# print("The decoded message is ",end="")
				print(encode_letter, end="")
			else:
				print("Not supported direction")
				should_continue = False


should_continue = True
while should_continue:
	direction = input("type 'incode' to incrypt and type 'decode' to decrypt: ")
	message = input("Type your message: ").lower()
	shift = int(input("Enter shift number: "))
	code(message, shift, direction)

	result = input("\nType 'yes' if you want to go again. Otherwise type 'no' : ")
	if result == 'yes':
		should_continue = True
	else:
		should_continue = False

