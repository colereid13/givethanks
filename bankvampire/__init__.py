from .bankvampire import BankVampire

__red_end_user_data_statement__ = "This cog stores discord IDs as needed for operation."


async def setup(bot):
    bot.add_cog(BankVampire(bot))
