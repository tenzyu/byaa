import const
from discord import AllowedMentions
from discord.ext.commands import Bot, Cog


class Authenticator(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        if reaction.channel_id != const.CH_AUTH:
            return

        user = reaction.member
        guild = self.bot.get_guild(reaction.guild_id)
        role_member = guild.get_role(const.ROLE_MEMBER)
        if role_member in user.roles:
            return
        await user.add_roles(role_member)
        ch_notify = self.bot.get_channel(const.CH_NOTIFY)
        await ch_notify.send(
            f"{user.mention}が参加しました。",
            allowed_mentions=AllowedMentions.none(),
        )


def setup(bot: Bot):
    bot.add_cog(Authenticator(bot))
