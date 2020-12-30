import bitly_api 
BITLY_ACCESS_TOKEN = "92e989d02751df075d38513381c5a56d03aeb050"
access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
print("Web address (place it in quotations):" )
full_link = input()
short_url = access.shorten(full_link) 
print('Short URL = ',short_url['url'])