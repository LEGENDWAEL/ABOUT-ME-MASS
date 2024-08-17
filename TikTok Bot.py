import telebot , requests ,  time , uuid , random
import hashlib , Topython , datetime

attempt= 0
sent = 0
notsent = 0

token = "6759661633:AAGyxMfunBjib92Rb4dvRB2ztULLVltqOgo"

bot = telebot.TeleBot(token=token)

commands = [
    telebot.types.BotCommand(command='/start', description="بدء"),
    telebot.types.BotCommand(command='/information', description="معلومات"),
    telebot.types.BotCommand(command='/support', description="تواصل مع الدعم")
    ]

bot.set_my_commands(commands)

def buttons():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    StartReport = telebot.types.KeyboardButton("بدء البلاغ")
    HowUse = telebot.types.KeyboardButton("طريقة الاستخدام")
    Time = telebot.types.KeyboardButton("الوقت")
    TypeReport = telebot.types.KeyboardButton("انواع البلاغ")
            
    Progrmmer = telebot.types.KeyboardButton("المبرمج")
    ProgrmmerCh = telebot.types.KeyboardButton("حساب المبرمج")         
    
    markup.add(StartReport)
    markup.add(HowUse,Time)
    markup.add(TypeReport)
    markup.add(Progrmmer,ProgrmmerCh)
    return markup
   
def create_keyboard():
    buttons = [
        telebot.types.KeyboardButton("استغلال الأشخاص الذين تقل أعمارهم عن 18 عامًا أو إساءة معاملتهم"),
        telebot.types.KeyboardButton("العنف الجسدي والتهديدات العنيفة"),
        telebot.types.KeyboardButton("الاستغلال والاعتداء الجنسي"),
        telebot.types.KeyboardButton("الاستغلال البشري"),
        telebot.types.KeyboardButton("الإساءة للحيوان"),
        telebot.types.KeyboardButton("الأنشطة الإجرامية الأخرى"),
        telebot.types.KeyboardButton("العنف والإيذاء والاستغلال الإجرامي"),
        telebot.types.KeyboardButton("الكلام الذي يحض على الكراهية والسلوكيات البغيضة"),
        telebot.types.KeyboardButton("التحرش والتنمر"),
        telebot.types.KeyboardButton("الكراهية والتحرش"),
        telebot.types.KeyboardButton("الانتحار وإيذاء النفس"),
        telebot.types.KeyboardButton("اضطرابات الأكل وصورة الجسم غير الصحية"),
        telebot.types.KeyboardButton("الأنشطة والتحديات الخطرة"),
        telebot.types.KeyboardButton("العري والمحتوى الجنسي"),
        telebot.types.KeyboardButton("النشاط الجنسي للشباب والاستدراج الجنسي والاستغلال الجنسي"),
        telebot.types.KeyboardButton("السلوك الموحي جنسيًا بواسطة الشباب"),
        telebot.types.KeyboardButton("النشاط الجنسي للبالغين والخدمات الجنسية والاستدراج الجنسي"),
        telebot.types.KeyboardButton("عُري البالغين"),
        telebot.types.KeyboardButton("اللغة الجنسية الفاحشة"),
        telebot.types.KeyboardButton("المحتوى صادم وبشع المنظر"),
        telebot.types.KeyboardButton("معلومات خاطئة"),
        telebot.types.KeyboardButton("معلومات ضارة مضللة"),
        telebot.types.KeyboardButton("التزييف العميق والوسائط التركيبية والوسائط التي تم التلاعب بها"),
        telebot.types.KeyboardButton("السلوك المخادع والغش"),
        telebot.types.KeyboardButton("مزعج"),
        telebot.types.KeyboardButton("السلع والأنشطة الخاضعة للإرشادات التنظيمية"),
        telebot.types.KeyboardButton("المقامرة"),
        telebot.types.KeyboardButton("الكحول والتبغ والمخدرات"),
        telebot.types.KeyboardButton("الأسلحة النارية والأسلحة الخطرة"),
        telebot.types.KeyboardButton("تجارة السلع والخدمات الأخرى الخاضعة للإرشادات التنظيمية"),
        telebot.types.KeyboardButton("الغش والاحتيال"),
        telebot.types.KeyboardButton("مشاركة المعلومات الشخصية"),
        telebot.types.KeyboardButton("انتهاك الملكية الفكرية"),
        telebot.types.KeyboardButton("محتوى مرتبط بعلامة تجارية غير معلن عنه")
        
    ]
    back = telebot.types.KeyboardButton("رجوع")
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(*buttons)
    markup.add(back)
    return markup

