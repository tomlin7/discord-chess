from discord.ext.commands import Bot

import config

client = Bot(command_prefix='.')

# extensions
client.load_extension('cogs.chess')
client.load_extension('cogs.events')


client.run(config.get_token())