import os , random , datetime , base64 , logging , asyncio , time
from telethon.tl import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
import requests
import datetime
from justwatch import JustWatch
from telegraph import Telegraph, upload_file, exceptions
class AiArt:
	def __init__(self, query, *vars):
		self.r = requests.Session()
		self.query = query
		self._main_()
	def _main_(self):
		authorization = requests.post("https://securetoken.googleapis.com/v1/token?key=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw", data={"grant_type": "refresh_token", "refresh_token": "AOEOulYxSBtIcIUxZJXlnRNkUtRRFaqDpaQeOEu8ELuSg2LovVGbHSBNf1vFjFD6vVzsSqj81NO5-XUdueMr5g100iP8gN8Hit0zRaJDxVdIcGSL8ktAq9PoET806WIUThrJKAheBz4DTqiDCCRX5UeR23xClCObrhbCWvqmXobRUe09_yAPanY"}).json()
		self.r.headers = {"authorization":f"{str(authorization['token_type']).lower()} {str(authorization['access_token'])}"}
		self.id = self.r.post("https://paint.api.wombo.ai/api/tasks", data='{"premium":false}').json()["id"]
		self.r.put("https://paint.api.wombo.ai/api/tasks/"+self.id, data='{"input_spec":{"prompt":"'+self.query+'","style":3,"display_freq":10}}')
	def Generator(self):
		while True:
			response = self.r.get("https://paint.api.wombo.ai/api/tasks/"+self.id).json()
			if response["state"] == "completed":
				return response["result"]["final"]
			time.sleep(1.5)
api_id = '6034319'
api_hash = 'ec87c3a00c745ce8ef9566e3019c26b6'
client = TelegramClient('session', api_id, api_hash)
telegraph = Telegraph()
r = telegraph.create_account(short_name=logging.getLogger(__name__))
auth_url = r["auth_url"]
@client.on(events.NewMessage(outgoing=True,pattern=".قول"))
async def _(event):
        await event.edit('انتظر...')
        from gtts import gTTS
        chat = await event.get_chat()
        if 'بالانكليزي' in event.raw_text :
            text = event.raw_text.replace('.قول بالانكليزي','')
            lang = 'en'
        if 'بالعربي' in event.raw_text :
            text = event.raw_text.replace('.قول بالعربي','')
            lang ='ar'
        save = gTTS(text=text, lang=lang, slow=False)
        await client.delete_messages(chat, event.message)
        save.save(f'{text}.mp3')
        await client.send_file(event.to_id,f'{text}.mp3',caption=f'Done pronounced \nword pronunciation : {text}\nLanguege word : {lang}\n\n•••••••••••••••\nBy : @Huks3 , @i_m_q')
        os.remove(f'{text}.mp3')