def completeSend():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) 
    Back = telebot.types.KeyboardButton("رجوع")
    Again = telebot.types.KeyboardButton("ارسال مرة اخرى")
    Time = telebot.types.KeyboardButton("الوقت")
    markup.add(Back,Again)
    markup.add(Time)
    return markup
@bot.message_handler(commands=['start'])
def starts(message):
    caption="""
*اهلا بك في بوت ابلاغات فيديوهات تيك توك
المبرمج :* [LEGEND.WAEL](t.me/kalijohn)""",

    bot.send_video(
    message.chat.id,
    "https://t.me/yyyyyy3w/31",
    caption=caption,
    parse_mode= "Markdown",
    reply_markup=buttons())    
    bot.send_message(message.chat.id,
    "> * اختر من الازرار ما تريد : *",
    parse_mode='MarkdownV2')   

@bot.message_handler(commands=['information'])
def information(message):
    howUse(message)

@bot.message_handler(commands=['support'])
def support(message):
    programmerCh(message)
    
@bot.message_handler(func=lambda message: message.text in ["الوقت", "طريقة الاستخدام", "انواع البلاغ", "المبرمج", "حساب المبرمج", "رجوع", "بدء البلاغ","ارسال مرة اخرى"])
def Work(message):
        text = message.text
        if text == "بدء البلاغ":
            typeReport(message)
        elif text == "الوقت":
            showtime(message)
        elif text == "طريقة الاستخدام" :
            howUse(message)
        elif text == "انواع البلاغ":
            typeReport(message)
        elif text == "المبرمج" :
            programmer(message)
        elif text == "حساب المبرمج":
            programmerCh(message)
        elif text == "ارسال مرة اخرى":
            typeReport(message)
        elif text == "رجوع":
            starts(message)
            bot.clear_step_handler_by_chat_id(message.chat.id)
        
@bot.message_handler(func=lambda message: True)
def Work2(message):
    text = message.text
    if text == "استغلال الأشخاص الذين تقل أعمارهم عن 18 عامًا أو إساءة معاملتهم":
        reason = 90012
    elif text == "العنف الجسدي والتهديدات العنيفة":
        reason = 90013
    elif text == "الاستغلال والاعتداء الجنسي":
        reason = 90014
    elif text == "الاستغلال البشري":
        reason = 90015
    elif text == "الإساءة للحيوان":
        reason = 90016
    elif text == "الأنشطة الإجرامية الأخرى":
        reason = 90017
    elif text == "العنف والإيذاء والاستغلال الإجرامي":
        reason = 9001
    elif text == "الكلام الذي يحض على الكراهية والسلوكيات البغيضة":
        reason = 9002
    elif text == "التحرش والتنمر":
        reason = 9007
    elif text == "الكراهية والتحرش":
        reason = 9020
    elif text == "الانتحار وإيذاء النفس":
        reason = 90061
    elif text == "اضطرابات الأكل وصورة الجسم غير الصحية":
        reason = 90063
    elif text == "الأنشطة والتحديات الخطرة":
        reason = 90064
    elif text == "العري والمحتوى الجنسي":
        reason = 9008
    elif text == "النشاط الجنسي للشباب والاستدراج الجنسي والاستغلال الجنسي":
        reason = 90084
    elif text == "السلوك الموحي جنسيًا بواسطة الشباب":
        reason = 90085
    elif text == "النشاط الجنسي للبالغين والخدمات الجنسية والاستدراج الجنسي":
        reason = 90086
    elif text == "عُري البالغين":
        reason = 90087
    elif text == "اللغة الجنسية الفاحشة":
        reason = 90088
    elif text == "المحتوى صادم وبشع المنظر":
        reason = 9005
    elif text == "معلومات خاطئة":
        reason = 9011
    elif text == "معلومات ضارة مضللة":
        reason = 90115
    elif text == "التزييف العميق والوسائط التركيبية والوسائط التي تم التلاعب بها":
        reason = 90116
    elif text == "السلوك المخادع والغش":
        reason = 9019
    elif text == "مزعج":
        reason = 9010
    elif text == "السلع والأنشطة الخاضعة للإرشادات التنظيمية":
        reason = 9003
    elif text == "المقامرة":
        reason = 90034
    elif text == "الكحول والتبغ والمخدرات":
        reason = 90037
    elif text == "الأسلحة النارية والأسلحة الخطرة":
        reason = 90032
    elif text == "تجارة السلع والخدمات الأخرى الخاضعة للإرشادات التنظيمية":
        reason = 90038
    elif text == "الغش والاحتيال":
        reason = 9004
    elif text == "مشاركة المعلومات الشخصية":
        reason = 9018
    elif text == "انتهاك الملكية الفكرية":
        reason = 9012
    elif text == "محتوى مرتبط بعلامة تجارية غير معلن عنه":
        reason = 9021
    else:
        return
        
    GetLinks(message, reason)
        
