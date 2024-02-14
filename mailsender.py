##########################################Testing Email Sending############################################
import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("dt.bitcoding@gmail.com", "movc eptj thth kcxp")

subject="Sending email using python"
body="This is a test email sent using python script"
message="Subject:{}\n\n{}".format(subject,body)
# print(message)
listofaddress=["darshiltalaviya8834@gmail.com","demo.darshil@yopmail.com"]
ob.sendmail("dt.bitcoding@gmail.com",listofaddress,message)

print("Sent successfully to the given email address")
ob.quit()

##########################################End Testing Email Sending############################################