@client.on(events.NewMessage(outgoing=True,pattern=".تلكراف (ميديا|تيكست)"))
async def _(event):
    await event.edit('انتظر...')
    from datetime import datetime
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "ميديا":
            downloaded_file_name = await client.download_media(
                r_message,      
            )
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit("تم التحميل في {} ب {} ثواني.".format(downloaded_file_name, ms))
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await event.edit("خطأ " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await event.edit("تم الرفع على https://telegra.ph{} ب {} ثانية.".format(media_urls[0], (ms + ms_two)), link_preview=True)
        elif input_str == "تيكست":
            user_object = await client.get_entity(r_message.from_id)
            title_of_page = user_object.first_name
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await client.download_media(
                    r_message,
                    Config.TMP_DOWNLOAD_DIRECTORY
                )
                m_list = ''
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(
                title_of_page,
                html_content=page_content
            )
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit("Pasted to https://telegra.ph/{} in {} seconds.".format(response["path"], ms), link_preview=True)
    else:
        await event.edit("لازم تسوي رد ع رساله")
def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")
@client.on(events.NewMessage(outgoing=True, pattern=".فحص"))
async def _(event):
      await client(JoinChannelRequest("@a6pthon"))
      sec = time.time()
      y = datetime.datetime.now().year;m = datetime.datetime.now().month;dayy = datetime.datetime.now().day;day = datetime.datetime.now().strftime("%A");
     
      start = datetime.datetime.now()
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
Ok ..
-- -- -- -- -- -- -- -- --"""
)
      end = datetime.datetime.now()
      ms = (end - start).microseconds / 1000
      chat = await event.get_chat()
      await client.delete_messages(chat,event.message)
      await client.send_file(event.to_id,'https://telegra.ph/file/3765697b5e7dd71dcd924.mp4',caption=f"""
- -- -- -- -- -- -- -- --
36pthon source
Python : 3.8
36pthon : 1.0
Ping : {ms}
Date : {y}/{m}/{dayy} - {day}
Id : {event.sender_id}
Dev : @Huks3 , @i_m_q
Ch : @a6pthon
-- -- -- -- -- -- -- -- --""")
@client.on(events.NewMessage(outgoing=True, pattern=".مربعات"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "🟧",
        "🟧🟧",
        "🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        ".عكس",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧",
        "🟧🟧",
        "🟧",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])
@client.on(events.NewMessage(outgoing=True, pattern=".خنيث"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("خنيث")
    animation_chars = [
        """-- -- -- -- -- -- -- -- -- --
🟥🟥🟥🟥🟥🟥
🟧🟧🟧🟧🟧🟧
🟨🟨🟨🟨🟨🟨
🟩🟩🟩🟩🟩🟩
🟦🟦🟦🟦🟦🟦
🟪🟪🟪🟪🟪🟪
-- -- -- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- -- -- --
 🟥🟥🟥🟥🟥🟥
 🟧🟧🟧🟧🟧🟧
 🟨🟨🟨🟨🟨🟨
 🟩🟩🟩🟩🟩🟩
 🟦🟦🟦🟦🟦🟦
 🟪🟪🟪🟪🟪🟪
-- -- -- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- -- -- --
  🟥🟥🟥🟥🟥🟥
  🟧🟧🟧🟧🟧🟧
  🟨🟨🟨🟨🟨🟨
  🟩🟩🟩🟩🟩🟩
  🟦🟦🟦🟦🟦🟦
  🟪🟪🟪🟪🟪🟪
-- -- -- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- -- -- --
   🟥🟥🟥🟥🟥🟥
   🟧🟧🟧🟧🟧🟧
   🟨🟨🟨🟨🟨🟨
   🟩🟩🟩🟩🟩🟩
   🟦🟦🟦🟦🟦🟦
   🟪🟪🟪🟪🟪🟪
-- -- -- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- -- -- --
    🟥🟥🟥🟥🟥🟥
    🟧🟧🟧🟧🟧🟧
    🟨🟨🟨🟨🟨🟨
    🟩🟩🟩🟩🟩🟩
    🟦🟦🟦🟦🟦🟦
    🟪🟪🟪🟪🟪🟪
-- -- -- -- -- -- -- -- -- --""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.ساعه'))
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(outgoing=True, pattern=".الثواني"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً  !
الثواني الحالية : {sec}
-- -- -- -- -- -- -- -- --"""
)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.الارض'))
async def clock(event):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 20])
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.السنه'))
async def alsna(event):
    chat = await event.get_chat()
    await client.delete_messages(chat, event.message)
    await client.send_file(event.to_id, 'https://telegra.ph/file/5ba847f1a679479aacd29.jpg',
                           caption='ذا الله حك السنه')
@client.on(events.NewMessage(pattern="ايدي"))
async def id(event):
    await event.reply(f"ايدي حسابك : `{event.sender_id}`")        
@client.on(events.NewMessage(outgoing=True, pattern=".نسخ"))
async def _(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(m)
@client.on(events.NewMessage(pattern=r".صوره", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.edit_to_msg_id:
       await event.edit("قم بالرد على مستخدم !")
       return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
       await event.edit("قم بالرد على ملصق !")
       return
    chat = "@DownloadStickersBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("لا يعمل على البوتات !")
       return
    await event.edit("يتم التحويل ..")
    async with event.client.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=658563529))
              await event.client.forward_messages(chat, reply_message)
              response = await response
          except YouBlockedUserError:
              await event.edit("(@DownloadStickersBot) ")
              return
          if response.text.startswith("hi"):
             await event.edit("alooo")
          else:
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.جلب'))
async def dato(event):
    chat = await event.get_chat()
    await client.delete_messages(chat,event.message)
    hu = await event.get_reply_message()
    pic = await hu.download_media()
    await client.send_file('me',pic,caption='تم الجلب بنجاح By @huks3 + By @i_m_q')
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.مح'))
async def kshf(event):
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(pattern=r"^\.معلوماتي"))
async def reg(event):
        me = await client.get_me()
        await event.edit(me.stringify())
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.فضائي'))
async def kshf(event):
    deq = deque(list("👽👾👿💀👻👹👺"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.افكر'))
async def afkr(event):
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.قمور'))
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):     
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(outgoing=True, pattern=".التاريخ"))
async def _(event):
      y = datetime.datetime.now().year;m = datetime.datetime.now().month;dayy = datetime.datetime.now().day;day = datetime.datetime.now().strftime("%A");m9zpi = f"{y}/{m}/{dayy} - {day}";sec = time.time()
      await event.edit(f"""
`-- -- -- -- -- -- -- -- --
التاريخ : {m9zpi}
-- -- -- -- -- -- -- -- --`"""
)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.ضحك'))
async def moon(event):
    deq = deque(list("😹🤣😂😹🤣😂"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.مكعب'))
async def cube(event):
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.مطر'))
async def andre(event):
    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(1)

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.نجمه'))
async def andre(event):
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.قلب'))
async def heart(event):
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(2)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.حلويات'))
async def heart(event):
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(48):
        await event.edit("".join(deq))
        deq.rotate(3)
@client.on(events.NewMessage(outgoing=True, pattern=".مص"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
`مصه عزيزي`
-- -- -- -- -- -- -- -- --"""
)
def get_stream_data(query):
    stream_data = {}
    try:
        country = 'IQ'
    except Exception:
        country = "IN"
    # Cooking Data
    just_watch = JustWatch(country = country)
    results = just_watch.search_for_item(query = query)
    movie = results['items'][0]
    stream_data['title'] = movie['title']
    stream_data['movie_thumb'] = "https://images.justwatch.com"+movie['poster'].replace("{profile}","")+"s592"
    stream_data['release_year'] = movie['original_release_year']
    try:
        
        stream_data['release_date'] = movie['cinema_release_date']
    except KeyError:
        try:
            stream_data['release_date'] = movie['localized_release_date']
        except KeyError:
            stream_data['release_date'] = None

    stream_data['type'] = movie['object_type']

    available_streams = {}
    for provider in movie['offers']:
        provider_ = get_provider(provider['urls']['standard_web'])
        available_streams[provider_] = provider['urls']['standard_web']
    
    stream_data['providers'] = available_streams

    scoring = {}
    for scorer in movie['scoring']:
        if scorer['provider_type']=="tmdb:score":
            scoring['tmdb'] = scorer['value']

        if scorer['provider_type']=="imdb:score":
            scoring['imdb'] = scorer['value']
    stream_data['score'] = scoring
    return stream_data
def pretty(name):
    if name=="play":
        name = "Google Play Movies" 
    return name[0].upper()+name[1:]

def get_provider(url):
    url = url.replace("https://www.","")
    url = url.replace("https://","")
    url = url.replace("http://www.","")
    url = url.replace("http://","")
    url = url.split(".")[0]
    return url
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.مشاهدة'))
async def _(event):
    if event.fwd_from:
        return
    query = event.text.replace('.مشاهدة ','')
    await event.edit("البحث عن مواقع...")
    streams = get_stream_data(query)
    title = streams['title']
    thumb_link = streams['movie_thumb']
    release_year = streams['release_year']
    release_date = streams['release_date']
    scores = streams['score']
    try:
        imdb_score = scores['imdb']
    except KeyError:
        imdb_score = None
    
    try:
        tmdb_score = scores['tmdb']
    except KeyError:
        tmdb_score = None
        
    stream_providers = streams['providers']
    if release_date is None:
        release_date = release_year

    output_ = f"**الفلم**\n`{title}`\n**تاريخ الاصدار:**\n`{release_date}`"
    if imdb_score:
        output_ = output_ + f"\n**IMDB: **{imdb_score}"
    if tmdb_score:
        output_ = output_ + f"\n**TMDB: **{tmdb_score}"

    output_ = output_ + "\n\n**موجود على:**\n"
    for provider,link in stream_providers.items():
        if 'sonyliv' in link:
            link = link.replace(" ","%20")
        output_ += f"[{pretty(provider)}]({link})\n"
    
    await client.send_file(event.chat_id, caption=output_, file=thumb_link,force_document=False,allow_cache=False, silent=True)
    await event.delete()
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.كشف'))
async def kshf(event):
    if event.reply_to_msg_id: 
        r_message = await event.get_reply_message()
        chat = await event.get_chat()
        t = await client.get_entity(r_message.from_id)
        
        username = '@'+t.username
        phone = t.phone
        id = t.id
        name = t.first_name
        y = datetime.datetime.now().year;m = datetime.datetime.now().month;dayy = datetime.datetime.now().day;day = datetime.datetime.now().strftime("%A");m9zpi = f"{y}/{m}/{dayy} - {day}";sec = time.time()
        await event.edit(f"""
- -- -- -- -- -- -- -- --
36pthon source
NAME : {name}
USERNAME : {username}
PHONE : {phone}
36pthon : 1.0
Date : {m9zpi}
Id : {id}
Dev : @Huks3 , @i_m_q
-- -- -- -- -- -- -- -- --""")
    else:
        chat = await event.get_chat()
        name = chat.first_name
        username = '@'+chat.username
        phone = chat.phone
        id = chat.id
        await event.edit(f'الايدي : {id}\nالاسم : {name}\nاليوزر : {username}\nرقمه : {phone}\nشكرا لأستخدامك سورس عطبثون')
@client.on(events.NewMessage(pattern=r"\.salamanca"))
async def salamanca(event):
        await event.edit("salamanca on top...")
        time.sleep(1)
        await event.edit("[...                         ] 5%")
        time.sleep(1)
        await event.edit("[.....                       ] 10%")
        time.sleep(1)
        await event.edit("[.......                     ] 15%")
        time.sleep(1)
        await event.edit("[.........                   ] 20%")
        time.sleep(1)
        await event.edit("[..........                  ] 35%")
        time.sleep(1)
        await event.edit("[...........                 ] 45%")
        time.sleep(1)
        await event.edit("[.............               ] 50%")
        time.sleep(1)
        await event.edit("[...............             ] 60%")
        time.sleep(1)
        await event.edit("[.................           ] 70%")
        time.sleep(1)
        await event.edit("[....................        ] 75%")
        time.sleep(1)
        await event.edit("[........................    ] 80%")
        time.sleep(1)
        await event.edit("[..........................  ] 90%")
        time.sleep(1)
        await event.edit("[............................] 100%")
        time.sleep(1)
        await event.edit("salamanca blood")
        time.sleep(1)
        await event.edit("salamanca money")
        time.sleep(1)
        await event.edit("👴🏿👴🏿👴🏿👴🏿👴🏿👴🏿👴🏿👴🏿👴🏿👴🏿 زنوج السلامانكا")
@client.on(events.NewMessage(outgoing=True, pattern=".السنة"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً  !
السنة : {y}
-- -- -- -- -- -- -- -- --"""
)
@client.on(events.NewMessage(outgoing=True, pattern=".اوامر الوقتي"))
async def _(event):
      await event.reply("""
-- -- -- -- -- -- -- -- --
       36pthon source

بايو [لتفعيل البايو الوقتي]
اسم [لتفعيل الاسم الوقتي]
الثواني [يضهر لك الثواني]
التاريخ [يضهر لك التاريخ اليوم]
السنة [يضهر لك السنه الحاليه]
الوقت [يضهرلك جميع التفاصيل]

By @huks3 By @i_m_q
-- -- -- -- -- -- -- -- --"""
)
@client.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""
[. ᯏ𝙖6𝙥𝙩𝙝𝙤𝙣 - ᥴ𝗆𝖽 ᭡ .](t.me/a6pthon)
✦┅━╍━╍╍━━╍━━╍━┅✦

- مرحبا بك عزيزي المستخدم هذه هي قائمة اوامر السورس 

.صوره ◂ امر تحويل الملصق الى صورة
.غرامات ◂ مثلا [.غرامات بغداد:خصوصي:1:أ] وينطيك الغرامات الي ع سيراة
.ذكاء ◂ امر الذكاء الاصطناعي [.ذكاء + جملتك بالانكليزي فقط]
.تحميل ◂ امر تحميل من التيكتوك [.تحميل + رابط الفيديو]
.جلب ◂ امر سحب الصورة الذاتية المؤقتة [.جلب بالرد على الصورة]
.تيك ◂ امر معلومات تيكتوك [.تيك + اليوزر]
.اوامر التسلية ◂ اوامر تسلية
مشاهدة ◂ [مشاهدة + اسم الفلم ] ينطيك معلومات الفلم او المسلسل
.وقتي ◂ اوامر الوقتي
.غادر ◂ مغادرة الكروب
.تيليكراف ◂ (.تيليكراف ميديا) للصور (.تيليكراف تيكست) للرسائل"""
)
@client.on(events.NewMessage(pattern=r".ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await client(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)
@client.on(events.NewMessage(outgoing=True, pattern=".اوامر التسلية"))
async def _(event):
      await event.edit("""
-- -- -- -- -- -- -- -- --
       36pthon source

1 - مح
2 - فضائي
3 - افكر
4 - قمور
5 - ضحك
6 - مكعب
7 -مطر
8- قلب
9- حلويات
salamanca -10
11- شرطه
12- نار
13- طياره
14 - تفاعلات
15- رفع ابن زنا
16 - رفع كحبه
17- ساعه
18- الارض
19- الثواني
20 - السنة
21- الوقت
22- نسويه
23- مص
24- .روسيا
25 - خنيث
26 - طوبة
27 - اقمار
28- سني
29- اقمار2
30- عشوائي
31- دائره
32- يد
33- العد التنازلي
By @huks3 By @i_m_q
-- -- -- -- -- -- -- -- --"""
)
@client.on(events.NewMessage(outgoing=True, pattern=".انشاء (g|c)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    type_of_group = event.pattern_match.group(1)
    group_name = '@a6pthon !'
    if type_of_group == "g":
        try:
            result = await client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                users=["@GoogleIMGBot"],
                # Not enough users (to create a chat, for example)
                # Telegram, no longer allows creating a chat with ourselves
                title=group_name
            ))
            created_chat_id = result.chats[0].id
            await client(functions.messages.DeleteChatUserRequest(
                chat_id=created_chat_id,
                user_id="@GoogleIMGBot"
            ))
            result = await client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await event.edit("تم انشاء كروب بنجاح\nالرابط : {}".format(result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    elif type_of_group == "g" or type_of_group == "c":
        try:
            r = await client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                title=group_name,
                about="Ch : @a6pthon\nDev : @Huks3 , @i_m_q",
                megagroup=False if type_of_group == "c" else True
            ))
            created_chat_id = r.chats[0].id
            result = await client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await event.edit("تم انشاء قناة  بنجاح\nالرابط : {}".format(result.link))
        except Exception as e:
            await event.edit(str(e))
    else:
        await event.edit("Read .helpme to know how to use me")
@client.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


@client.on(events.NewMessage(pattern=r".سني", outgoing=True))
async def _(event):
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    hhu = await client.get_me()
    hu = hhu.first_name
    await event.edit(f"تم التفجير بواسطة السني {hu}......")
    await asyncio.sleep(2)

@client.on(events.NewMessage(pattern=r".ملصق", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.edit_to_msg_id:
       await event.edit("`يجب الرد على رسالة !`")
       return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
       await event.edit("`يجب الرد على رسالة !`")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("`جار تحويل النص الى ملصق ..`")
    async with event.client.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response
          except YouBlockedUserError:
              await event.edit("```Please unblock me (@QuotLyBot) u Nigga```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else:
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
@client.on(events.NewMessage(outgoing=True, pattern=".روسيا"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("روسيا")
    animation_chars = [
        """-- -- -- -- -- -- -- --
⬜⬜⬜⬜⬜
🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
 ⬜⬜⬜⬜⬜
 🟦🟦🟦🟦🟦
 🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
  ⬜⬜⬜⬜⬜
  🟦🟦🟦🟦🟦
  🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
   ⬜⬜⬜⬜⬜
   🟦🟦🟦🟦🟦
   🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
    ⬜⬜⬜⬜⬜
    🟦🟦🟦🟦🟦
    🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
     ⬜⬜⬜⬜⬜
     🟦🟦🟦🟦🟦
     🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@client.on(events.NewMessage(outgoing=True, pattern=".طوبة"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("طوبة")
    animation_chars = [

        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])

@client.on(events.NewMessage(outgoing=True, pattern=".العد التنازلي"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("العد التنازلي")
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
@client.on(events.NewMessage(outgoing=True, pattern=".دائره"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("دائره")
    animation_chars = [

        "⚫", "⬤", "●", "∘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])




@client.on(events.NewMessage(outgoing=True, pattern=".النضام الشمسي"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("النضام الشمسي")
    animation_chars = [

        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@client.on(events.NewMessage(outgoing=True, pattern=".عشوائي"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("عشوائي")
    animation_chars = [
        "◧", "◨", "◧", "◨", "‎"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])



@client.on(events.NewMessage(outgoing=True, pattern=".اقمار"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("اقمار")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@client.on(events.NewMessage(outgoing=True, pattern=".يد"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("يد")
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
@client.on(events.NewMessage(outgoing=True, pattern=".اقمار2"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("اقمار2")
    animation_chars = [        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
@client.on(events.NewMessage(outgoing=True, pattern=".نسويه"))
async def _(event):
      await event.edit("""
-- -- -- -- -- -- -- -- --
🍆 , 🍌 , 🥒 , 🍑 , 🍒 , 🏳️‍⚧️ , 🏳️‍🌈 , 🩴
ملاحظة : يجب على النسويه ان تختار شيء واحد فقط !
ملاحظة : النسويات مو بشر
-- -- -- -- -- -- -- -- --"""
)
@client.on(events.NewMessage(pattern=r"\.شرطه"))
async def police(event):
    await event.edit("🔵 police here open your door 🔴")
    time.sleep(3)
    await event.edit("👮 beep oob a sound of police 👮")
    time.sleep(1)
    await event.edit("👮 beep oob a sound of police 👮.")
    time.sleep(1)
    await event.edit(" 🔵stand clear don man`ll talk 👮 ")
    time.sleep(2)
    await event.edit("🔵 you cant stand where i stand 🔴")
    time.sleep(2)
    await event.edit("👮 beep oob a sound of police 👮")
    time.sleep(1)
    await event.edit("👮 beep oob a sound of police . 👮")
    time.sleep(1)
    await event.edit("👮 police here open your fucking door 👮")

@client.on(events.NewMessage(pattern=r"\.نار"))
async def nar(event):
    await event.edit("جاري اشعال النار")
    time.sleep(0.3)
    await event.edit("تحضر")
    time.sleep(0.3)
    await event.edit("استعد")
    time.sleep(0.3)
    await event.edit(" ابدا ")
    time.sleep(0.5)
    await event.edit("اخر مره")
    time.sleep(0.2)
    await event.edit("اخر مره والله")
    time.sleep(0.3)
    await event.edit("وين البانزين")
    time.sleep(0.3)
    await event.edit("🔥🔥🔥")
    time.sleep(0.3)
    await event.edit("نار حته ابو حطب ممسويها هه 🔥🔥🔥")

@client.on(events.NewMessage(pattern=r"\.طياره"))
async def nar(event):
    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----")
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await asyncio.sleep(3)


@client.on(events.NewMessage(pattern=r"\.تفاعلات"))
async def tfa3lat(event):
    for i in range(5):
        await event.edit("أ‿أ")
        await event.edit("╥﹏╥")
        await event.edit("T＿T")
        await event.edit("πーπ")
        await event.edit("⋟﹏⋞")
        await event.edit("☯️﹏☯️")
        await event.edit("☍﹏⁰")
        await event.edit("ಥ_ʖಥ")
        await event.edit("ಢ_ಢ")
        await event.edit("༎ຶ ෴ ༎ຶ")
        await event.edit("Ｔ▽Ｔ")
        await event.edit("；へ：")
        await event.edit("ToT")
        await event.edit("╥﹏╥")

@client.on(events.NewMessage(outgoing= True,pattern=r'^\.رفع كحبه'))
async def abnk7ba(event):
    chat = await event.get_chat()
  
    await event.edit(
                     f'⇜ ابشر رفعته كحبه 👙  ')

@client.on(events.NewMessage(outgoing= True,pattern=r'^\.رفع ابن زنا'))
async def abnzna(event):
    chat = await event.get_chat()

    await event.edit(
                     f'⇜ ابشر رفعته ابن زنا 💦  ')
@client.on(events.NewMessage(outgoing= True,pattern=r'^\.تيك'))
async def e(event):
                chat = event.get_chat()
                h = event.text
                mes = h.replace('.تيك ','')
                await event.edit('انتظر...')
                url = f"https://tiktok-best-experience.p.rapidapi.com/user/{mes}"
                headers = {
		"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
		"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
		"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
	}
                r = (requests.get(url,headers=headers).json())
                
                if r['status'] == 'ok':
                 
                  insta = ''
                  uid = ''
                  name=''
                  yc=''
                  bio=''
                  h=''
                  fg=''
                  fs=''
                  p= r['data']['avatar_medium']['url_list'][0]
                  try:
                      uid = r["data"]["uid"]
                  except:
                      uid='not found'
                  try:
                      yc = r["data"]["youtube_channel_id"]
                  except:
                      yc='not found'
                  try:
                      h = r["data"]["total_favorited"]
                  except:
                      h='0'
                  try:
                      fg = r["data"]["following_count"]
                  except:
                      fg='0'
                  try:
                      fs = r["data"]["follower_count"]
                  except:
                      fs='0'
                  try:
                      name = r["data"]["nickname"]
                  except:
                      name='not found'
                  try:
                      bio = r["data"]["signature"]
                  except:
                      bio = 'not found'
    
                  try:
                      insta = r["data"]["ins_id"]
                  except:
                      insta = 'not found'
           
                await event.edit(f'''
• Name : {name}

• Followers : {fs}

• Following : {fg}

• Instagram : {insta}

• Youtube Chanel : {yc}

• Likes : {h}

• Bio : {bio}

• iD : {uid}
= = = = = = = = = = = = = = = = = = = = 
By : @Huks3 by : @i_m_q''')
@client.on(events.NewMessage(pattern=r"\.تحميل .", outgoing=True))
async def sj(event):
    command = event.raw_text.split(" ")
    keyword = command[1]
    chat = await event.get_chat()
    await event.edit('انتظر...')

    r = requests.get(f"https://ammxx.ml/API/TikTok/tik_avadown.php?url={keyword}").json()
    mp4 = r['medias'][0]['url']
    tit = r['title']
    qu = r['medias'][0]['quality']
    si = r['medias'][0]['formattedSize']
    mp3 = r['medias'][2]['url']
    qu3 = r['medias'][2]['quality']
    si3 = r['medias'][2]['formattedSize']

    await client.delete_messages(chat, event.message)
    await client.send_file(event.to_id, mp4,
                           caption=f'Done Download\nTitle : {tit}\nQuality : {qu}\nSize : {si}\n\n••••••••••••••\nBy : @Huks3 by @i_m_q ')
    await client.send_file(event.to_id, mp3,
                           caption=f'Done Download\nTitle : {tit}\nQuality : {qu3}\nSize : {si3}\n\n••••••••••••••\nBy : @Huks3 By @i_m_q')


@client.on(events.NewMessage(outgoing=True, pattern=r'^\.ذكاء'))
async def hne(event):
    chat = await event.get_chat()
    command = event.raw_text.replace('.ذكاء ','')
    
    await event.edit('انتظر...')

    await client.send_file(event.to_id, AiArt(query=command).Generator(),
                           caption=f'Done Art \nArt name : {command}\n\n•••••••••••••••\nBy : @Huks3 , @i_m_q')
    await client.delete_messages(chat, event.message)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.غرامات'))
async def bi(event):
    await event.edit('انتظر...')
    k = event.raw_text.replace('.غرامات ', '')
    r = k.split(':')[0]
    t = k.split(':')[1]
    n = k.split(':')[2]
    l = k.split(':')[3]
    headers = {
        'authority': 'itp.gov.iq',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'ar;q=0.5',
        'cache-control': 'max-age=0',
        'origin': 'https://itp.gov.iq',
        'referer': 'https://itp.gov.iq/carSearch.php',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
    }
    data = {
        'CarLetter': l,
        'CarNumber': n,
        'CarType': t,
        'CarReg': r,
        'submit': 'بحث',
    }
    r = requests.post('https://itp.gov.iq/carSearch.php', headers=headers, data=data)

    if 'لا توجد غرامات مفروضة على المركبة - شكرا لالتزامكم بقواعد السير الامن ' in r.text:
        await event.edit('لا توجد غرامات مفروضة على المركبة - شكرا لالتزامكم بقواعد السير الامن ')
    else:
        suop = BeautifulSoup(r.text, "html.parser")
        m = suop.find_all("table", {"class": "blueTable"})
        for i in m:
            u = (str(i.text).replace('<td>', ''))
            o = str(u.replace('رقم المخالفة', ''))
            ou = str(o.replace('مبلغ المخالفة', ''))
            oo = str(ou.replace('مكان المخالفة', ''))
            uu = str(oo.replace('الوقت', ''))
            await event.edit(uu)
@client.on(events.NewMessage(outgoing=True, pattern=".بايو"))
async def _(event):
    hg = event.raw_text.replace('.بايو ', '')
    DEL_TIME_OUT = 60
    LOGS = logging.getLogger(__name__)
    normzltext = "1234567890"
    namerzfont = "1𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
    if event.fwd_from:
        return
    await event.edit(f'-----------\nتم تفعيل البايو الوقتي بنجاح !\n{hg}\n-----------\nDev : @Huks3 , @i_m_q')
    while True:
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = f"{hg} |️ {HM}"
        LOGS.info(bio)
        try:
            await client(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
@client.on(events.NewMessage(outgoing=True, pattern=".اسم"))
async def _(event):
    DEL_TIME_OUT = 60
    LOGS = logging.getLogger(__name__)
    normzltext = "1234567890"
    namerzfont = "1𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
    try:
        if event.fwd_from:
            return
        await event.edit('-----------\nتم تفعيل الاسم الوقتي بنجاح !\n-----------\nDev : @Huks3 , @i_m_q')
        while True:
            HM = time.strftime("%I:%M")
            for normal in HM:
                if normal in normzltext:
                    namefont = namerzfont[normzltext.index(normal)]
                    HM = HM.replace(normal, namefont)
            name = f"{HM}"
            LOGS.info(name)
            try:
                await client(
                    functions.account.UpdateProfileRequest(
                        first_name=name
                    )
                )
            except FloodWaitError as ex:
                LOGS.warning(str(e))
                await asyncio.sleep(ex.seconds)
            await asyncio.sleep(DEL_TIME_OUT)
    except:
        await event.edit('-----------\nالاسم الوقت مفعل من قبل !!\n-----------\nDev : @Huks3 , @i_m_q')
@client.on(events.NewMessage(outgoing=True, pattern=".الوقت"))
async def _(event):
      y = datetime.datetime.now().year;m = datetime.datetime.now().month;dayy = datetime.datetime.now().day;day = datetime.datetime.now().strftime("%A");m9zpi = f"{y}/{m}/{dayy} - {day}";sec = time.time()
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً  !
السنة : {y}
الشهر : {m}
تاريخ اليوم : {dayy}
اليوم : {day}
الثواني الان : {sec}
-- -- -- -- -- -- -- -- --"""
)
@client.on(events.NewMessage(outgoing=True, pattern='.سكرين'))
async def hf(event):
    chat = await event.get_chat()
    query = event.raw_text.replace('.سكرين ','')
    q = (f'https://mr-abood.herokuapp.com/Screenshot/API?Link={query}')
    await client.delete_messages(chat, event.message)
    await client.send_file(event.to_id, q,caption=f'Done screen \nscreen url : {query}\n\n•••••••••••••••\nBy : @Huks3 , @i_m_q')
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.بينتريست'))
async def bv(event):
    chat = await event.get_chat()
    command = event.raw_text.split(" ")
    query = event.raw_text.replace('.بينتريست ','')
    
    url = 'https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/my_pins/?q=avengers&rs=rs&eq=naruto%208K&etslf=15092&term_meta[]=avengers%7Crecentsearch%7C4&data={"options":{"article":null,"applied_filters":null,"appliedProductFilters":null,"auto_correction_disabled":false,"corpus":null,"customized_rerank_type":null,"filters":null,"query":"'+query+'","query_pin_sigs":null,"redux_normalize_feed":true,"rs":"direct_navigation","scope":"pins","source_id":null,"no_fetch_context_on_resource":false},"context":{}}&_=1662617352806'
    headers = {
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'csrftoken=0e018d7a846bbb9b8fa7832662c63ed2; _b="AWbcYA0FqcRO6pt4TXz6L96G+/bXeigv/QK5RoON+UKFoKfeyCZZ/IQx+Ka7R9tJhOc="; g_state={"i_l":0}; _auth=1; _pinterest_sess=TWc9PSZoUjNlM2o4dlk2Nis0K3M5bThOOWlzcVVZQ2xKK0grQVhScjU0Vk14M0dYTEswUUMrako1YmNiYk8xaStHSHpnQ2Ezbzc1Rlg1TkZqZkM3djVqRkg2VEg3MTNGZEd4UURRZHc2Njlpam5BdmxFV1hhaW9LNzJ2TWpLdkg3K3krTDJzYXhqbndWeXltYUh5NzVQNEF0M2NQZTc4dVl5RkhDNlFkbGNBa1F0cU0rSEpHclY0dDJHRGdrRWdRdkpoeXhBK3lmMkp3MHh2Z3NJZzVkVm1WTDdJd2ZsQTB3YWI4N2h3c3hnU2tiWU9zYW5sQUJxWFBiSElyRGZTY3hWd2MrZURnSk9idnZ2cFhoUmtTTlRjWGhxTHhNVE9EaTVSQ1FMM2toQmRIYjdCSmVDSklJSFNlMVVycjJ6STdXbnNBaG5nL0xRUFVZYmhxZEtMOUJTKzNqTE9zK1ZYTDNHeEpzOWxXTmpVWkRXRHg4SDUyVkZIZEtxMzZBVnVBZjd2czBKSHp1K0QyV21rOEt3OG03MUdYcVFIVTEvci9VRW9jblplSHE2TGFQZVgrKzlvS2JJK2pRcis1S1JHbU9IYUtYSkVJaENaT05pZXNvd2krMUxNeDVkYnhtK3N0cEMwMzRlMSsrZXVQUEpZdTJtSXZsTTBxWGs1ZmtqYnBUcmJJMlEwSW55ak1mWXVtclV5bzhtTEhadGtLV21LbkVqdzFKelBZWmVlZWE4eGRVNjQ4NFNablRDUTJnb3F0ZTVkWWx1UHdjOXVJWGtwRWtsSit2dHpkMmVzeUxEOHFzdzdmS3NKVnFITDJwUjlDYnRMWWJSeURtQWZ5MloxV1c0WEp4RkQ3SWRKTm1Bc0ZYMDdUR0pubkRXUVpKRS8xNmxQNWNvYUpSb3dtNHlWencvWncrS2hkOXFBNlNsTW5Ha1lpVkdhZ2dMQmhsOUxGN2s4cmdwQUpDRmV5ODVDb0sreWtnNzdhdjZUWjBnLzJ4MlJjdXVHOVI2ZXovUm1KTTQwVmFTREJTUkVvWUF3WEx0QnhwWEtEU2NxSmpXZjNWREcxTWpTb0MrOCtiOW1JbFEvOUlUUFJCNTc4SzJkSTByOG5ieW94UWZ0OWVFR3RPUmpWRGZ2NFRYNTYzRGd5RVlZK1o3UkhVTG5xVUZ5cVlzakl6a2U0Vks1YmQ5SUpkckgvVTlTY2tqblVIU3dmUnRTdkhtL2F6SnFWUnVsMkVwZGRyUlQ5Rk9CMlNzb2VieFYxTDc2UU8vcnBZcjFMR1h5aFV2VFRSRlFrbGppczNYYVh4NXAwcG54TUx3TnpiczZhQTJOMHMxdzgyVitFPSZtUTFDTnV5UTdrNit6R0Q5VDJyS0dXZGN3R0k9; _routing_id="2446e1bc-a370-4e3c-8e3c-ec9ec536d20f"; sessionFunnelEventLogged=1; cm_sub=none',
        'pragma': 'no-cache',
        'referer': 'https://www.pinterest.com/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-app-version': 'a332b16',
        'x-pinterest-appstate': 'active',
        'x-pinterest-experimenthash': 'c519017d978aab61a2dc39b3ed657696bcb130c2aa27632777fcafe1dcae2bce503172a4f5554e6bf64bdce07f29915629f8bc0c126647930a83f3fe6f8d8795',
        'x-pinterest-pws-handler': 'www/search/[scope].js',
        'x-pinterest-source-url': '/search/pins/?q=avengers&rs=typed&term_meta[]=avengers%7Ctyped',
        'x-requested-with': 'XMLHttpRequest',
    }
    req = requests.get(url, headers=headers)
    u='لا بأس من وجود بعض العري في Pinterest، ولكن ضمن حدود الآداب.'
   
    try:
        import random
        h = ['1','2','3','4','5']
        q = req.json()['resource_response']['data']['results'][int(random.choice(h))]['images']['orig']['url']
        await client.delete_messages(chat, event.message)

        await client.send_file(event.to_id, q,
                               caption=f'Done Serch \nserch name : {query}\n\n•••••••••••••••\nBy : @Huks3 , @i_m_q')
                               
    except Exception as s:
        uk=(requests.get(url, headers=headers).json()['resource_response']['data']['nag']['messages'])
        await client.delete_messages(chat, event.message)
        um = f'{uk}'.replace('"','')
        un = um.replace("'",'')
        ub = un.replace('[','')
        uv = ub.replace(']','')
        await client.send_message(chat,f'{uv}',parse_mode='htm')
@client.on(events.NewMessage)
async def my_event_handler(event):
    
        if event.raw_text == 'منصب':
            if event.sender_id == 1887927704:
                await event.reply('اي')
            else:
                await event.edit('هذا الامر خاص للمطورين')
client.start()
client.run_until_disconnected()