def GetLinks(message, reason=None):
    text = """
ارسل الان رابط الفيديو واسم مستخدم وعدد الابلاغات
هكذا
*1234567890  
legend.wael
50*
※ حيث السطر الاول ايدي الفيديو
والسطر الثاني اسم مستخدم «يوزر»
والسطر الثالث عدد الابلاغات
"""
    sent = bot.reply_to(
        message, text,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )
    
    bot.register_next_step_handler(message, lambda msg: sendReport(msg , sent , reason))

def programmer(message):
    text = """
*تمت برمجة البوت بواسطة المبرمج وَائِــــــــــــــــــلْ :* [LEGEND.WAEL](t.me/kalijohn) """
    bot.reply_to(
    message,text,
    parse_mode="Markdown",
    disable_web_page_preview=True
    )

def programmerCh(message):
    text = """
*تمت برمجة البوت بواسطة المبرمج وَائِــــــــــــــــــلْ :* [LEGEND.WAEL](t.me/kalijohn)
* حساب المبرمج :* [LEGEND.WAEL](https://instagram.com/legend.wael)
 """
    bot.reply_to(
    message,text,
    parse_mode="Markdown",
    disable_web_page_preview=True
    )

def sendReport(message,send ,reason=None):
    global attempt , sent , notsent    
    texts = message.text.split('\n')
    if len(texts) == 3:
        try:
            idvideo = texts[0].strip()  
            username = texts[1].strip()
            attempts = texts[2].strip()
            id = Topython.Tiktok.information(username)['id']
            print(reason,id,username,attempts,idvideo)
                 
            for i in range(int(attempts)):
                attempt += 1
                url = "https://api16-normal-c-alisg.tiktokv.com/aweme/v2/aweme/feedback/"
                params = {
                    'report_type': "video",
                    'object_id': str(idvideo),
                    'owner_id': str(id),
                    'hide_nav_bar': "1",
                    'lang': "ar",
                    'report_desc': "",
                    'uri': "",
                    'reason': str(reason),
                    'category': "porn",
                    'request_tag_from': "h5",
                    'manifest_version_code': "270701",
                    '_rticket': str(int(time.time() * 1000)),
                    'app_language': "ar",
                    'app_type': "normal",
                    'iid': "7402994552561043206", 
                    'channel': "googleplay",
                    'device_type': random.choice(["SO-51A", "SM-G973F", "Pixel 4", "iPhone12,1"]), 
                    'language': "ar",
                    'locale': "ar",
                    'resolution': random.choice(["1096*2434", "1080*2340", "1170*2532", "1440*3040"]),  
                    'openudid': hashlib.md5(str(uuid.uuid4()).encode()).hexdigest(), 
                    'update_version_code': "270701",
                    'ac2': "wifi",
                    'cdid': str(uuid.uuid4()), 
                    'sys_region': "IQ",
                    'os_api': random.choice(["31", "30", "29", "28"]),  
                    'timezone_name': "Asia/Baghdad",
                    'dpi': random.choice(["420", "480", "400", "440"]), 
                    'carrier_region': "IQ",
                    'ac': "wifi",
                    'device_id': str(uuid.uuid4().int >> 64),  
                    'os_version': random.choice(["12", "11", "10", "9"]), 
                    'timezone_offset': "10800",
                    'version_code': "270701",
                    'app_name': "musically_go",
                    'ab_version': "27.7.1",
                    'version_name': "27.7.1",
                    'device_brand': random.choice(["docomo", "Samsung", "Google", "Apple"]), 
                    'op_region': "IQ",
                    'ssmix': "a",
                    'device_platform': "android",
                    'build_number': "27.7.1",
                    'region': "IQ",
                    'aid': "1340",
                    'ts': str(int(time.time())) 
                }
                
                headers = {
                  'User-Agent': "com.zhiliaoapp.musically.go/270701 (Linux; U; Android 12; ar_IQ; SO-51A; Build/58.2.B.0.520;tt-ok/3.12.13.2-rc.5)",
                  'Accept-Encoding': "gzip",
                  'sdk-version': "2",
                  'x-tt-token': "03d0f74e52e927278280eea250059e562b04d9b6da41ac3d3aafb9e458ca8020f7f6e1606a5e1bd5d15c8cf2a6cd48c729c0a4739854edab9c5847e93892411abbdee904e179a1144b7e961e53325213b9f07217f0e41bcf79c99851c7baa711be4f0-CkBhMjY3OTU4YTYwYzI1OWQ5MmU3YWM0NWMyMGJlZWY0ODY0MGU4NDIwMmIyMjZiMWI4ZDY5NmZjNTk1ZDU3OGY3-2.0.0",
                  'passport-sdk-version': "30790",
                  'x-tt-ultra-lite': "1",
                  'x-vc-bdturing-sdk-version': "2.2.1.i18n",
                  'x-tt-store-region': "iq",
                  'x-tt-store-region-src': "did",
                  'x-ladon': "gWoOEvznyTUkImahU0y4lAIQkBPJuuOdj9jIhV2Gnlf39Qgm",
                  'x-khronos': "1723662214",
                  'x-argus': "gTXbP/7rjfLkY7zQZTGfqVPbA58IQh6fmcrJS1CJ50O19wgDnBDHgTZ3jAlmh3GoJ9M/liFjYCkEOKFZwolR8XOha/rxogEWbLizklmRK/frcwZE0gEegWRrzobF0tN3H7j6PMpCZlHdMOMYK4W7yjiqL7HbhQ2E7YQzVTwZ3eYjPw3xPsV6aruaMC3a4MiJo3oEmVN+XZt7S3EnDHejJJ2mzSei2tiGLwNJCQNGlewg+sgwGLvtLIU841zHT20eMrHOUYjKKTsW8jxpAxiU7zw644hsJY449LDFkjj1m5YqFQ==",
                  'x-gorgon': "0404405d1000eb144f9500c0efb7b060418bbc0656daa9f85b41"
                }
                try:
                    response = requests.get(url, params=params, headers=headers).text
                    if '"status_code":0' in response:
                        sent += 1                
                    else:
                        notsent += 1            
                except requests.exceptions.ConnectionError:
                    notsent += 1            
                except requests.exceptions.BaseHTTPError:
                    notsent += 1            
                except:
                    notsent += 1
                text = f"""
*تم ارسال البلاغ :* `{sent}`
*لم يتم الأرسال  :* `{notsent}`

*المبرمج :* [LEGEND.WAEL](t.me/kalijohn)
*حساب المبرمج :* [LEGEND.WAEL](https://instagram.com/legend.wael)
"""      
                bot.edit_message_text(
                        text,chat_id=message.chat.id,
                        message_id=send.message_id,
                        parse_mode="Markdown",
                        disable_web_page_preview=True,
                        )            
            text = f"* تم ارسال * `{attempts}` *ابلاغ*"
            bot.send_message(
    message.chat.id,text,
    parse_mode="Markdown",
    reply_markup=completeSend())            
        
        except Exception as e:
            text = f"حدث خطأ غير متوقع : {e}"
            bot.reply_to(
            message,text)                           
    else:
        text = "*ارسل قيم صحيحة ثلاثة اسطر فقط *"
        bot.reply_to(
        message,text,
        parse_mode="Markdown")        

def typeReport(message):
    text = "* هذه انواع البلاغات !*"
    bot.reply_to(
    message,text,
    parse_mode="Markdown",
    reply_markup=create_keyboard())
    

def howUse(message):
    text = """
يمكنك استخدام البوت مجانا 
كل العليك ضغط * بدء البلاغ * 
وترسل له *ايدي الفيديو* و *يوزر الشخص* و *عدد الابلاغات* ويتم الابلاغ بسرعة متوسطة 
> ملاحظة الابلاغ حقيقي 100%
 *غير مسؤول عن سوء الاستخدام*
"""
    bot.reply_to(
    message,text,
    parse_mode='MarkdownV2')

def showtime(message):
    now = datetime.datetime.now()
    time = now.strftime("%Y/%m/%d %H:%M")
    text = f"*الوقت الان :* `{time}`"
    bot.reply_to(
    message,text,
    parse_mode="Markdown"
    )


bot.polling()