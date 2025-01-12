from ubot import *

__MODULE__ = "VoiceChat"
__HELP__ = """
Bantuan Untuk Voice Chat

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.

• Perintah: <code>{0}joinvc</code>
• Penjelasan: Untuk bergabunf voice chat grup.

• Perintah: <code>{0}leavevc</code>
• Penjelasan: Untuk meninggalkan voice chat grup.
"""


@PY.UBOT("startvc", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Cstartvc", "") & ~filters.me)
async def _(client, message):
    await start_vctools(client, message)


@PY.UBOT("stopvc", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Cstopvc", "") & ~filters.me)
async def _(client, message):
    await stop_vctools(client, message)


@PY.UBOT("joinvc", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Cjoinvc", "") & ~filters.me)
async def _(client, message):
    await join_os(client, message)


@PY.UBOT("leavevc", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("Cleavevc", "") & ~filters.me)
async def _(client, message):
    await turun_os(client, message)
