from PIL import Image, ImageDraw
import math, os, json

S = 256
OUT = "site_src/icons"; os.makedirs(OUT, exist_ok=True)
INDIGO=(27,37,64); MADDER=(142,43,30); TURMERIC=(217,162,27); GREEN=(46,94,66); CLOTH=(243,237,223)
INK=(42,36,32); GOLD=(230,180,60); DGOLD=(150,105,30); WHITE=(255,252,240)
SKIN={'a':(210,160,110),'b':(190,135,90),'c':(160,105,70),'blue':(70,110,190)}

def ring(d, color):
    d.ellipse([4,4,S-4,S-4], fill=color)
    d.ellipse([14,14,S-14,S-14], fill=CLOTH)

def face(d, skin, cy=118, r=46):
    d.ellipse([S/2-r, cy-r, S/2+r, cy+r], fill=skin)
    # neck+shoulders
    return cy, r

def body(d, robe, top=160):
    d.pieslice([S/2-95, top, S/2+95, top+190], 180, 360, fill=robe)

def hair_crown(d, cy, r):
    d.polygon([(S/2-r-4,cy-r+18),(S/2-r+4,cy-r-26),(S/2-r/2,cy-r-4),(S/2,cy-r-34),(S/2+r/2,cy-r-4),(S/2+r-4,cy-r-26),(S/2+r+4,cy-r+18)], fill=GOLD, outline=DGOLD)
    d.ellipse([S/2-6,cy-r-16,S/2+6,cy-r-4], fill=MADDER)
def hair_jata(d, cy, r):  # sage bun
    d.ellipse([S/2-r-2,cy-r-8,S/2+r+2,cy-r+30], fill=(90,70,50))
    d.ellipse([S/2-22,cy-r-34,S/2+22,cy-r+2], fill=(90,70,50))
    d.arc([S/2-r,cy-r-6,S/2+r,cy+10], 200, 340, fill=(60,45,35), width=8)
def hair_plain(d, cy, r, col=(40,30,30)):
    d.chord([S/2-r-2,cy-r-6,S/2+r+2,cy+r-6], 180, 360, fill=col)
def hair_woman(d, cy, r):
    d.chord([S/2-r-4,cy-r-6,S/2+r+4,cy+r+10], 180, 360, fill=(35,25,25))
    d.rectangle([S/2-r-4,cy-6,S/2-r+14,cy+r+30], fill=(35,25,25))
    d.rectangle([S/2+r-14,cy-6,S/2+r+4,cy+r+30], fill=(35,25,25))
    d.ellipse([S/2-5,cy-r+2,S/2+5,cy-r+12], fill=MADDER)  # bindi
def hair_turban(d, cy, r, col=MADDER):
    d.chord([S/2-r-8,cy-r-14,S/2+r+8,cy+r-10], 180, 360, fill=col)
    d.arc([S/2-r-4,cy-r-4,S/2+r+4,cy+r-14], 200, 340, fill=GOLD, width=5)
def beard(d, cy, r, col=(230,230,230)):
    d.chord([S/2-r+6,cy-6,S/2+r-6,cy+r+34], 0, 180, fill=col)
def blindfold(d, cy):
    d.rectangle([S/2-50,cy-14,S/2+50,cy+4], fill=CLOTH, outline=INK)

def eyes(d, cy, closed=False):
    for x in (S/2-16, S/2+16):
        if closed: d.line([(x-7,cy-2),(x+7,cy-2)], fill=INK, width=3)
        else: d.ellipse([x-4,cy-6,x+4,cy+2], fill=INK)
    d.arc([S/2-12,cy+8,S/2+12,cy+24], 20, 160, fill=INK, width=3)

