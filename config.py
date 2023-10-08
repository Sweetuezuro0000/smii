"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "29516998"))
API_HASH = getenv("API_HASH", "9dad1d74a0d6253dabbb51cf6539f5f5")
BOT_TOKEN = getenv("BOT_TOKEN", "5757948115:AAHx3QiqEWaXuHu6SyfN2nDWm7yFsP6nymw")
SESSION_STRING = getenv("SESSION_STRING", "BQHCZMYAenO-cNWir8sUeZ6pjj_Bt-PHi-kxCfwST8-dWa-jGZ3yZPkNm07JHwbhm8zMTrhphP-e_dRppsSmwvPWUExMqRfrUc3ENuSuSYub673QfkW5JvgWmA_R4pABW8pyeD54MTyy7mMz5QdfGfVZwdfYoG0RiRG9Kf7RkHCnqX9vXMwPua3D0KMDrtOqFB6CRPGdrTr1JXPwJBh78nV6wWlNgaHFuSKxCfAjBahs0FUDl7gCvr_wjEDDV_I9hHEVCysGowscqFEuytyNTtHWk4Yp-ZCu4Ei5krh8Pvvi_oQq3kSfm1egXErOdRYV9WCL2mLZZMsI9Pmf-N_Oc6L0wteAHgAAAAFY9ByRAA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Sweetu_Friends_Group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sweetu_support")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Sweetu_assistant")
SUDO_USERS = list(map(int, getenv("SUDO_USERS")))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "No Pm © @sweetu_support")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
