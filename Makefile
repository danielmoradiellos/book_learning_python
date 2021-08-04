all:
	gcc -o ./embedded.exe ./embedded.c -lpython2.7 -I/usr/include/python2.7/
clean:
	rm ./embedded.exe
