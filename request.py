#we add requests library
import requests

#target url
url = 'http://192.168.1.101/dvwa/login.php'

#admin,password and login information
data = {'username' :'admin', 'Password' :'password','Login':'Login'}

#try except
try:
	    
	    #we create object and we add url,data,allow_redirects and timeout 
    r = requests.get(url,data = data, allow_redirects=False,timeout=2)


    #we use if and else, if r.status_code=200 means login succesfully
    if r.status_code == 200 :
    	print("Login succesfully")

    else:
    	print(">> ", r.status_code)

#if we have any exception this code execute
except Exception as e:
	print(e)
	pass


