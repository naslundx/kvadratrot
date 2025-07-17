Astronomi kan kallas en av de absolut äldsta vetenskaperna. “Redan de gamla grekerna” diskuterade de ljuspunkter som kunde observeras på himlavalvet och vad de kunde tänkas betyda. Stjärnbilder fick en stor betydelse för långväga resenärer eftersom det gick att navigera efter dem och i och med de första teleskopen under 1600-talet tog observationen av universum en rejäl fart.

Idag har människan lyckats sända upp föremål i omloppsbana och vidare bortom solsystemet. Människan har till och med, i egen hög person, besökt månen! Bragder som vi absolut inte lyckats med utan matematikens hjälp. Triviala frågor som hur mycket bränsle som behöver lastas kan snabbt bli svåra: Ju mer bränsle som tas med, desto mer väger farkosten. När farkosten väger mer går det åt mer bränsle. Vilken mängd är den optimala men ändå tillräcklig för att astronauterna med marginal tar sig tillbaka? Samma beräkningar tillämpas när det gäller mängden bränsle som ska tas med på flygplan men är ännu viktigare vid rymdfärder. Den genomsnittliga kostnaden för att sända upp ett kilogram i omloppsbana rör sig om hundratusentals kronor!

Mer avancerade saker såsom vilket datum som är det bäst lämpade för raketens uppskjutning och hur lång tid det tar att resa, eller i vilken vinkel som rymdraketerna ska skickas upp för att komma till rätt plats, vore alla omöjliga att besvara utan matematiken. Det finns också mycket svåra och ännu olösta problem såsom N-kropparproblemet. Med alla planeter, månar, asteroider och solen samt gravitationskrafter mellan alla dessa, är vårt solsystem verkligen stabilt? Kommer det någon dag krascha ihop? Det har visat sig vara mycket svårt att avgöra.

Vår egen planet påverkas av vad som sker runtom oss i universum, varför det är i vårt intresse att veta mer om det. Vår egen kalender är också nära länkad till astronomin, vilket vi ska se nedan. Viktiga vetenskapliga teorier såsom relativitetsteorin har kunnat styrkas genom observationer av stjärnornas position kring solen vid en solförmörkelse.

Relativitetsteorin förutsade att ljuset på väg till oss från stjärnor bakom solen skulle böjas på grund av gravitationen och därför ge en illusion av att stjärnorna befinner sig på andra platser. Detta visade sig vara korrekt och hade inte varit mätbart om det inte var en solförmörkelse. Ljuset från solen är annars så starkt att man inte ser stjärnorna som på himlavalvet är belägna nära solen. Lyckligtvis har vi goda formler för att förutspå solförmörkelser in på sekunden och var på jorden de går att observera.

## Koordinater i rymden
Det finns några olika sätt att uttrycka sin nuvarande plats här på jorden. Det normala förfaringssättet är med sfäriska koordinater, där jorden ses som en stor boll (en sfär) och en position uttrycks som en vinkel i två olika riktningar utifrån jordens mitt. Latitud mäter vinkeln från ekvatorn mot nord- eller sydpolen, alltså i nord-syd-riktningen. Longitud mäter vinkeln åt andra hållet, i väst-öst-riktningen, och utgår genom internationell standard från Greenwich, England. Här är denna vinkel noll.

När det inte gäller ett ändligt objekt som jorden utan den till synes oändliga värld som kosmos utgör blir problemet något svårare. Det vanliga är att utgå härifrån jorden. Även om vår planet inte utgör universums eller ens solsystemets centrum så är det den plats vi befinner oss på och därmed en naturlig utgångspunkt.

På samma sätt som latitud och longitud utgör ett positionssystem på jorden, används inom astronomin de motsvarande termerna dek-lination och rektascension för att uttrycka en vinkel från vår planets mittpunkt. De ackompanjeras med ett värde för avståndet från jorden.

![Alt text](wtf)

