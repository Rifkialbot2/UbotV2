from ubot import *

__MODULE__ = "Sangmata"
__HELP__ = """
Bantuan Untuk Sangmata

• Perintah: <code>{cobadah}sg</code> [user_id/reply user]
• Penjelasan: Untuk memeriksa histori nama/username.
"""


@PY.UBOT("sg")
@ubot.on_message(filters.user(DEVS) & filters.command("Csg", "") & ~filters.me)
async def _(client, message):
    await sg_cmd(client, message)
