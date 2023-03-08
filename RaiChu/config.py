## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC1VIzIkTECugLZH7Mgu7WgU8drf8QPYgQSlsyDxu-gCJMdk_RMSRVDzrrbXBZhOgqiG2tbmDONu58pxOB95vW1MNAajTjZBLpNLYQD2kwyc_jiv_umWR0ulh7-0QpWFzpVRj-VpoWfP1mgURzGC4W1PxIgKRB9fvPePCo3-8dRgGF1BAO_-bxahnVbIbyzFvgF3JE2qewuYgtN-S27dyPuR9xHwPHf8hxIg3B3mDUA7cLM8ZkKAR0lhI6MNeOFn2QQbTakpVujK5J_TjXwAuiAl7h1FjY-BbCZlq_vvEddHa19G92gjJphM9EpOPN8TljUWIiJRlHikz1jUR8r3vT2AAAAAWcHpJcA")
BOT_TOKEN = getenv("BOT_TOKEN""6190039100:AAFRHuOPumSCpb8nb-gxZ_wmD6hKRRqBepg")
BOT_NAME = getenv("BOT_NAME""Lovely_x_music")
API_ID = int(getenv("API_ID", "25115940"))
API_HASH = getenv("API_HASH", "e9e647b11ae0edbe517017743a7c71cb")
OWNER_NAME = getenv("OWNER_NAME", "̶*̶•̶.̶¸̶♡̶『̶l̶o̶v̶e̶r̶ ̶✘̶j̶e̶r̶r̶ʏ̶⃝̶🧸̶』̶🕊̶.̶⋆")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "@mahi_bot_01")
BOT_USERNAME = getenv("BOT_USERNAME""@Lovely_musicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "̶*̶•̶.̶¸̶♡̶M̶A̶H̶I̶🕊̶.̶⋆")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