Vinklar och ett avstånd från en given punkt används alltså för att uttrycka en position. För den som är bekant med vektorer eller komplexa tal i polär form bör matematiken bakom vara tydlig.
Andra system och referenspunkter finns, som lämpar sig bättre för föremål på riktigt stora avstånd, exempelvis avlägsna galaxer. På något sätt måste vi i alla fall kunna uttrycka positioner och rörelser i rymden för att planera satellituppskjutningar, följa planeter och stjärnor och kunna förutsäga sol- och månförmörkelser.

## Skjuta upp och orientera satelliter
Satelliter faller inte ner på jorden igen utan håller sig hela tiden ovanför oss. Detta beror på att de rör sig precis tillräckligt fort runt jorden, inte så fort att de flyger härifrån men inte så pass långsamt att de faller ner och orsakar allvarlig huvudvärk på någon stackars förbipasserande.

Genom kunskaper i fysik kan vi använda oss av Newtons mycket kända lagar för gravitation och centripetalacceleration. Då är det möjligt att härleda formler för hur avstånd till jorden hänger ihop med hastigheten som behövs för att hålla sig kvar i omloppsbana, nämligen:

$$v=\sqrt{\frac{3,987 \cdot 10^{14}}{r+6371000}}$$

v är hastigheten i meter per sekund och r är avståndet från jordytan i meter. Tack vare kunskaper i algebra och ekvationslösning kan vi också ge formeln med det omvända sambandet, hur avståndet beror av hastigheten:

$$ r=\frac{3,987 \cdot 10^{14}}{v^2} - 6371000$$

Konstanten \\(3,987 \cdot 10^{14}\\) är resultatet av jordens massa gånger gravitationskonstanten och värdet 6 371 000 (meter) representerar medelavståndet från jordytan till vår planets mittpunkt, med andra ord jordens radie. Gravitationskonstanten är det värde som gör att formler om gravitation stämmer överens med vår värld. En formel som förutsäger hur snabbt något faller mot marken ska självklart ge svar som vi vet är korrekta (stämmer med experiment). Den kan också modifieras och ge upphov till andra världar, till exempel inom datorspel (se kapitlet Datorspel och animerade filmer).

Ur formlerna kan vi utläsa, utan att först behöva skicka upp en satellit, att den behöver lägre hastighet ju längre bort den är.  Detta beror på att jordens gravitation påverkar den mindre på större avstånd. Mycket nära jorden måste en satellit färdas mycket snabbare än jordens egen rotation för att inte ramla ner. Långt bort måste den istället färdas mycket långsamt för att inte slungas iväg.

I och med detta spektrum av hastigheter, från mycket snabbare till mycket långsammare, måste det därför finnas något särskilt avstånd där satelliten behöver lika lång tid för att genomföra ett varv runt jorden som det tar för jorden att rotera ett varv. Med andra ord att både satelliten och planeten har samma vinkelhastighet. Detta sär-skilda avstånd, kallat geostationär omloppsbana, har en mycket önskvärd egenskap. En satellit placerad där befinner sig rakt ovanför samma punkt på jorden hela tiden.

För att befinna sig i geostationär bana runt jorden måste satelliten hålla en hastighet om 11 068,7 kilometer per timme (3074,6 meter per sekund). Om vi sätter in detta i vår ekvation får vi:

$$r=\frac{3,987 \cdot 10^14}{3074,6^2} -6371000=35 786 000 \text{(meter)}$$

På detta avstånd från jorden, 35 786 kilometer, befinner sig de flesta väder- och TV-satelliter eftersom en mottagare då inte ständigt behöver justeras. Den kan hela tiden peka mot samma plats på himlen. Mottagaren kan till exempel vara en TV-antenn eller parabol.

