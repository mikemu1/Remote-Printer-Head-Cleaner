'''
icclean.py

Email printer with HTML text to clean printheads

To beach printer via hpeprint
From icloud app account

'''
import smtplib
from email.message import EmailMessage
from datetime import datetime
#from pretty import *

dts = datetime.now().ctime()
print(dts)

MY_EMAIL_ADDRESS = 'mikemu0919@icloud.com'
MY_EMAIL_PASSWORD = 'ywqj-amdp-usab-ihlr'
TO_EMAIL_ADDRESS = 'nsbeachprinter@hpeprint.com'
# TO_EMAIL_ADDRESS = '88b34hjm@hpeprint.com'
# TO_EMAIL_ADDRESS = 'mikemu0919@icloud.com'

txt = f"Clean printer heads {dts} {MY_EMAIL_ADDRESS}"

EMAIL_CONTENT = f'''
<!DOCTYPE html>
<html>
    <body>

        <h1>Cleaning printheads</b></h1>

        <p style="font-size:14px">{txt}</br>
        <span style="color:blue">{txt}</span></br>
        <span style="color:red">{txt}</span></br>
        <span style="color:yellow; background-color:gray">{txt}</span></p>

        <p style="font-size:18px">{txt}</br>
        <span style="color:blue">{txt}</span></br>
        <span style="color:red">{txt}</span></br>
        <span style="color:yellow; background-color:gray">{txt}</span></p>

        <p style="font-size:18px;font-weight:bold">{txt}</br>
        <span style="color:blue">{txt}</span></br>
        <span style="color:red">{txt}</span></br>
        <span style="color:yellow; background-color:gray">{txt}</span></p>

   </body>
</html>
'''

msg = EmailMessage()
msg['Subject'] = f'PrettyClean {dts}'
msg['From'] = MY_EMAIL_ADDRESS 
msg['To'] = TO_EMAIL_ADDRESS 
msg.set_content(EMAIL_CONTENT, subtype='html')


with smtplib.SMTP('smtp.mail.me.com', 587) as smtp:
    print(smtp.ehlo())
    print(smtp.starttls())
    print(smtp.ehlo())
    print(smtp.login(MY_EMAIL_ADDRESS, MY_EMAIL_PASSWORD))
    print(smtp.send_message(msg))

    

    




