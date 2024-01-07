import os

BOT_TOKEN = os.environ.get('BOT_TOKEN', 'Pulsar')
ADMIN = os.environ.get('ADMIN', 5934725286)
GROUP = os.environ.get('GROUP',1635762236)
AUTHORIZED_USER_IDS = [5934725286, 5377327708, 5817420325, 1918582402, 699882662, 1257545168, 1753264718, 1203220311, 6955248384, 752492336, 1673876488, 650599868, 1732613271, 1180727254, 1309190580, 967340481, 5322473767, 6426386490, 10368310407]
COMMANDS = ['/start', '/show', '/users', '/stats', '/test', '/neon']
global last_update_id
last_update_id = -1
last_sent_time = None
VOICES = [
    ("https://raw.githubusercontent.com/guys-voice/voices/main/1.ogg", "V.V.Putin"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/2.ogg", "Kulib qoydim sanga, shavkat"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/3.ogg", "Kulib qoydim"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/4.ogg", "Nima bu"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/5.ogg", "Temola pilot 1"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/6.ogg", "Bir marta yozding indamadim"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/7.ogg", "Yot hammang, yot"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/8.ogg", "Gazni pulini bering"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/9.ogg", "Yaxsh"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/10.ogg", "Ya uka chichyording"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/11.ogg", "Hate emas, maqsad unique bo'lish"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/12.ogg", "Ollo rozi bo'sin"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/13.ogg", "Cringe"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/14.ogg", "Cringe 2"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/15.ogg", "Tupoy odam qomadi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/16.ogg", "Sohib"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/17.ogg", "Sohib king"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/18.ogg", "Sohib bot"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/19.ogg", "Qilig'ing yoqmaydi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/20.ogg", "Qarameng"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/21.ogg", "Ohio"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/22.ogg", "Na mehr qoldi na oqibat"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/23.ogg", "Murdoch university"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/24.ogg", "Maqsad yoq albatta"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/25.ogg", "O bu mano nima o'zi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/26.ogg", "Abdu kesang tiqamiz"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/27.ogg", "Katta tezlik bilan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/28.ogg", "Kim u"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/29.ogg", "Jiyaniim yopishtiraman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/30.ogg", "Oh no Jahongii"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/31.ogg", "Eshikni oching, gazdan keldik"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/32.ogg", "Man sani dadangmanmi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/33.ogg", "Yomurod dadam o'ldiradiku"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/34.ogg", "Chilparchin, uzr so'rayman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/35.ogg", "Yamon, tovushcha nima diyopti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/36.ogg", "E bot bo'lopti Abdu"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/37.ogg", "Bir marta yozding indamadim"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/38.ogg", "Oh no cringe"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/39.ogg", "LOL 1"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/40.ogg", "Untitled"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/41.ogg", "Yemagan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/42.ogg", "Ko'rsa yitalaydi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/43.ogg", "LOL 2"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/44.ogg", "Nima bu nima"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/45.ogg", "Cringe 3"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/46.ogg", "17 secs of bullying Abdu"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/47.ogg", "Goher nasihatlari"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/48.ogg", "Cringe 4"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/49.ogg", "Bichara"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/50.ogg", "Abduni bitta gapi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/51.ogg", "Abdu 106"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/52.ogg", "Uxlamoqchiman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/53.ogg", "LOL 3"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/54.ogg", "LOL 4"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/55.ogg", "LOL 5"),
#   ("https://raw.githubusercontent.com/guys-voice/voices/main/56.ogg", "Shoxijon"), # BANNED BY AUTHOR
    ("https://raw.githubusercontent.com/guys-voice/voices/main/57.ogg", "Untitled"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/58.ogg", "Yaxshi, sohib sila"),
#   ("https://raw.githubusercontent.com/guys-voice/voices/main/59.ogg", "Massivni demanstratsiya qilaylik"), # BANNED BY AUTHOR
#   ("https://raw.githubusercontent.com/guys-voice/voices/main/60.ogg", "Yok"), # BANNED BY AUTHOR
#   ("https://raw.githubusercontent.com/guys-voice/voices/main/61.ogg", "Yolka"), # BANNED BY AUTHOR
#   ("https://raw.githubusercontent.com/guys-voice/voices/main/62.ogg", "Yaxshi, krisa"), # BANNED BY AUTHOR
    ("https://raw.githubusercontent.com/guys-voice/voices/main/63.ogg", "Mirkoff"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/64.ogg", "Untitled"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/65.ogg", "Kimdir yitiribti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/66.ogg", "Untitled"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/67.ogg", "Mirko supuruvchi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/68.ogg", "Problem netu"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/69.ogg", "Ha"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/70.ogg", "Xo'sh 1"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/71.ogg", "Shoxa b*a"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/72.ogg", "Sui"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/73.ogg", "Yo murod, b*a"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/74.ogg", "Haaa 1"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/75.ogg", "Haaa 2"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/76.ogg", "Jahongir pakinul gruppe 1"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/77.ogg", "Murod sila"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/78.ogg", "Sabab yoq"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/79.ogg", "Jahongir pakinul gruppe 2"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/80.ogg", "Temola pilot 2"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/81.ogg", "Tezlash shoxa"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/82.ogg", "Ignor"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/83.ogg", "Wowo"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/84.ogg", "So'ra tualetga bo'sayam"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/85.ogg", "Yamon yegan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/86.ogg", "Vote qilamiz"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/87.ogg", "Yo murod, mirko"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/88.ogg", "Iye mirko"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/89.ogg", "Ha xo'sh"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/90.ogg", "Jiyan zvezdasan"),
#   ("https://raw.githubusercontent.com/guys-voice/voices/main/91.ogg", "Yemadi"), # DOES NOT WORK BY MISTAKE (I HAVE RUN THE PROGRAM BEFORE UPLOADING THE FILE)
    ("https://raw.githubusercontent.com/guys-voice/voices/main/92.ogg", "Bu hech nima bermaydi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/93.ogg", "Shavkat pakinul gruppe"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/94.ogg", "Yemadi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/95.ogg", "O sila"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/96.ogg", "Mirko qo'shiqchi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/97.ogg", "Makkilladizla"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/98.ogg", "Maqtov yorlig'i"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/99.ogg", "LOL 6"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/100.ogg", "Bachala tez, tez"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/101.ogg", "DNA, yomayo"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/102.ogg", "Boshqasi bormi, tasha"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/103.ogg", "Abduni sotaman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/104.ogg", "Ko'rganman buni, abdu"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/105.ogg", "Abdu tiqadi sani"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/106.ogg", "Raxmat, bilamiz"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/107.ogg", "Arqada o'tirib, oldindan olaymi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/108.ogg", "Qizlani arqasini olopti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/109.ogg", "Yo murod"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/110.ogg", "S*koptimi jahon"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/111.ogg", "Shaxmat ko'ropti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/112.ogg", "Qizig'i yoq, shukur"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/113.ogg", "Yoshda holi, yosh"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/114.ogg", "Shavkatni statistikasi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/115.ogg", "Abdu, o'zingdan ketma"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/116.ogg", "O' shuhrat"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/117.ogg", "Maqsad yoq, O'"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/118.ogg", "Mativatsion video ko'rdingmi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/119.ogg", "Unutamiz"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/120.ogg", "Bilmayman e"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/121.ogg", "Bo'lli raxmat e"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/122.ogg", "Jahon debatga nol"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/123.ogg", "N klassiko qachon"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/124.ogg", "Xo'sh 2"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/125.ogg", "Sabab yoq, baxti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/126.ogg", "Toshkent sliv zonaku"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/127.ogg", "Nosni kayfi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/128.ogg", "Abdu, nachag'"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/129.ogg", "Xo'sh, variant beringla"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/130.ogg", "Abdu za*bat qilopti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/131.ogg", "Nima bu, shoxa"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/132.ogg", "Mirko selfimi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/133.ogg", "Iy sohib jirkanch"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/134.ogg", "Gilos zo'r ekan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/135.ogg", "Muzika nima diyopti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/136.ogg", "Shavkat qo'shiqchi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/137.ogg", "Jahon xeyter bo'ma 1"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/138.ogg", "Jahon xeyter bo'ma 2"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/139.ogg", "Don't interrupt me"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/140.ogg", "Shavkat admin ber"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/141.ogg", "Tezroq yoz jahon"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/142.ogg", "Bl*"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/143.ogg", "Sohibdir o'sha"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/144.ogg", "IQni ko'p ishlatmangla"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/145.ogg", "Qizig'i bor deb o'ylaydi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/146.ogg", "Mumkin emas dedila"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/147.ogg", "Qo'ling yopishganmi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/148.ogg", "Jahon qattasan ukam"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/149.ogg", "Maktab qachondan ekan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/150.ogg", "IQcha"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/151.ogg", "Aqllimisan mirko"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/152.ogg", "Man ijod qiganman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/153.ogg", "Chiqeveradi..."),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/154.ogg", "Hamma ko'rib bo'lli"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/155.ogg", "Akangni chempionligi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/156.ogg", "Shuhrat sila"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/157.ogg", "Qerasan baxti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/158.ogg", "Avtobus kutib o'tirimman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/159.ogg", "Bordizlami"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/160.ogg", "Tax bo'llim boromman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/161.ogg", "Kelinni aytmadi boxa"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/162.ogg", "Kelinni oti jahona"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/163.ogg", "Juda off bo'lli"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/164.ogg", "Umman off bo'mapti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/165.ogg", "Oshib tushopti shoxa"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/166.ogg", "Jahon s..."),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/167.ogg", "Qizla choqiropti kelingla"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/168.ogg", "Shoxa off"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/169.ogg", "Tezlash boxa"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/170.ogg", "Sohib krinjoviy king"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/171.ogg", "Da*uya bo'lib ketadiku"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/172.ogg", "Turutu turutu"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/173.ogg", "Mirkoni kodi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/174.ogg", "Shukur sila"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/175.ogg", "Qisib o'tirish kerak edi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/176.ogg", "I wanna thank me"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/177.ogg", "LOL 7"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/178.ogg", "Maqsad munnan ko'rish"),
    #("https://raw.githubusercontent.com/guys-voice/voices/main/179.ogg", "Abdullo kayfullo"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/180.ogg", "Tushunningmi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/181.ogg", "Puling bo'sa kel"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/182.ogg", "O'tmishni unut"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/183.ogg", "Mirko sani o'diramiz"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/184.ogg", "Mirko krisada"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/185.ogg", "Mirkoga oqibat yoq"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/186.ogg", "Sherxan baxodirxon"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/187.ogg", "Nag'zmi shumo"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/188.ogg", "Mirko off topic"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/189.ogg", "Baxodir tushundizmi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/190.ogg", "Orqadan gapirma"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/191.ogg", "Uzur shukur"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/192.ogg", "Xich qerni bilmaysan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/193.ogg", "Sohib da*bayob"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/194.ogg", "Mirko sila"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/195.ogg", "Shukur murod bo'ma"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/196.ogg", "Tug'ilsang vinavat emasmanku"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/197.ogg", "Bir gap aytmayda"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/198.ogg", "Rost gapiromman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/199.ogg", "Xich kim bilmaydi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/200.ogg", "Yaxshi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/201.ogg", "Manimcha yoq"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/202.ogg", "Shavkat obviyuslashopsan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/203.ogg", "Beeline kirib yotibti"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/204.ogg", "Voiceni ignor qiladi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/205.ogg", "Qachon o'tiramiz"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/206.ogg", "Murodmisan"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/207.ogg", "Ignormas ko'chagaman"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/208.ogg", "Sanam bezor bo'llingmi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/209.ogg", "Videoni ko'rmapsanku"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/210.ogg", "Shercha bo'ganim yoq"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/211.ogg", "Jiyancham"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/212.ogg", "Nima diysan e"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/213.ogg", "Choq 50 ming"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/214.ogg", "Obro'ni to'kdi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/215.ogg", "Chi chi chi"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/216.ogg", "Albatta"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/217.ogg", "Qanchaga oloding"),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/218.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/219.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/220.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/221.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/222.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/223.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/224.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/225.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/226.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/227.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/228.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/229.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/230.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/231.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/232.ogg", ""),
    ("https://raw.githubusercontent.com/guys-voice/voices/main/233.ogg", ""),
]
