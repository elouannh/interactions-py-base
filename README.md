# How to configure it?

Create a `token.json` file at the root of your project, and then write in it:
```json
{
  "token": "your token goes here"
}
```

# How to add commands?

Into the `./commands` directory, add a command based on the `ping.py` example.
```python
from interactions import SlashContext


async def executor(ctx: SlashContext):
    await ctx.send('Pong !')
```
Just replace the executor content by your command script.

Then, into the `__init__.py` file, add the exportation of your command by reusing the `ping.py` example.

Then, into the `main.py` file, add this script:
```python
@slash_command(
    name="ping",
    description="Replies pong!"
)
async def ping(ctx: SlashContext) -> None:
    await ping_executor(ctx)
```
Don't forget to add your commands above your bot login to be sure they are correctly loaded.
Don't forget to update information about your command: name, description, etc.

# How to start it?

Then, just run the `main.py` file.