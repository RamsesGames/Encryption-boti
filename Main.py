# Encryption-boti
import discord from discord.ext import commands from discord.ui import Button, View

إعداد البوت

intents = discord.Intents.default() bot = commands.Bot(command_prefix="!", intents=intents)

خريطة التشفير

encryption_map = { "كريديت": "كريــDــيت", "كريديتس": "كريــDــيت", "نوفا": "نوفـــــ|", "أعضاء": "اعــ4ــاء", "توكنات": "توكــ:ـــات", "فلوس": "فـــ|ـــوس", "مجاني": "مجــــ|ـــ:ــي", "مليون": "ملـــyـــون" }

دالة التشفير

def encrypt_message(message: str) -> str: for word, replacement in encryption_map.items(): message = message.replace(word, replacement) return message

كلاس للزر

class EncryptView(View): def init(self): super().init() self.add_item(EncryptButton())

class EncryptButton(Button): def init(self): super().init(label="تشفير", style=discord.ButtonStyle.primary)

async def callback(self, interaction: discord.Interaction):
    modal = EncryptModal()
    await interaction.response.send_modal(modal)

class EncryptModal(discord.ui.Modal, title="تشفير المنشور"): message = discord.ui.TextInput(label="ضع رسالتك هنا", style=discord.TextStyle.long, max_length=4000)

async def on_submit(self, interaction: discord.Interaction):
    encrypted_message = encrypt_message(self.message.value)
    embed = discord.Embed(title="🔒 تم التشفير!", description=encrypted_message, color=0x00ff00)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.command() async def عرض_التشفير(ctx): embed = discord.Embed(title="🔑 تشفير الكلمات", description="اكتب في الزر أدناه الكلمات التي تريد تشفيرها.", color=0x3498db) view = EncryptView() await ctx.send(embed=embed, view=view)

تشغيل البوت

bot.run("TOKEN")

