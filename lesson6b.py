
#def multiply(principal, rate, time):
 #   answer = principal*rate*time/100
  #  print('This your simple interest', answer)

#multiply(1240,1.5,2)

#def multiply(principal, rate, time):
  #  answer = principal*rate*time/100
   # return answer
#def my_values():
    #principal = float(input('Enter your Principal amount'))
    #rate = float(input('Enter your Rate '))
    #time = int(input('Enter Duration'))
    #result = multiply(principal,rate,time)

    #print('this is your simple interest', result)

#my_values()

password = (input('Enter password : '))
while password == '':
    print('You Must Enter Password')
    password =  (input('Enter password : '))
   
login = False
if password == 'modcom':
    print('Logged in successfully')
else:
    print('Invalid paasword')
    password =  (input('Enter password : '))
    

