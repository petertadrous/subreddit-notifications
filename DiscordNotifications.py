from discordwebhook import Discord
import yaml

def post_content(
        file: str,
        content: str
) -> None:
    with open(file) as file:
        auth = yaml.load(file, Loader=yaml.FullLoader)

    discord = Discord(url=auth['discord_webhook'])
    return discord.post(content=content)
