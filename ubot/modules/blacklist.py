from ubot import *

__MODULE__ = "Blacklist"
__HELP__ = """
 Bantuan Untuk Blacklist

• Perintah : <code>{0}rallbl</code>
• Penjelasan : Menghapus semua anti gcast

• Perintah : <code>{0}addbl</code>
• Penjelasan : Menambahkan grup kedalam anti Gcast.

• Perintah : <code>{0}delbl</code>
• Penjelasan : Menghapus grup dari daftar anti Gcast.

• Perintah : <code>{0}listbl</code>
• Penjelasan : Melihat daftar grup anti Gcast.
"""


@PY.UBOT("addbl", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Caddbl", "") & ~filters.me)
async def _(client, message):
    await add_blaclist(client, message)


@PY.UBOT("delbl", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Cdelbl", "") & ~filters.me)
async def _(client, message):
    await del_blacklist(client, message)


@PY.UBOT("rallbl", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Crallbl", "") & ~filters.me)
async def _(client, message):
    await rem_all_blacklist(client, message)


@PY.UBOT("listbl", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Clistbl", "") & ~filters.me)
async def _(client, message):
    await get_blacklist(client, message)
