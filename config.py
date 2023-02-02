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
API_ID = int(getenv("API_ID", "20466793"))
API_HASH = getenv("API_HASH", "5229101f02e28e6444d1e099013e0c69")
BOT_TOKEN = getenv("BOT_TOKEN", "5757948115:AAHx3QiqEWaXuHu6SyfN2nDWm7yFsP6nymw")
SESSION_STRING = getenv("SESSION_STRING", "BQCj_pgzwrq_uDGD-qRqeht9nUziNHq1DzCgU-6DxP6CntQZhqQWj7ExQ5aEIfukCWrqI4UBbBGlxE-_vnP0ezfUgbVCxRB8RJUhLEVsiurlqy9Vo1_0ETP-iRlbLI-EKEP2QrRJa3qwmi7kdbhvN6Dxp4rl1-IBDmGy9b0-G4c95u2z7d2f19OBZ4xTj01vEJHW45MQdc4zPqcQTueul047uWqH1gSjBV8vLSKWkwMF5CXwkIF044EwxmOMvhcVl-0db8KmDdZxu366OQVJxvM_wpHFr4PL5xGS5KB4REy1WnCpus-D6Ra8_-dY0EyXJutCOjAdaKC38ZsOhcbCddmUAAAAAUtcqN4A")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Sweetu_Friends_Group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Join_channel_Or_Group")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Cutie_Bamby_bot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split(5559331038)))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
