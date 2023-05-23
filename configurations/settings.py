TOKEN = "5801652759:AAFVrHysy_Jv145fsxteRmzFcgeRX9RG5ls"
NAME = "Whispers"
WEBHOOK = False
# The following configuration is only needed if you setted WEBHOOK to True #
WEBHOOK_OPTIONS = {
    "listen": "0.0.0.0",  # IP
    "port": 443,
    "url_path": TOKEN,  # This is recommended for avoiding random people
    # making fake updates to your bot
    "webhook_url": f"https://example.com/{TOKEN}",
}
