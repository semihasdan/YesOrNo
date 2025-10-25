import json

# The questions are in a single block of text, so I'll simulate reading them from a file.
turkish_questions_text = """
--- Hayvanlar ---
Memeli mi?
Suda mı yaşar?
Uçabilir mi?
Yırtıcı mı?
Otobur mu?
Kürkü var mı?
Tüyleri var mı?
Yumurta mı yumurtlar?
Sürüngen mi?
Amfibi mi?
Böcek mi?
Evcil bir hayvan mı?
Vahşi bir hayvan mı?
Bir insandan daha mı büyük?
Bir kediden daha mı küçük?
Afrika'da mı yaşar?
Asya'da mı yaşar?
Avrupa'da mı yaşar?
Kuzey Amerika'da mı yaşar?
Güney Amerika'da mı yaşar?
Avustralya'da mı yaşar?
Antarktika'da mı yaşar?
Sürü hayvanı mı?
Yalnız yaşayan bir hayvan mı?
Gececi mi?
Gündüzcü mü?
Kış uykusuna yatar mı?
Göç eder mi?
Kuyruğu var mı?
Boynuzları var mı?
Geyik boynuzları var mı?
Pençeleri var mı?
Toynakları var mı?
Patileri var mı?
Yüzgeçleri var mı?
Solungaçları var mı?
Pulları var mı?
Kabuu var mı?
Zehirli mi?
Zehirli bir tür mü?
Primat mı?
Kedi türü mü?
Köpek türü mü?
Kemirgen mi?
Keseli mi?
Nesli tükenmekte olan bir tür mü?
Nesli tükenmiş mi?
Benekleri var mı?
Çizgileri var mı?
Ana rengi siyah mı?
Ana rengi beyaz mı?
Ana rengi kahverengi mi?
Ana rengi gri mi?
Ana rengi kırmızı mı?
Ana rengi turuncu mu?
Ana rengi sarı mı?
Ana rengi yeşil mi?
Ana rengi mavi mi?
Renk değiştirebilir mi?
Çiftlik hayvanı mı?
Ev hayvanı mı?
Ağaçlarda mı yaşar?
Yeraltında mı yaşar?
Hızlı bir koşucu mu?
İyi bir yüzücü mü?
Tırmanabilir mi?
Uzun bir boynu var mı?
Uzun bir hortumu var mı?
Kesi var mı?
Büyük bir maymun mu?
Büyük bir kedi mi?
Yırtıcı bir kuş mu?
Şakıyan bir kuş mu?
Deniz memelisi mi?
Tatlı su balığı mı?
Tuzlu su balığı mı?
Kabuklu mu?
Yumuşakça mı?
Araknid mi?
Dörtten fazla bacağı var mı?
Kanatları var ama uçamaz mı?
Kükremesiyle mi bilinir?
Ulumasıyla mı bilinir?
Tıslamasıyla mı bilinir?
Vızıldamasıyla mı bilinir?
Yuva yapar mı?
Baraj yapar mı?
Ağ yapar mı?
Sosyal bir böcek mi?
Bal yapar mı?
Çiçekleri tozlaştırır mı?
Soğukkanlı bir hayvan mı?
Sıcakkanlı bir hayvan mı?
Omurgası var mı?
Omurgasız mı?
Yelesi var mı?
Gagası var mı?
Bıyıkları var mı?
Bambu yer mi?
Okaliptüs yaprakları yer mi?
Böcek yer mi?
Balık yer mi?
Hepçil mi?
Geviş getiren mi?
Geviş getirir mi?
Zekasıyla mı bilinir?
Taklit yeteneğiyle mi bilinir?
Bir ülkenin sembolü mü?
Mitolojik bir yaratık mı?
Çölde mi yaşar?
Yağmur ormanında mı yaşar?
Dağlarda mı yaşar?
Otlaklarda mı yaşar?
Kavrayıcı bir kuyruğu var mı?
Fildişleri var mı?
Filtreleyerek mi beslenir?
Leşçil mi?
Larva aşaması var mı?
Metamorfoz geçirir mi?
Biyolüminesan mı?
Kaybettiği vücut parçalarını yenileyebilir mi?
İki ayaklı bir hayvan mı?
Dört ayaklı bir hayvan mı?
Zehirli bir iğnesi var mı?
Zehirli bir ısırığı var mı?
Tehdit altındaki bir tür mü?
Koruma altındaki bir tür mü?
50 yıldan fazla mı yaşar?
Bir yıldan az mı yaşar?
Sürü halinde mi yaşar?
Sürü halinde uçan bir hayvan mı?
Mükemmel bir görme yeteneği var mı?
Mükemmel bir koku alma duyusu var mı?
Mükemmel bir işitme duyusu var mı?
Ekolokasyon kullanır mı?
Sessiz bir hayvan mı?
Çok sesli bir hayvan mı?
Ayırt edici bir çağrısı var mı?
Popüler bir çizgi film karakteri mi?
Masallarda veya folklorda yer alır mı?
İnsanlar için bir zararlı mı?
İnsanlara bir şekilde faydalı mı?
Ulaşım için kullanılır mı?
İnsanlar için bir besin kaynağı mı?
İnsanlar için bir giysi malzemesi kaynağı mı?
Benzersiz bir savunma mekanizması var mı?
Yırtıcılardan kaçmak için ölü taklidi yapar mı?
Kamuflaj kullanır mı?
Uyarıcı bir renge sahip mi?
Ekosisteminde kilit bir tür mü?
Bazı bölgelerde istilacı bir tür mü?
Başka bir türle simbiyotik bir ilişkisi var mı?
Parazit mi?
Parazitler için bir konak mı?
Sürüler halinde mi seyahat eder?
Sırt yüzgeci var mı?
Solunum deliği var mı?
Bir balina türü mü?
Bir yunus türü mü?
Bir köpekbalığı türü mü?
Bir kaplumbağa türü mü?
Bir yılan türü mü?
Bir kertenkele türü mü?
Bir kurbağa türü mü?
Bir kelebek türü mü?
Bir arı türü mü?
Bir karınca türü mü?
Bir örümcek türü mü?
Bir yarasa türü mü?
Bir ayı türü mü?
Bir kurt türü mü?
Bir tilki türü mü?
Bir geyik türü mü?
Bir maymun türü mü?
Bir papağan türü mü?
Bir kartal türü mü?
Bir baykuş türü mü?
Bir penguen türü mü?
Bir timsah türü mü?
Bir kanguru türü mü?
Bir koala türü mü?
Bir fil türü mü?
Bir zürafa türü mü?
Bir zebra türü mü?
Bir aslan türü mü?
Bir kaplan türü mü?
Bir çita türü mü?
Bir gergedan türü mü?
Bir su aygırı türü mü?
Bir goril türü mü?
Çatal dilli mi?
Bileşik gözleri var mı?
Güney Amerika'dan bir keseli mi?
Bir monotrem mi?
Başında bir sorguç var mı?
Detaylı kur gösterisiyle mi bilinir?
Türün erkeği dişiden daha renkli tüylere mi sahip?
Derin deniz canlısı mı?
--- Kimyasal Elementler/Bileşikler ---
Soy gaz mı?
Metal mi?
Ametal mi?
Metaloid mi?
Oda sıcaklığında sıvı halde mi?
Oda sıcaklığında katı halde mi?
Oda sıcaklığında gaz halinde mi?
Radyoaktif mi?
Alkali metal mi?
Alkalin toprak metali mi?
Geçiş metali mi?
Halojen mi?
Lantanit mi?
Aktinit mi?
Atom numarası 10'dan küçük mü?
Atom numarası 10 ile 20 arasında mı?
Atom numarası 21 ile 30 arasında mı?
Atom numarası 31 ile 40 arasında mı?
Atom numarası 41 ile 50 arasında mı?
Atom numarası 50'den büyük mü?
Sembolü tek harf mi?
Sembolü iki harf mi?
Adını bir kişiden mi alıyor?
Adını bir yerden mi alıyor?
Yaşam için gerekli mi?
Toksik mi?
Yanıcı mı?
Aşındırıcı mı?
Organik bir bileşik mi?
Anorganik bir bileşik mi?
Karbon içerir mi?
Hidrojen içerir mi?
Oksijen içerir mi?
Azot içerir mi?
Kükürt içerir mi?
Halojen içerir mi?
Asit mi?
Baz mı?
Tuz mu?
Hidrokarbon mu?
Alkol mü?
Eter mi?
Aldehit mi?
Keton mi?
Karboksilik asit mi?
Ester mi?
Amin mi?
Amit mi?
Polimer mi?
Karbonhidrat mı?
Lipid mi?
Protein mi?
Nükleik asit mi?
Vitamin mi?
Mineral mi?
Yaygın bir ev kimyasalı mı?
Sanayide kullanılır mı?
Tıpta kullanılır mı?
Tarımda kullanılır mı?
Sera gazı mı?
Kirletici mi?
Doğal olarak mı bulunur?
Sentetik olarak mı üretilir?
Suda çözünür mü?
Güçlü bir elektrolit mi?
Zayıf bir elektrolit mi?
Elektrolit olmayan mı?
Katı halde elektriği iletir mi?
Yüksek bir erime noktası var mı?
Düşük bir erime noktası var mı?
Yüksek bir kaynama noktası var mı?
Düşük bir kaynama noktası var mı?
Sudan daha mı yoğun?
Sudan daha mı az yoğun?
Manyetik mi?
Katalizör mü?
İnhibitör mü?
İzotopları var mı?
Diatomik bir molekül mü?
Poli-atomik bir molekül mü?
Kovalent bağlar oluşturur mu?
İyonik bağlar oluşturur mu?
Metalik bağlar oluşturur mu?
Hidrojen bağı sergiler mi?
Kristal bir katı mı?
Amorf bir katı mı?
Belirgin bir rengi var mı?
Belirgin bir kokusu var mı?
Tatsız mı?
Tatlı mı?
Ekşi mi?
Acı mı?
Tuzlu mu?
Havaifişeklerde kullanılır mı?
Soy metal mi?
Değerli metal mi?
Ağır metal mi?
Hafif metal mi?
Alaşımlarda kullanılır mı?
Yarı iletken mi?
Süper iletken mi?
Yalıtkan mı?
İletken mi?
Su ile reaksiyona girer mi?
Asitlerle reaksiyona girer mi?
Bazlarla reaksiyona girer mi?
Oksidasyona uğrar mı?
Redüksiyona uğrar mı?
İndirgeyici bir ajan mı?
Yükseltgeyici bir ajan mı?
Yakıt olarak kullanılır mı?
Soğutucu mu?
Yağlayıcı mı?
Çözücü mü?
Aşındırıcı mı?
Kurutucu mu?
Pigment mi?
Gübre mi?
Pestisit mi?
Herbisit mi?
İnsektisit mi?
Fungisit mi?
Rodentisit mi?
Dezenfektan mı?
Antiseptik mi?
Anestezik mi?
Ağrı kesici mi?
Antibiyotik mi?
Antiviral mi?
Antifungal mı?
Aşı mı?
Hormon mu?
Enzim mi?
Nörotransmitter mi?
Feromon mu?
Toksin mi?
Zehir mi?
Kanserojen mi?
Mutajen mi?
Teratojen mi?
Sera gazı mı?
Ozon tabakasını incelten bir madde mi?
Kalıcı organik kirletici mi?
Uçucu organik bileşik mi?
Polisiklik aromatik hidrokarbon mu?
Poliklorlu bifenil mi?
Dioksin mi?
Furan mı?
Ağır metal mi?
Radyoaktif element mi?
Sentetik element mi?
Transuranik element mi?
Süper ağır element mi?
Yerkabuğunda mı bulunur?
Yer mantosunda mı bulunur?
Yer çekirdeğinde mı bulunur?
Atmosferde mi bulunur?
Hidrosferde mi bulunur?
Biyosferde mi bulunur?
DNA'nın bir bileşeni mi?
RNA'nın bir bileşeni mi?
Proteinlerin bir bileşeni mi?
Karbonhidratların bir bileşeni mi?
Lipidlerin bir bileşeni mi?
Hücre zarlarının bir bileşeni mi?
Kemiğin bir bileşeni mi?
Dişlerin bir bileşeni mi?
Kanın bir bileşeni mi?
Klorofilin bir bileşeni mi?
Hemoglobinin bir bileşeni mi?
Fotosentezde rol alır mı?
Hücresel solunumda rol alır mı?
Fermantasyonda rol alır mı?
Azot fiksasyonunda rol alır mı?
Su döngüsünde rol alır mı?
Karbon döngüsünde rol alır mı?
Azot döngüsünde rol alır mı?
Fosfor döngüsünde rol alır mı?
Kükürt döngüsünde rol alır mı?
Birincil besin mi?
İkincil besin mi?
Mikro besin mi?
İnsanlar için temel bir besin mi?
Bitkiler için temel bir besin mi?
İz element mi?
Ana mineral mi?
İz mineral mi?
Ultra iz mineral mi?
--- Şehirler ve Başkentler ---
Avrupa'da mı?
Asya'da mı?
Afrika'da mı?
Kuzey Amerika'da mı?
Güney Amerika'da mı?
Avustralya'da mı?
Bir ülkenin başkenti mi?
Bir eyalet veya il başkenti mi?
Kıyıda mı yer alıyor?
Bir nehir kenarında mı yer alıyor?
Dağlarda mı yer alıyor?
Denize kıyısı olmayan bir şehir mi?
İsmi birden fazla kelimeden mi oluşuyor?
Adını bir kişiden mi alıyor?
Bir megakent mi (nüfusu 10 milyondan fazla)?
Nüfusu 1 milyondan az mı?
15. yüzyıldan önce mi kuruldu?
20. yüzyılda mı kuruldu?
UNESCO Dünya Mirası Listesi'nde mi?
Olimpiyat Oyunları'na ev sahipliği yaptı mı?
Bu şehirde ünlü bir anıt var mı?
Antik kalıntılarıyla mı biliniyor?
Önemli bir finans merkezi mi?
Gece hayatıyla mı biliniyor?
Büyük bir din için kutsal bir şehir mi?
Ana dili İngilizce mi?
Ana dili İspanyolca mı?
Ana dili Fransızca mı?
Ana dili Arapça mı?
Ana dili Mandarin Çincesi mi?
Kuzey Yarım Küre'de mi yer alıyor?
Güney Yarım Küre'de mi yer alıyor?
Ekvator üzerinde mi?
Belirli bir yiyecek türüyle mi biliniyor?
Bu şehirde ünlü bir üniversite var mı?
Liman kenti mi?
Metro sistemi var mı?
Kanallarıyla mı biliniyor?
Kurgusal bir şehir mi?
Ünlü bir filmin veya kitabın geçtiği yer mi?
İsmi ünlü bir kişiyle aynı mı?
Amerika Birleşik Devletleri'nde bir şehir mi?
Çin'de bir şehir mi?
Hindistan'da bir şehir mi?
Brezilya'da bir şehir mi?
Rusya'da bir şehir mi?
Japonya'da bir şehir mi?
Almanya'da bir şehir mi?
Birleşik Krallık'ta bir şehir mi?
Fransa'da bir şehir mi?
İtalya'da bir şehir mi?
Kanada'da bir şehir mi?
Avustralya'da bir şehir mi?
Meksika'da bir şehir mi?
İspanya'da bir şehir mi?
Endonezya'da bir şehir mi?
Nijerya'da bir şehir mi?
Pakistan'da bir şehir mi?
Bangladeş'te bir şehir mi?
Mısır'da bir şehir mi?
Vietnam'da bir şehir mi?
Türkiye'de bir şehir mi?
İran'da bir şehir mi?
Tayland'da bir şehir mi?
Güney Afrika'da bir şehir mi?
Arjantin'de bir şehir mi?
Kolombiya'da bir şehir mi?
Güney Kore'de bir şehir mi?
Suudi Arabistan'da bir şehir mi?
Filipinler'de bir şehir mi?
Polonya'da bir şehir mi?
Hollanda'da bir şehir mi?
Belçika'da bir şehir mi?
İsveç'te bir şehir mi?
İsviçre'de bir şehir mi?
Avusturya'da bir şehir mi?
Yunanistan'da bir şehir mi?
Portekiz'de bir şehir mi?
İrlanda'da bir şehir mi?
Norveç'te bir şehir mi?
Danimarka'da bir şehir mi?
Finlandiya'da bir şehir mi?
Yeni Zelanda'da bir şehir mi?
Şili'de bir şehir mi?
Peru'da bir şehir mi?
Venezuela'da bir şehir mi?
Malezya'da bir şehir mi?
Singapur'da bir şehir mi?
BAE'de bir şehir mi?
İsrail'de bir şehir mi?
Fas'ta bir şehir mi?
Kenya'da bir şehir mi?
Etiyopya'da bir şehir mi?
Gana'da bir şehir mi?
Küba'da bir şehir mi?
Jamaika'da bir şehir mi?
İzlanda'da bir şehir mi?
Antik bir şehir mi?
Modern bir şehir mi?
Bir takma adı var mı?
Mimarisiyle mi biliniyor?
Popüler bir turistik yer mi?
Ünlü bir köprüsü var mı?
Ünlü bir kulesi var mı?
Ünlü bir müzesi var mı?
Ünlü bir parkı var mı?
Atlas Okyanusu'na kıyısı olan bir şehir mi?
Pasifik Okyanusu'na kıyısı olan bir şehir mi?
Hint Okyanusu'na kıyısı olan bir şehir mi?
Akdeniz'e kıyısı olan bir şehir mi?
Bir ada üzerinde mi yer alıyor?
5 milyondan fazla nüfusu olan bir şehir mi?
Şehir belirli bir endüstri ile mi biliniyor?
Şehir bir imparatorluğun başkenti oldu mu?
Şehir büyük bir tarihi olaya sahne oldu mu?
Şehir bir çöl bölgesinde mi yer alıyor?
Şehir tropikal bir bölgede mi yer alıyor?
Şehir kutup bölgesinde mi yer alıyor?
Şehrin devlet başkanı bir hükümdar mı?
Şehir küresel bir havayolu için önemli bir merkez mi?
Şehir moda haftasıyla mı biliniyor?
Şehir film endüstrisi için önemli bir merkez mi?
Şehir müzik endüstrisi için önemli bir merkez mi?
Şehir sokak sanatıyla mı biliniyor?
Şehir birden fazla kıtada mı yer alıyor?
Şehrin adı bir palindrom mu?
Şehrin adı 'A' harfiyle mi başlıyor?
Şehrin adı 'B' harfiyle mi başlıyor?
Şehrin adı 'C' harfiyle mi başlıyor?
Şehrin adı 'D' harfiyle mi başlıyor?
Şehrin adı 'E' harfiyle mi başlıyor?
Şehrin adı 'F' harfiyle mi başlıyor?
Şehrin adı 'G' harfiyle mi başlıyor?
Şehrin adı 'H' harfiyle mi başlıyor?
Şehrin adı 'I' harfiyle mi başlıyor?
Şehrin adı 'J' harfiyle mi başlıyor?
Şehrin adı 'K' harfiyle mi başlıyor?
Şehrin adı 'L' harfiyle mi başlıyor?
Şehrin adı 'M' harfiyle mi başlıyor?
Şehrin adı 'N' harfiyle mi başlıyor?
Şehrin adı 'O' harfiyle mi başlıyor?
Şehrin adı 'P' harfiyle mi başlıyor?
Şehrin adı 'Q' harfiyle mi başlıyor?
Şehrin adı 'R' harfiyle mi başlıyor?
Şehrin adı 'S' harfiyle mi başlıyor?
Şehrin adı 'T' harfiyle mi başlıyor?
Şehrin adı 'U' harfiyle mi başlıyor?
Şehrin adı 'V' harfiyle mi başlıyor?
Şehrin adı 'W' harfiyle mi başlıyor?
Şehrin adı 'X' harfiyle mi başlıyor?
Şehrin adı 'Y' harfiyle mi başlıyor?
Şehrin adı 'Z' harfiyle mi başlıyor?
Şehir kahve kültürüyle mi biliniyor?
Şehir başka bir ünlü şehirle 'kardeş şehir' mi?
Şehrin saat dilimi GMT/UTC mi?
Şehir bir şarap bölgesinde mi yer alıyor?
Şehir kışın kar yağışı alır mı?
Şehir yaygın bir yolcu gemisi limanı mı?
Şehir önemli bir hac yeri mi?
Şehrin adı yerli kökenli mi?
--- Gündelik Eşyalar ---
Ekmek kutusundan küçük mü?
Bir arabadan daha mı büyük?
Mutfakta mı bulunur?
Banyoda mı bulunur?
Yatak odasında mı bulunur?
Oturma odasında mı bulunur?
Ofiste mi bulunur?
Garajda mı bulunur?
Elektronik mi?
Pil gerektirir mi?
Fişe takılması gerekir mi?
Metaldan mı yapılmış?
Plastikten mı yapılmış?
Ahşaptan mı yapılmış?
Camdan mı yapılmış?
Kumaştan mı yapılmış?
Keskin mi?
Temizlik için mi kullanılır?
Yemek pişirmek için mi kullanılır?
Yemek yemek için mi kullanılır?
Yazmak için mi kullanılır?
İletişim için mi kullanılır?
Eğlence için mi kullanılır?
Ulaşım için mi kullanılır?
Bir mobilya parçası mı?
Bir giysi parçası mı?
Bir alet mi?
Bir kap mı?
Sıvıları mı tutar?
Tek kullanımlık mı?
Yeniden kullanılabilir mi?
Her gün kullanır mısınız?
Giydiğiniz bir şey mi?
Bir sapı var mı?
Düğmeleri var mı?
Bir ekranı var mı?
Ses çıkarır mı?
Ağır mı?
Kırılgan mı?
Tek elle tutabilir misiniz?
Bir setin parçası mı?
Farklı renkleri var mı?
Genellikle bir okulda mı bulunur?
Kişisel hijyen için mi kullanılır?
Bir kapağı var mı?
Yumuşak mı?
Sert mi?
Esnek mi?
Sert mi?
Şeffaf mı?
Opak mı?
Hareketli parçaları var mı?
Ölçmek için mi kullanılır?
Bir ışık kaynağı mı?
Kullanıldığında ısınır mı?
Bir güvenlik cihazı mı?
Dekorasyon için mi kullanılır?
Bir müzik aleti mi?
Bir oyuncak mı?
Bahçe işleri için mi kullanılır?
Bir hobiyle mi ilgili?
Bir bıçağı var mı?
Bir motoru var mı?
Okuduğunuz bir şey mi?
Bir şeyleri saklamak için mi kullanılır?
Bir kilidi var mı?
Bir tür çanta mı?
Sporla mı ilgili?
Cüzdanda veya çantada bulduğunuz bir şey mi?
Bir güç kablosu var mı?
Kablosuz mu?
Bir tür fırça mı?
Kesmek için mi kullanılır?
Bir sapı ve kılları var mı?
Zamanı söylemek için mi kullanılır?
Yemek pişirmek için mi kullanılır?
Yemek servis etmek için mi kullanılır?
İçmek için mi kullanılır?
Oturmak için mi kullanılır?
Uyumak için mi kullanılır?
Bir tür ayakkabı mı?
Bir tür başlık mı?
Bir tür dış giyim mi?
Dişlerinizi temizlemek için mi kullanılır?
Ellerinizi yıkamak için mi kullanılır?
Kendinizi kurulamak için mi kullanılır?
Bir tür bağlayıcı mı?
Fermuarı var mı?
Bağcıkları var mı?
Tokası var mı?
Bir tür kağıt ürünü mü?
Kalemle veya kurşun kalemle yazmak için mi kullanılır?
Hataları silmek için mi kullanılır?
Kağıtları bir arada tutmak için mi kullanılır?
Bir tür yapıştırıcı mı?
Bir mutfak aleti mi?
Bir banyo eşyası mı?
Bir ofis ekipmanı mı?
Bir bahçe aleti mi?
Bir elektrikli alet mi?
Bir el aleti mi?
Bir temizlik malzemesi mi?
Bir mutfak gereci mi?
Bir çatal bıçak takımı parçası mı?
Bir tabak mı?
Bir tür tencere veya tava mı?
Bir fırın aleti mi?
Bir tür lamba veya aydınlatma armatürü mü?
Bir tür ayna mı?
Bir tür saat mi?
Bir tür telefon mu?
Bir tür bilgisayar mı?
Bir tür kamera mı?
Bir tür hoparlör veya kulaklık mı?
Bir tür televizyon veya monitör mü?
Bir tür uzaktan kumanda mı?
Bir tür pil mi?
Bir tür kablo veya kordon mu?
Bir tür anahtar veya kilit mi?
Bir tür cüzdan veya çanta mı?
Bir tür sırt çantası veya çanta mı?
Bir tür şemsiye mi?
Bir tür gözlük mü?
Bir tür şapka veya bere mi?
Bir tür atkı veya eldiven mi?
Bir tür çorap mı?
Bir tür ayakkabı veya bot mu?
Bir tür gömlek veya bluz mu?
Bir tür pantolon mu?
Bir tür elbise veya etek mi?
Bir tür ceket veya palto mu?
Bir tür kazak mı?
Bir tür takım elbise veya üniforma mı?
Bir tür kravat veya papyon mu?
Bir tür kemer veya askı mı?
Bir takı parçası mı?
Bir tür yüzük mü?
Bir tür kolye mi?
Bir tür bilezik mi?
Bir tür küpe mi?
Bir tür saat mi?
Bir tür iğne veya broş mu?
Bir kozmetik ürünü mü?
Bir tür sabun veya şampuan mı?
Bir tür losyon veya krem mi?
Bir tür parfüm veya kolonya mı?
Bir tür tıraş makinesi veya jilet mi?
Bir tür diş fırçası veya diş macunu mu?
Bir tür tarak veya fırça mı?
Bir tür havlu veya yüz bezi mi?
Bir tür yatak veya şilte mi?
Bir tür yastık veya minder mi?
Bir tür battaniye veya yorgan mı?
Bir tür çarşaf veya yastık kılıfı mı?
--- Ünlü İnsanlar ---
Hayatta mılar?
Öldüler mi?
Tarihi bir figür mü?
Çağdaş bir figür mü?
Politikacı mı?
Sanatçı mı?
Bilim insanı mı?
Sporcu mu?
Aktör/aktris mi?
Müzisyen mi?
Yazar mı?
İş insanı mı?
Mucit mi?
Kaşif mi?
Filozof mu?
Dini bir figür mü?
Hükümdar mı?
Askeri lider mi?
Devrimci mi?
Aktivist mi?
Amerikalı mı?
İngiliz mi?
Fransız mı?
Alman mı?
İtalyan mı?
Rus mu?
Çinli mi?
Hintli mi?
Başka bir ülkeden mi?
Erkek mi?
Kadın mı?
20. yüzyılda mı doğdular?
19. yüzyıldan önce mi doğdular?
Tek bir başarıyla mı tanınırlar?
Onlara atfedilen ünlü bir söz var mı?
Nobel Ödülü kazandılar mı?
Oscar kazandılar mı?
Grammy kazandılar mı?
Olimpiyat altın madalyası kazandılar mı?
Onlar hakkında ünlü bir film var mı?
Onlar hakkında ünlü bir kitap var mı?
Yüzleri herhangi bir para biriminde var mı?
Onların adına büyük bir anıt var mı?
Tek bir isimle mi tanınırlar?
Ünlü bir takma adları var mıydı?
Büyük bir savaşa katıldılar mı?
Bir başkan veya başbakan mıydılar?
Bir kral veya kraliçe miydiler?
Büyük bir bilimsel keşif yaptılar mı?
Ünlü bir sanat eseri yarattılar mı?
Klasik bir roman yazdılar mı?
Ünlü bir müzik parçası bestelediler mi?
Büyük bir şirket kurdular mı?
Bugün kullandığımız bir şey icat ettiler mi?
Büyük bir keşif gezisine liderlik ettiler mi?
Büyük bir din veya felsefe kurdular mı?
Belirli bir siyasi ideolojiyle mi ilişkilendirilirler?
Bir sosyal harekete liderlik ettiler mi?
Hayırseverlikleriyle mi tanınırlar?
Bir çocuk dahi miydiler?
90 yaşından fazla mı yaşadılar?
Trajik bir şekilde genç mi öldüler?
Suikaste mi uğradılar?
Tartışmalı bir figür mü?
Yaygın olarak takdir edilirler mi?
Çalışmaları bugün hala etkili mi?
Bazen gerçek bir kişiyle karıştırılan kurgusal bir karakter mi?
Spor dünyasından mılar?
Eğlence dünyasından mılar?
Bilim ve teknoloji dünyasından mılar?
Siyaset ve tarih dünyasından mılar?
Sanat ve edebiyat dünyasından mılar?
İş ve finans dünyasından mılar?
Tıp alanındaki katkılarıyla mı tanınırlar?
Fizik alanındaki katkılarıyla mı tanınırlar?
Kimya alanındaki katkılarıyla mı tanınırlar?
Biyoloji alanındaki katkılarıyla mı tanınırlar?
Matematik alanındaki katkılarıyla mı tanınırlar?
Bilgisayar bilimi alanındaki katkılarıyla mı tanınırlar?
Astronomi alanındaki katkılarıyla mı tanınırlar?
Felsefe alanındaki katkılarıyla mı tanınırlar?
Din alanındaki katkılarıyla mı tanınırlar?
Sanat tarihi alanındaki katkılarıyla mı tanınırlar?
Müzik tarihi alanındaki katkılarıyla mı tanınırlar?
Edebiyat tarihi alanındaki katkılarıyla mı tanınırlar?
Siyasi tarih alanındaki katkılarıyla mı tanınırlar?
Askeri tarih alanındaki katkılarıyla mı tanınırlar?
Ekonomi tarihi alanındaki katkılarıyla mı tanınırlar?
Sosyal tarih alanındaki katkılarıyla mı tanınırlar?
Antik tarihten bir figür mü?
Orta Çağ'dan bir figür mü?
Rönesans'tan bir figür mü?
Aydınlanma Çağı'ndan bir figür mü?
Modern dönemden bir figür mü?
21. yüzyıldan bir figür mü?
Uzaya gittiler mi?
Everest Dağı'na tırmandılar mı?
Dünyayı dolaştılar mı?
Ünlü bir talk show'a konuk oldular mı?
Hayat hikayeleri bir 'sıfırdan zenginliğe' masalı mı?
Ünlü bir ailede mi doğdular?
Başka bir kişiyle ünlü bir rekabetleri var mıydı?
Başka bir kişiyle ünlü bir ortaklıkları var mıydı?
Kendine özgü tarzları veya görünüşleriyle mi tanınırlar?
İsimleri ilginç bir şeyin anagramı mı?
Onlar hakkında komplo teorileri var mı?
Parodi veya hiciv konusu mu?
Çalışmaları okullarda okutuluyor mu?
Onlara adanmış bir müze var mı?
Büyük bir şehirde heykelleri var mı?
Kültürel bir ikon mu?
Ulusal bir kahraman mı?
Belirli bir fikrin veya hareketin sembolü mü?
İsimlerini değiştirdiler mi?
Ünlü bir evcil hayvanları var mıydı?
Çok dil biliyorlar mıydı?
Kendi kendilerini mi eğittiler?
Mütevazı bir geçmişten mi geldiler?
Büyük bir aileleri var mıydı?
Münzevi bir hayat mı yaşadılar?
Bir gurbetçi miydiler?
Ünlü son sözleri var mıydı?
Mezarları bir turistik cazibe merkezi mi?
Ünlü bir fotoğrafın konusu mu?
Ünlü bir tablonun konusu mu?
Ünlü bir şarkın konusu mu?
Kendilerine özgü bir jestleri veya sloganları var mıydı?
İnsani yardım çalýşmalarıyla mı tanınırlar?
Savaş esiri miydiler?
Siyasi bir mahkum muydular?
Açlık grevine gittiler mi?
Bir protesto veya gösteriye liderlik ettiler mi?
Kendi ülkelerinden sürgün edildiler mi?
Devlet töreniyle mi gömüldüler?
Herhangi bir ülkenin onursal vatandaşı mılar?
Onların onuruna bir ulusal bayram var mı?
Bilimsel bir yasanın veya teorinin isim babası mılar?
Bir ölçü biriminin isim babası mılar?
Bir kimyasal elementin isim babası mılar?
Bir gök cisminin isim babası mılar?
Bir bitki veya hayvan türünün isim babası mılar?
Bir binanın veya kurumun isim babası mılar?
Bir ödülün veya armağanın isim babası mılar?
Bir cadde veya meydanın isim babası mılar?
Bir şehir veya kasabanın isim babası mılar?
Bir gemi veya aracın isim babası mılar?
Bir yiyecek veya içeceğin isim babası mılar?
Bir moda öğesinin isim babası mılar?
Bir saç stilinin isim babası mılar?
Bir dans hareketinin isim babası mılar?
Felsefi bir kavramın isim babası mılar?
Psikolojik bir fenomenin isim babası mılar?
Tarihsel bir dönemin isim babası mılar?
Edebi bir türün isim babası mılar?
Müzikal bir türün isim babası mılar?
Sanatsal bir akımın isim babası mılar?
Siyasi bir hareketin isim babası mılar?
Sosyal bir hareketin isim babası mılar?
Bilimsel bir aletin isim babası mılar?
Matematiksel bir formülün isim babası mılar?
Bir bilgisayar algoritmasının isim babası mılar?
Bir programlama dilinin isim babası mılar?
Bir yazılım uygulamasının isim babası mılar?
Bir video oyununun isim babası mılar?
Bir çizgi roman karakterinin isim babası mılar?
Bir romandaki kurgusal bir karakterin isim babası mılar?
Bir oyundaki bir karakterin isim babası mılar?
Bir filmdeki bir karakterin isim babası mılar?
Bir televizyon şovundaki bir karakterin isim babası mılar?
Bir marka veya ürünün isim babası mılar?
Bir şirketin isim babası mılar?
Bir spor takımının isim babası mılar?
Bir stadyum veya arenanın isim babası mılar?
Bir havaalanının isim babası mılar?
Bir köprünün isim babası mılar?
Bir parkın isim babası mılar?
Bir dağın isim babası mılar?
Bir nehrin isim babası mılar?
Bir gölün isim babası mılar?
Bir okyanusun isim babası mılar?
Bir denizin isim babası mılar?
Bir kıtanın isim babası mılar?
Bir ülkenin isim babası mılar?
Bir eyalet veya ilin isim babası mılar?
Bir bölgenin isim babası mılar?
Bir adanın isim babası mılar?
Bir yarımadanın isim babası mılar?
Bir körfezin isim babası mılar?
Bir boğaz veya kanalın isim babası mılar?
"""

