from interactions import SlashContext


async def executor(ctx: SlashContext):
    await ctx.send('Pong !')