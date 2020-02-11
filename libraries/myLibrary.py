import os


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}


def squared(num):
    print('Hello there' , num)

def myDict(book):
    for k, v in thisdict.items():
        if book in v:
            return k
def checkIf(key):
	if key in thisdict:
	   print("exists", key)
	else:
	   print('This does not exist', key)

	   