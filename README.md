A simple Python script.
It copies (or steals, as it is commonly referred to among meme public administrators) memes from other meme publics specified in the code lines. It sends them to your channel as specified in the code lines.
The bot looks at the last 20 images, randomly selects one, copies it, and sends it to your meme public at a reasonable interval

# ===== TIME-BASED RANDOM INTERVAL FUNCTION =====
def get_random_interval():
    hour = datetime.now().hour
    if 6 <= hour <= 11:
        return random.randint(600, 900)      # 10–15 minutes
    elif 12 <= hour <= 17:
        return random.randint(2100, 3300)    # 35–55 minutes
    elif 18 <= hour <= 22:
        return random.randint(2700, 3300)    # 45–55 minutes
    else:
        return random.randint(3300, 6000)    # 55–100 minutes


Intervals
Morning: 10–15 minutes
Afternoon: 35–55 minutes
Evening: 45-55
Night: 55-100 (why at night? — it is possible that someone will decide to host the script, where it will run 24/7 while your hosting platform tariff is valid)

* The script was written by GPT chat, I only gave instructions

Installing Python (the programming language on which the script is based)

Windows 
https://www.python.org/downloads/windows/

Arch/Manjaro 
sudo pacman -S python python-pip






Debian/Ubuntu 
sudo apt update #recommended
sudo apt install python3 python3-pip






MacOs
Download the installer, similar to Windows (not .exe, but follow the link above and find the MacOS Python installer there)

Install the library/dependency for the script to work 
pip install telethon






Log in to my.telegram.org
—> API development tools —> create a bot (when creating a bot, select the desktop platform — recommended) —> copy the API HASH and API ID
Paste into the code lines (to edit the code, use any Python IDE; on Linux, you can use nano; the main thing is to specify the correct path to the file.
# ===== CONFIGURATION =====
api_id = 82137982173       # << Your API ID
api_hash = ‘a8d907ad798a7d98a07d98787a897d98’ # << Your API HASH





The parameters I have specified are approximate, not my data...

Change the lines of code to specify the channels from which we will steal memes 
source_channels = [
    ‘sadadasd’,
    ‘sadadasd’,
    'sadasdasd',
    ‘asdasdasd’,
    ‘asdasdasd’,
    ‘sestadsad’,
    ‘sdadasdad’,
    ‘sdadasdasda’,
    ‘sdadasda’
]  # Channels to steal memes from





Insert the link to the channel, i.e. what comes after t.me/
Without @
Not enough channels? From a new line: 
press TAB ‘namechannel’, ,
 — if you plan to add another line/channel (put a comma before the previous one if you are adding a channel) 
 — if you have finished the list, there should be no comma 

Create a new directory/folder 
Or change the location of the script to an existing one 
Important! After opening the script and registering for the first time, another file in .session format will appear in the folder. It stores your session, so if you want to open the script in the future and have it work without re-registering, do not delete the file...
 
This is a user bot; the script logs into your account, not the bot account that we usually create using BotFather.
Nothing bad will happen; the bot will send memes to the channel on your behalf. Even if you are not online, the main thing is that the script is open. 


The bot does not steal images with captions. As a rule, memes do not need captions. And if the image has a caption, it is either a contest in TGK, an advertisement, or a vlog by the admin of the victim channel...

That's it, I've given you the basics. Feel free to modify the code as you wish.
