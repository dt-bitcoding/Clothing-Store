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

############################## Mail Send to Gmail#############################################

# def pass_reset_form(request):  
#     if request.method == "POST": 
#         with get_connection(  
#             host=settings.EMAIL_HOST, 
#         port=settings.EMAIL_PORT,  
#        username=settings.EMAIL_HOST_USER,  
#        password=settings.EMAIL_HOST_PASSWORD,  
#         use_tls=settings.EMAIL_USE_TLS 
#         ) as connection:  
#             recipient_list = request.POST.get("email").split() 
#             bcc_list = ['dt.bitcoding@gmail.com', 'demo.darshil@yopmail.com']

#             # Create an EmailMessage instance
#             email = EmailMessage(
#                 subject='Sending to the Testing Email',
#                 body='http://127.0.0.1:4455/password_reset_complete/',
#                 from_email='demo.darshil@yopmail.com',
#                 to=recipient_list,
#                 bcc=bcc_list,  # Make sure bcc is a list or tuple
#                 connection=connection
#             )

#             # Now you can send the email
#             email.send()
            
#         return redirect('/password_reset_done')
        
#     else:
#         form = PasswordResetForm()
#     return render(request, 'NovaBazaar/pass_reset_form.html', {'form': form})