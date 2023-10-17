from Crypto.Util.number import getPrime
from math import prod

with open("flag.txt","rb") as f:
    flag = f.read().strip()
assert len(flag) == 72

m1 = int.from_bytes(flag[:36],"big")
m2 = int.from_bytes(flag[36:],"big")

e = 65537

p,q = getPrime(2048),getPrime(2048)
n1 = p*q
c1 = pow(m1,e,n1)
print("c1 = ",c1)
print("n1 = ",n1)

primes = [getPrime(64) for _ in range(32)]
n2 = prod(primes)
c2 = pow(m2,e,n2)
print("c2 = ",c2)
print("n2 = ",n2)

# c1 =  10004937130983861141937782436252502991050957330184611684406783226971057978666503675149401388381995491152372622456604317681236160071166819028679754762162125904637599991943368450200313304999566592294442696755822585022667008378021280392976010576970877334159755332946926433635584313137140987588847077645814987268595739733550220882135750267567373532603503399428451548677091911410732474324157868011686641243202218731844256789044721309478991918322850448456919991540932206923861653518190974620161055008847475600980152660468279765607319838003177639654115075183493029803981527882155542925959658123816315099271123470754815045214896642428657264709805029840253303446203030294879166242867850331945166255924821406218090304893024711068773287842075208409312312188560675094244318565148284432361706108491327014254387317744284876018328591380705408407853404828189643214087638328376675071962141118973835178054884474523241911240926274907256651801384433652425740230755811160476356172444327762497910600719286629420662696949923799255603628210458906831175806791599965316549386396788014703044837917283461862338269599464440202019922379625071512100821922879623930069349084917919100015782270736808388388006084027673781004085620817521378823838335749279055639005125
# n1 =  343504538870081878757729748260620800783581983635281373321527119223374418103340873199654926888439040391545101913132680017655039577253974802351999985470115474655124168592386965001556620077117966153475518658881140827499124290142523464795351995478153288872749817655925271395693435582010998996210909883510311066017237567799370371513462802547313382594409676803895262837061350017911885033133654781876923251129406855067993830824618637981136966134029212516871210627954762147349788788999116702635535406398258621926040887099782494271000823401788337120154104692934583729065189687995570122890809807661370008740283447636580308161498808092269041815719148127168137018600113465985504975054319601741498799761500526467431533990903047624407330243357514588557352746347337683868781554819821575385685459666842162355673947984514687068626166144076257334426612302554448774082488600083569900006274897032242821388126274957846236552373226099112200392102883351088570736254707966329366625911183721875374731791052229266503696334310835323523568132399330263642353927504971311717117370721838701629885670598853025212521537158141447625623337563164790788106598854822686494249848796441153496412236527242235888308435573209980270776407776277489669763803746640746378181948641
# c2 =  4948422459907576438725352912593232312182623872749480015295307088166392790756090961680588458629287353136729331282506869598853654959933189916541367579979613191505226006688017103736659670745715837820780269669982614187726024837483992949073998289744910800139692315475427811724840888983757813069849711652177078415791290894737059610056340691753379065563574279210755232749774749757141836708161854072798697882671844015773796030086898649043727563289757423417931359190238689436180953442515869613672008678717039516723747808793079592658069533269662834322438864456440701995249381880745586708718334052938634931936240736457181295
# n2 =  8582505375542551134698364096640878629785534004976071646505285128223700755811329156276289439920192196962008222418309136528180402357612976316670896973298407081310073283979903409463559102445223030866575563539261326076167685019121804961393115251287057504682389257841337573435085535013992761172452417731887700665115563173984357419855481847035192853387338980937451843809282267888616833734087813693242841580644645315837196205981207827105545437201799441352173638172133698491126291396194764373021523547130703629001683366722885529834956411976212381935354905525700646776572036418453784898084635925476199878640087165680193737