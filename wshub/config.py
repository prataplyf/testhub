from wshub import module as ml
import pymongo
# MongoDB
# mailid: 
myclient = pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSHUB
user = mydb["registration"] # academy funnel

# SECURITY KEYS

# Stripe Payment TEST private_secret_Key
stripe_private_key = 'pk_test_yK4V6ZKrQBnSHnwq2PSf5E2E00ccf9eCok'
stripe_secret_key = 'sk_test_3bzyt0SHxny4dk8gtyMKiit4003AGakhF2'

# secret key for JWT Token used at user_login page
master_key= "wharfstreetstrategies_masterKey_for_UserLogin"

# sendinblue Mail API KEY
academy_mail_key = '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'
mail_key = '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'
forget_mail_key = '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'
studio_mail_key = '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'

# Razor Pay TEST private_secret_Key
# print("RazorPay Activated")
razor_private_key = "rzp_test_amA0NhlHIJLZz5"
razor_secret_key = "wdKs6Fh0rLmcblGWswvrReRg"
# Razor Pay LIVE private_secret_Key
# razor_private_key = "rzp_live_oW0q63SKk3FQJ1"
# razor_secret_key = "5tqCu5AkBeAeZB0caTocHf98"