def attr(d, kind):
    cx, cy = S-56, S-56
    d.ellipse([cx-34,cy-34,cx+34,cy+34], fill=WHITE, outline=DGOLD, width=3)
    k = kind
    if k=='bow':
        d.arc([cx-22,cy-26,cx+22,cy+26], 250, 470, fill=INK, width=5); d.line([(cx-4,cy-24),(cx-4,cy+24)], fill=INK, width=2)
    elif k=='mace':
        d.line([(cx-14,cy+22),(cx+6,cy-6)], fill=INK, width=6); d.ellipse([cx,cy-24,cx+26,cy+2], fill=(120,120,130), outline=INK)
    elif k=='chakra':
        d.ellipse([cx-22,cy-22,cx+22,cy+22], outline=GOLD, width=6)
        for i in range(8):
            a=i*math.pi/4; d.line([(cx,cy),(cx+22*math.cos(a),cy+22*math.sin(a))], fill=GOLD, width=3)
    elif k=='dice':
        d.rounded_rectangle([cx-20,cy-20,cx+20,cy+20], 6, fill=WHITE, outline=INK, width=3)
        for px,py in [(-10,-10),(10,10),(0,0),(10,-10),(-10,10)]: d.ellipse([cx+px-3,cy+py-3,cx+px+3,cy+py+3], fill=INK)
    elif k=='book':
        d.rectangle([cx-24,cy-14,cx+24,cy+14], fill=(240,225,180), outline=(120,90,50), width=3)
        for i in range(3): d.line([(cx-18,cy-6+i*7),(cx+18,cy-6+i*7)], fill=(120,90,50), width=2)
    elif k=='sun':
        d.ellipse([cx-14,cy-14,cx+14,cy+14], fill=GOLD)
        for i in range(12):
            a=i*math.pi/6; d.line([(cx+18*math.cos(a),cy+18*math.sin(a)),(cx+26*math.cos(a),cy+26*math.sin(a))], fill=GOLD, width=3)
    elif k=='flame':
        d.polygon([(cx,cy-26),(cx+16,cy+2),(cx+8,cy+20),(cx-8,cy+20),(cx-16,cy+2)], fill=(225,110,40)); d.polygon([(cx,cy-8),(cx+7,cy+8),(cx-7,cy+8)], fill=GOLD)
    elif k=='serpent':
        pts=[(cx-24+i*3, cy+12*math.sin(i*0.5)) for i in range(17)]; d.line(pts, fill=GREEN, width=6); d.ellipse([cx+18,cy-8,cx+30,cy+4], fill=GREEN)
    elif k=='axe':
        d.line([(cx-16,cy+22),(cx+10,cy-14)], fill=INK, width=5); d.pieslice([cx-4,cy-30,cx+28,cy+2], 200, 20, fill=(150,150,160), outline=INK)
    elif k=='lotus':
        for i in range(-2,3):
            a=math.pi/2+i*0.45; d.polygon([(cx,cy+16),(cx+24*math.cos(a)-8*math.sin(a),cy+16-24*math.sin(a)-8*math.cos(a)),(cx+30*math.cos(a),cy+16-30*math.sin(a)),(cx+24*math.cos(a)+8*math.sin(a),cy+16-24*math.sin(a)+8*math.cos(a))], fill=(235,120,150), outline=MADDER)
    elif k=='crown':
        d.polygon([(cx-22,cy+12),(cx-18,cy-12),(cx-8,cy),(cx,cy-18),(cx+8,cy),(cx+18,cy-12),(cx+22,cy+12)], fill=GOLD, outline=DGOLD)
    elif k=='conch':
        d.ellipse([cx-16,cy-18,cx+16,cy+14], fill=WHITE, outline=INK, width=3); d.polygon([(cx-6,cy+10),(cx+6,cy+10),(cx,cy+26)], fill=WHITE, outline=INK)
    elif k=='water':
        for i in range(3): d.arc([cx-24,cy-14+i*10,cx+24,cy+6+i*10], 200, 340, fill=(60,120,180), width=4)
    elif k=='pen':
        d.line([(cx-16,cy+18),(cx+14,cy-16)], fill=INK, width=5); d.polygon([(cx+14,cy-16),(cx+22,cy-24),(cx+18,cy-10)], fill=GOLD)
    elif k=='boat':
        d.polygon([(cx-26,cy),(cx+26,cy),(cx+14,cy+14),(cx-14,cy+14)], fill=(120,80,50)); d.line([(cx,cy),(cx,cy-24)], fill=INK, width=3); d.polygon([(cx,cy-24),(cx+18,cy-6),(cx,cy-6)], fill=MADDER)
    elif k=='tusk':
        d.line([(cx-16,cy+20),(cx+16,cy-20)], fill=WHITE, width=10); d.line([(cx-16,cy+20),(cx+16,cy-20)], fill=INK, width=2)
    elif k=='wing':
        for i,(sp,col) in enumerate([(0,GOLD),(1,(225,110,40))]):
            for j in range(5):
                a = math.radians(150 + j*17)
                d.line([(cx+6-sp*3, cy+14), (cx+6-sp*3+34*math.cos(a), cy+14+34*math.sin(a))], fill=col, width=5)
        d.ellipse([cx+2,cy+8,cx+18,cy+24], fill=(150,105,30))
    elif k=='star':
        pts=[(cx+(26 if i%2==0 else 11)*math.cos(-math.pi/2+i*math.pi/5), cy+(26 if i%2==0 else 11)*math.sin(-math.pi/2+i*math.pi/5)) for i in range(10)]; d.polygon(pts, fill=GOLD, outline=DGOLD)