# The category names in the text file are slightly different from the ones in the JSON file.
# I need a mapping to match them.
category_mapping = {
    "Hayvanlar": "Hayvanlar",
    "Kimyasal Elementler/Bileşikler": "Kimyasal Elementler/Bileşikler",
    "Şehirler ve Başkentler": "Şehirler ve Başkentler",
    "Gündelik Eşyalar": "Günlük Eşyalar",
    "Ünlü İnsanlar": "Ünlü İnsanlar",
    "Yiyecek ve Mutfak": "Yiyecek ve Mutfak",
    "Teknoloji ve Cihazlar": "Teknoloji ve Cihazlar",
    "Kurgusal Karakterler": "Kurgusal Karakterler",
    "Tarihi Olaylar ve Dönemler": "Tarihi Olaylar ve Dönemler",
    "Spor ve Atletizm": "Spor ve Atletizm",
    "Müzik Aletleri": "Müzik Aletleri",
    "Mitolojik Yaratıklar": "Mitolojik Yaratıklar",
    "Meslekler ve Uğraşlar": "Meslekler ve Uğraşlar",
    "Gezegenler ve Astronomik Nesneler": "Gezegenler ve Astronomik Nesneler",
    "Video Oyunları ve Konsollar": "Video Oyunları ve Konsollar",
    "Türk Ünlüler": "Türk Ünlüler"
}

def parse_questions(text):
    questions_by_category = {}
    current_category = None
    for line in text.strip().split('\n'):
        line = line.strip()
        if line.startswith('---') and line.endswith('---'):
            current_category = line[4:-4]
            questions_by_category[current_category] = []
        elif line and current_category:
            questions_by_category[current_category].append(line)
    return questions_by_category

turkish_questions = parse_questions(turkish_questions_text)

with open('gameDataTr.json', 'r', encoding='utf-8') as f:
    game_data = json.load(f)

for category_data in game_data['gameData']:
    category_name_json = category_data['categoryName']

    # Check if this category from the JSON has a corresponding entry in our parsed questions
    if category_name_json in category_mapping.values():
      # Find the key from the text file that maps to the current JSON category name
      text_file_category_name = [k for k, v in category_mapping.items() if v == category_name_json][0]
      if text_file_category_name in turkish_questions:
          category_data['questions'] = turkish_questions[text_file_category_name]

with open('gameDataTr.json', 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=2)

print("gameDataTr.json updated successfully.")