Att veta avståndet är bara början, att bestämma hastighet och vinkel för att ta sig upp i rymden och kunna placera en satellit på just denna höjd och med just den hastigheten utgör mycket komplicerade geometriska beräkningar, inget vi ska våga oss på här. Poängen är ändå förhoppningsvis klar, inget av detta vore möjligt utan djupa studier i geometri, trigonometri, algebra och förmågan att formulera en ekvation som representerar verkligheten, vilket är precis vad tillämpad matematik handlar om.


## Astronomin på vår jord
Rymdforskningen stillar inte bara en nyfikenhet kring vad som finns “där ute” utan skänker oss även mycket användbar information om jorden. En solfläck är ett område på solen som är kallare på grund av störningar i solens magnetfält. Vår upptäckt och förståelse av den så kallade solfläckscykeln, där antalet solfläckar varierar och når sitt maximum i genomsnitt vart elfte år, har visat sig viktig för oss. Denna process ökar nämligen strålningen mot oss på jorden vilket stör radiokommunikation och förändrar temperaturen.

Vår kalender är också baserad på rörelser av jorden runt solen (ungefär ett år) och månen runt jorden (ungefär en månad) och jordens egen rotation (ungefär ett dygn). Dessa saker är däremot inte enkelt delbara med varandra, så rent matematiskt har det visat sig vara mycket svårt att få en perfekt kalender. Med perfekt menas en som är lätt att använda men följer jordens rörelser noga. Är kalenderåret för kort eller långt jämfört med jordens restid runt solen börjar årstiderna glida runt över året. Sommaren hamnar på vintermånaderna och vice versa.

Faktum är att det egentligen tar ungefär 365,24 dygn för oss att färdas ett varv runt solen, vilket betyder att ett år egentligen är ungefär en fjärdedels dygn längre än de 365 vi normalt kallar ett år. För att inte årstiderna ska förskjutas, vilket var ett problem innan systemet började tillämpas, har skottdagen kommit till. Vart fjärde år förlänger den året med en dag. Fyra år räknas då som 365+365+365+366=1461 dagar. Under samma tid har \\(365,24 \cdot 4=1490,96\\) dygn egentligen passerat, det vill säga att vi har räknat 0,04 dygn för mycket. Det är alltså fortfarande fel, om än ett mycket mindre sådant. På 25 år har kalendern endast förskjutits en dag.

Vi kan bättre än så. På hundra år hinner det bli \\(100 \cdot 0,04=4\\) dagar för mycket och detta bekämpas med en ny regel som säger att skottår jämnt delbara med 100 inte är skottår.  Dessa år blir då istället lite för korta vilket jämnar ut beräkningen i slutändan. Om 8000 år har kalendern inte förskjutits mer än en dag, men det är väl rimligt att anta att vår nuvarande kalender sedan länge fallit i glömska vid det laget.


## Fotografera rymden

Tidigare har vi diskuterat hur digitala fotografier är uppbyggda och sparas på datorer. Här ska vi diskutera fotograferingen som sådan, i synnerhet av objekt i rymden.

Med ljusföroreningar menas det ljus som kommer från närliggande källor och stör vid fotograferingen av rymden. På grund av upplysta vägar, städer och byggnader måste idag astronomiska observationer förläggas till avlägsna platser såsom öknar eller högt belägna berg, men inte heller detta är utan sina problem. Jorden är ändå alltid upplyst och atmosfären stör ljuset från andra himlakroppar vilket gör fotografering från ytan svår, precis som när man fotograferar motiv framför ljusa fönster. Det bästa är att fotografera med teleskop i rymden.

Mycket matematik går in i beräkningar för avstånd mellan och storleken av linser i allt från digitalkameror till små och stora teleskop. I och med att jorden roterar och satelliter runt jorden förflyttas pekar inte ett teleskop mot samma stjärna under särskilt lång tid. För detta progammeras datorer som automatiskt justerar dem i rätt hastighet. Särskilt viktigt blir det eftersom fotograferingen ibland kan äga rum under flera timmar.

