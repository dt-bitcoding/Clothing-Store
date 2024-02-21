from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        
        if ipn_obj.receiver_email != "receiver_email@example.com":
           
            return

       
        if ipn_obj.custom == "premium_plan":
            price = ...
        else:
            price = ...

        if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'USD':
            ...
    else:
        #...

valid_ipn_received.connect(show_me_the_money)