CHARS = [
 # id, name, aliases, role, side, skin, hair, robe, attr, extra
 ("vyasa","వేదవ్యాసుడు",["వ్యాసుడు"],"మహాభారత రచయిత, పరాశర సత్యవతుల కుమారుడు","guru","c","jata",(232,120,40),"pen","beard"),
 ("ganapati","గణపతి",[],"భారత రచనకు లేఖకుడు","deva","a","crown",(225,60,50),"tusk",""),
 ("vaishampayana","వైశంపాయనుడు",[],"వ్యాస శిష్యుడు, జనమేజయునికి కథ చెప్పినవాడు","guru","b","jata",(232,120,40),"book",""),
 ("sauti","ఉగ్రశ్రవుడు (సౌతి)",["ఉగ్రశ్రవుడు"],"నైమిశారణ్య మునులకు కథ చెప్పిన సూతుడు","guru","b","turban",(200,150,90),"book",""),
 ("shaunaka","శౌనకుడు",[],"నైమిశారణ్య సత్రయాగ కులపతి","guru","c","jata",(232,120,40),"flame","beard"),
 ("rajarajanarendra","రాజరాజనరేంద్రుడు",[],"వేంగి రాజు, తెలుగులో భారతము రచింపమని నన్నయను కోరినవాడు","kuru","b","crown",(120,60,110),"crown","beard"),
 ("nannaya","నన్నయ",["నన్నయభట్టు","నన్నయభట్టారకుడు"],"ఆదికవి, ఆంధ్ర మహాభారత రచన ఆరంభించినవాడు","guru","b","jata",(232,120,40),"pen","beard"),
 ("narayanabhatta","నారాయణభట్టు",[],"నన్నయకు సహాయపడిన సహపాఠి","guru","b","jata",(200,150,60),"book","beard"),
 ("paila","పైలుడు",[],"వ్యాసుని శిష్యుడు, ఋగ్వేద ప్రవర్తకుడు, ఉదంకుని గురువు","guru","b","jata",(232,120,40),"book","beard"),
 ("shuka","శుక మహర్షి",["శుకుడు"],"వ్యాసుని కుమారుడు, విరాగి","guru","a","jata",(240,200,80),"book",""),
 ("sarama","సరమ",[],"దేవతల కుక్క, జనమేజయుని శపించినది","deva","a","woman",(150,150,160),"star",""),
 ("udanka","ఉదంకుడు",["ఉత్తంకుడు"],"పైలుని శిష్యుడు, తక్షకునిపై పగతో జనమేజయుని ప్రేరేపించినవాడు","guru","b","jata",(232,120,40),"book",""),
 ("paushya","పౌష్యుడు",[],"కుండలములు దానమిచ్చిన రాజు","other","b","crown",(120,60,110),"crown","beard"),
 ("indra","ఇంద్రుడు",["దేవేంద్రుడు"],"దేవతల రాజు, వజ్రాయుధధారి","deva","a","crown",GOLD,"star",""),
 ("bhrigu","భృగువు",[],"భృగు వంశ మూలపురుషుడు, అగ్నిని శపించిన మహర్షి","guru","b","jata",(232,120,40),"flame","beard"),
 ("puloma","పులోమ",[],"భృగు మహర్షి భార్య, చ్యవనుని తల్లి","other","a","woman",(140,30,60),"lotus",""),
 ("chyavana","చ్యవనుడు",[],"పుట్టుకతోనే తేజస్వి, భృగు పులోమల కుమారుడు","guru","a","jata",(232,120,40),"sun","beard"),
 ("ruru","రురువు",[],"ప్రమద్వర భర్త, సర్పద్వేషాన్ని వదిలిన మహర్షి","guru","b","plain",(232,120,40),"serpent",""),
 ("pramadvara","ప్రమద్వర",[],"మేనక విశ్వావసుల కుమార్తె, రురువు భార్య","other","a","woman",GREEN,"lotus",""),
 ("kadru","కద్రువ",[],"కశ్యపుని భార్య, నాగుల తల్లి","other","c","woman",(60,90,60),"serpent",""),
 ("vinata","వినత",[],"కశ్యపుని భార్య, అరుణ గరుడుల తల్లి","other","a","woman",GOLD,"wing",""),
 ("aruna","అరుణుడు",[],"వినత మొదటి కుమారుడు, సూర్యుని రథసారథి","deva","a","crown",(225,110,40),"sun",""),
 ("vasuki","వాసుకి",[],"నాగరాజు, ఆస్తీకుని మేనమామ","other","c","crown",(46,94,66),"serpent",""),
 ("garuda","గరుత్మంతుడు",["గరుడుడు","సుపర్ణుడు"],"వినత కుమారుడు, అమృతము తెచ్చినవాడు, విష్ణు వాహనము","deva","a","crown",GOLD,"wing",""),
 ("parikshit","పరీక్షిత్తు",[],"అభిమన్యు కుమారుడు, తక్షకుని కాటుకు బలైన రాజు","pandava","a","crown",INDIGO,"bow",""),
 ("shamika","శమీకుడు",[],"మౌన వ్రతంలో ఉన్న మహర్షి","guru","b","jata",(232,120,40),"lotus","beard"),
 ("shringi","శృంగి",[],"శమీకుని కుమారుడు, పరీక్షిత్తును శపించినవాడు","guru","a","jata",(232,120,40),"flame",""),
 ("takshaka","తక్షకుడు",[],"నాగరాజు, ఇంద్రుని మిత్రుడు","other","blue","crown",GREEN,"serpent",""),
 ("janamejaya","జనమేజయుడు",[],"పరీక్షిత్తు కుమారుడు, సర్పయాగం చేసిన రాజు","pandava","a","crown",INDIGO,"flame",""),
 ("jaratkaru","జరత్కారువు",[],"ఆస్తీకుని తండ్రి, పితరుల కోసం వివాహమాడిన ముని","guru","b","jata",(232,120,40),"flame","beard"),
 ("astika","ఆస్తీకుడు",[],"జరత్కారు కుమారుడు, సర్పజాతిని రక్షించిన బాలుడు","guru","a","jata",(232,120,40),"serpent",""),
 ("bharata","భరతుడు",[],"దుష్యంత శకుంతలల కుమారుడు, భరత వంశ మూలపురుషుడు","kuru","b","crown",MADDER,"crown",""),
 ("pratipa","ప్రతీపుడు",[],"శంతనుని తండ్రి","kuru","b","crown",MADDER,"lotus","beard"),
 ("shantanu","శంతనుడు",[],"కురు వంశ రాజు, భీష్ముని తండ్రి","kuru","a","crown",MADDER,"bow",""),
 ("ganga","గంగాదేవి",[],"నదీ దేవత, భీష్ముని తల్లి","deva","a","woman",(120,170,220),"water",""),
 ("bhishma","భీష్ముడు",["దేవవ్రతుడు"],"గంగా శంతనుల కుమారుడు, ఆజన్మ బ్రహ్మచారి, కురు వంశ రక్షకుడు","kuru","a","crown",(210,200,190),"bow","beard"),
 ("satyavati","సత్యవతి",[],"దాశరాజు కుమార్తె, శంతనుని రాణి, వ్యాసుని తల్లి","kuru","b","woman",(120,60,110),"boat",""),
 ("dasharaja","దాశరాజు",[],"సత్యవతి పెంపుడు తండ్రి","other","c","turban",(90,70,50),"boat",""),
 ("chitrangada-k","చిత్రాంగదుడు",[],"శంతను సత్యవతుల పెద్ద కుమారుడు","kuru","a","crown",MADDER,"bow",""),
 ("vichitravirya","విచిత్రవీర్యుడు",[],"శంతను సత్యవతుల చిన్న కుమారుడు","kuru","a","crown",MADDER,"lotus",""),
 ("amba","అంబ",[],"కాశీ రాజకుమార్తె, తరువాతి జన్మలో శిఖండి","other","a","woman",(150,50,60),"flame",""),
 ("dhritarashtra","ధృతరాష్ట్రుడు",[],"అంధుడైన కురు రాజు, కౌరవుల తండ్రి","kaurava","a","crown",MADDER,"crown","blind"),
 ("pandu","పాండురాజు",[],"హస్తినాపుర రాజు, పాండవుల తండ్రి","pandava","a","crown",INDIGO,"bow",""),
 ("vidura","విదురుడు",[],"ధర్మ స్వరూపుడు, కురు మంత్రి, ధర్మ బోధకుడు","guru","b","turban",(240,225,190),"book",""),
 ("gandhari","గాంధారి",[],"ధృతరాష్ట్రుని రాణి, కళ్ళకు గంతలు కట్టుకున్న సాధ్వి","kaurava","a","woman",(150,50,60),"lotus","blindfold"),
 ("kunti","కుంతి",["పృథ"],"పాండురాజు రాణి, పాండవుల తల్లి","pandava","a","woman",(60,60,120),"sun",""),
 ("madri","మాద్రి",[],"పాండురాజు రెండవ రాణి, నకుల సహదేవుల తల్లి","pandava","a","woman",(60,100,120),"star",""),
 ("karna","కర్ణుడు",["వసుషేణుడు","రాధేయుడు"],"కుంతి సూర్యుల కుమారుడు, అంగ రాజు, దుర్యోధన మిత్రుడు","kaurava","a","crown",GOLD,"sun",""),
 ("yudhishthira","యుధిష్ఠిరుడు",["ధర్మరాజు","ధర్మజుడు"],"పెద్ద పాండవుడు, యమధర్మరాజు వరపుత్రుడు","pandava","a","crown",INDIGO,"crown",""),
 ("bhima","భీముడు",[],"వాయు పుత్రుడు, పది వేల ఏనుగుల బలుడు","pandava","b","crown",INDIGO,"mace",""),
 ("arjuna","అర్జునుడు",[],"ఇంద్ర పుత్రుడు, గాండీవధారి, లోకైక విలుకాడు","pandava","a","crown",INDIGO,"bow",""),
 ("nakula","నకులుడు",[],"అశ్వినీ దేవతల కుమారుడు, అశ్వ శాస్త్ర నిపుణుడు","pandava","a","crown",INDIGO,"star",""),
 ("sahadeva","సహదేవుడు",[],"అశ్వినీ దేవతల కుమారుడు, జ్యోతిష్య నిపుణుడు","pandava","a","crown",INDIGO,"star",""),
 ("pandavas","పాండవులు",[],"పాండురాజు ఐదుగురు కుమారులు","pandava","a","crown",INDIGO,"star",""),
 ("duryodhana","దుర్యోధనుడు",[],"పెద్ద కౌరవుడు, హస్తినాపుర యువరాజు","kaurava","b","crown",MADDER,"mace",""),
 ("dushasana","దుశ్శాసనుడు",[],"దుర్యోధనుని తమ్ముడు","kaurava","b","crown",MADDER,"mace",""),
 ("shakuni","శకుని",[],"గాంధారి సోదరుడు, జూద నిపుణుడు","kaurava","b","turban",(120,60,110),"dice",""),
 ("drona","ద్రోణుడు",["ద్రోణాచార్యుడు"],"భరద్వాజ కుమారుడు, పాండవ కౌరవుల విలువిద్యా గురువు","guru","a","jata",(240,225,190),"bow","beard"),
 ("kripa","కృపాచార్యుడు",["కృపుడు"],"కురు రాజకుమారుల మొదటి గురువు","guru","a","jata",(240,225,190),"book","beard"),
 ("parashurama","పరశురాముడు",[],"భీష్మ ద్రోణ కర్ణుల గురువు, విష్ణు అవతారము","guru","b","jata",(232,120,40),"axe","beard"),
 ("ekalavya","ఏకలవ్యుడు",[],"నిషాద రాజకుమారుడు, స్వయంశిక్షిత విలుకాడు","other","c","turban",GREEN,"bow",""),
 ("ashvatthama","అశ్వత్థామ",[],"ద్రోణుని కుమారుడు","kaurava","a","crown",(240,225,190),"star",""),
 ("purochana","పురోచనుడు",[],"లక్క ఇల్లు నిర్మించిన దుర్యోధన మంత్రి","kaurava","b","turban",(90,70,50),"flame",""),
 ("hidimbi","హిడింబి",[],"రాక్షస కన్య, భీముని భార్య","other","c","woman",GREEN,"lotus",""),
 ("ghatotkacha","ఘటోత్కచుడు",[],"భీమ హిడింబిల కుమారుడు, మాయా యోధుడు","pandava","c","crown",GREEN,"mace",""),
 ("bakasura","బకాసురుడు",[],"ఏకచక్రపుర రాక్షసుడు","other","c","turban",(60,40,40),"mace",""),
 ("drupada","ద్రుపదుడు",[],"పాంచాల రాజు, ద్రౌపది తండ్రి","pandava","b","crown",(120,60,110),"flame","beard"),
 ("draupadi","ద్రౌపది",["కృష్ణ","పాంచాలి"],"యాగాగ్ని నుంచి జన్మించిన పాంచాల రాజకుమార్తె, పాండవుల భార్య","pandava","b","woman",(140,30,60),"lotus",""),
 ("dhrishtadyumna","ధృష్టద్యుమ్నుడు",[],"ద్రుపదుని కుమారుడు, పాండవ సేనాపతి","pandava","b","crown",(120,60,110),"bow",""),
 ("krishna","శ్రీకృష్ణుడు",["కృష్ణుడు"],"యదు వంశ నాయకుడు, పాండవ సఖుడు, గీతాచార్యుడు","deva","blue","crown",GOLD,"chakra",""),
 ("dhaumya","ధౌమ్యుడు",[],"పాండవుల పురోహితుడు","guru","b","jata",(232,120,40),"flame","beard"),
 ("ulupi","ఉలూపి",[],"నాగ కన్య, అర్జునుని భార్య","other","a","woman",GREEN,"serpent",""),
 ("chitrangada","చిత్రాంగద",[],"మణిపూర రాజకుమార్తె, అర్జునుని భార్య","other","b","woman",(60,100,120),"lotus",""),
 ("subhadra","సుభద్ర",[],"కృష్ణుని సోదరి, అర్జునుని భార్య, అభిమన్యు తల్లి","pandava","a","woman",GOLD,"lotus",""),
 ("agni","అగ్నిదేవుడు",[],"అగ్ని దేవత, ఖాండవ వనాన్ని దహించినవాడు","deva","a","jata",(225,110,40),"flame","beard"),
 ("maya","మయుడు",[],"దానవ శిల్పి, మయసభ నిర్మాత","other","c","turban",(90,70,50),"star",""),
]