Slumpmässighet är något som detaljerat studeras i matematik och det är just vad man kan säga om det “brus” av olika ljuskällor som inkräktar på en bild. Särskilt jobbigt är det då stjärnorna själva är så avlägsna och därmed små och ljussvaga. Detta kan motverkas genom att använda sig av längre exponeringstider (den tid som linsen är öppen och tar in ljus) och genom att blanda flera bilder genom olika typer av ljusfilter. Resultaten blir spektakulära, klara bilder av föremål nästintill obegripligt långt bort. Dessutom kan en hel redigering ingå i slutändan för att retuschera bort fula detaljer.


## Astronomiska siffror

Uttrycket “astronomiskt antal” brukar användas för att beskriva ofattbart enorma tal som antalet sandkorn på jorden eller antalet syremolekyler i atmosfären. Kanske kommer uttrycket från att tal inom astronomin oftast är mycket stora. Vårt moderna talsystem ger oss bra verktyg både för att hantera sådana enorma tal men också för att kunna sätta dem i perspektiv och jämföra dem. Något sådant är inte att ta för givet, dess utveckling tog många tusen år.

Med \\(10^x\\) menas en etta med \\(x\\) nollor efter. Därför är \\(10^4\\) hela tio gånger större än \\(10^3\\) som i sin tur är tio gånger större än \\(10^2\\). På så vis blir det lättare att prata om följande:

- <p>Sveriges längd från norr till syd: \\(1,5 \cdot 10^3 \,\text{km} (=1 574 \,\text{km})\\)</p>
- <p>Jordens diameter: \\(	1,3 \cdot 10^4 \,\text{km} (=12 735 \,\text{km})\\)</p>
- <p>Solens diameter: \\(	1,4 \cdot 10^6 \,\text{km}\\)</p>
- <p>Avståndet till solen: \\(	1,5 \cdot 10^8 \,\text{km}\\)</p>
- <p>Vår galax diameter: \\(	9,5 \cdot 10^{17} \,\text{km}\\)</p>
- <p>Antalet partiklar i hela universum: \\( \approx 10^{80} \,\text{km}\\)</p>

Hur ska man tolka dessa tal? Om du oavbrutet kunde köra en bil i 120 kilometer per timme tvärsöver Sverige från norr till söder går det åt:

$$ \text{Sträckan} / \text{Hastigheten} = 1574/120 \approx 13,1\,\text{timmar} $$

Till solen skulle det istället ta 1 250 000 timmar, eller runt 143 år! Inte heller finns särskilt många bensinmackar att stanna vid längs vägen.

Även om dessa tal verkligen är stora finns det många tal runtom oss som är mycket större! Om ett schackparti spelas upp till 40 drag har antalet möjliga partier uppskattats till omkring \\(10^{123}\\). Skulle vi försöka oss på att skriva upp alla möjliga partier kommer vi inte ens halvvägs eftersom antalet är mycket mer än \\(10^{80}\\), antalet partiklar i universum. Det finns helt enkelt inte ens tillräckligt med material i universum att tillverka papper för att anteckna alla möjligheter på!

Ändå finns det ingen begränsning, trots att \\(10^{123}\\) är enormt är \\(10^{123}+1\\) större och \\(10^{123}+2\\) är ännu större. Däremot är dessa gigantiska tal inte lika intressanta i sig själva, utan blir istället intressanta när de representerar något särskilt, såsom antalet möjliga schackpartier. Inom teoretisk matematik förekommer faktiskt många större tal än \\(10^{123}\\). Ett berömt sådant är Grahams tal som länge stod med i Guinness rekordbok som “det största tal som någonsin förekommit i ett matematiskt bevis”. Det är så stort att det normala sättet att skriva exponenter såsom \\(1000^{1000^{1000}}\\) inte ens är praktiskt.

På senare år har diverse tal använts inom olika områden som visat sig vara ännu större än Grahams tal. ”Astronomiska tal” är med andra ord rätt små i jämförelse med tal som ibland används i teoretisk matematik. I nästa kapitel ska vi se just vad vi har för nytta av dem.
