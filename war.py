Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cards import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from cards import *
ModuleNotFoundError: No module named 'cards'
>>> ntrials=1000
>>> awins=0
>>> for i in range(ntrials):
	adeck=deck()
	adeck.shuffle()
	bdeck=deck()
	bdeck.suffle()
	ascore=0
	bscore=0
	tied=0
	while adeck.cardsleft() > 0 and bdeck.cardsleft() > 4:
		acard1=adeck.dealcard()
		bcard=bdeck.dealcard()

		
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    adeck=deck()
NameError: name 'deck' is not defined
>>> if acard1.value() > bcard.value():
	ascore +=1
if acard1.value() == bcard.value():
	
SyntaxError: invalid syntax
>>> if acard1.value() == bcard.value():
	tied += 1

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    if acard1.value() == bcard.value():
NameError: name 'acard1' is not defined
>>> if bcard.value() > acard1.value():
	bscore +=1

	
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    if bcard.value() > acard1.value():
NameError: name 'bcard' is not defined
>>> print("player A win percentage=",awins/ntrials, "tied games", tied)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print("player A win percentage=",awins/ntrials, "tied games", tied)
NameError: name 'tied' is not defined
>>> 