SIDE_RING = {'pandava':INDIGO,'kaurava':MADDER,'guru':TURMERIC,'deva':GOLD,'kuru':(110,80,120),'other':GREEN}

for cid,name,al,role,side,skin,hair,robe,at,extra in CHARS:
    im = Image.new("RGBA",(S,S),(0,0,0,0)); d = ImageDraw.Draw(im)
    ring(d, SIDE_RING[side])
    body(d, robe)
    cy,r = face(d, SKIN[skin])
    {'crown':hair_crown,'jata':hair_jata,'plain':hair_plain,'woman':hair_woman,'turban':hair_turban}[hair](d,cy,r)
    if 'beard' in extra: beard(d,cy,r, (230,230,230) if cid in ('bhishma','vyasa','drona','kripa','parashurama','pratipa','shaunaka','shamika') else (70,50,40))
    eyes(d, cy, closed=('blind' in extra))
    if 'blindfold' in extra: blindfold(d, cy)
    attr(d, at)
    # clip to circle
    mask = Image.new("L",(S,S),0); ImageDraw.Draw(mask).ellipse([0,0,S,S], fill=255)
    im.putalpha(mask); im.save(f"{OUT}/{cid}.png", optimize=True)

json.dump([{"id":c[0],"name":c[1],"aliases":c[2],"role":c[3],"side":c[4]} for c in CHARS],
          open("site_src/characters.json","w",encoding="utf8"), ensure_ascii=False, indent=1)

# Parva emblems
PARVA = ['book','flame','dice','lotus','bow','conch','chakra','bow','sun','mace','flame','lotus','crown','book','star','lotus','water','star','sun']
EMB = {1:'book',2:'dice',3:'lotus',4:'star',5:'conch',6:'chakra',7:'bow',8:'sun',9:'mace',10:'flame',11:'water',12:'crown',13:'book',14:'star',15:'lotus',16:'water',17:'star',18:'sun'}
for n,k in EMB.items():
    im = Image.new("RGBA",(S,S),(0,0,0,0)); d = ImageDraw.Draw(im)
    d.ellipse([4,4,S-4,S-4], fill=INDIGO); d.ellipse([16,16,S-16,S-16], fill=CLOTH)
    # draw attr centred and larger by drawing to temp and scaling
    t = Image.new("RGBA",(S,S),(0,0,0,0)); td = ImageDraw.Draw(t); attr(td,k)
    t = t.crop((S-56-40,S-56-40,S-56+40,S-56+40)).resize((180,180),Image.LANCZOS)
    im.alpha_composite(t,(38,38)); im.save(f"{OUT}/parva_{n:02d}.png", optimize=True)
print(len(CHARS),"characters,",len(EMB),"emblems")
