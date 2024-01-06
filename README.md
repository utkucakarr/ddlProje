pip install -r requirements.txt

# Tiktok İstenilen Hashtag Göre Veri Çekme Ve Temizleme İşlemi
<br/>

Tiktoktan aralıtan hastaga göre video başlıklarını çeker ve başlıklarda temizleme işlemi yapar.
<br/>
## Kullanılan Kütüphaneler
-tiktokapipy<br/>

# VERİ SETİ'NİN OLUŞTURULMASI
Tiktok verilerinin çekilmesi için tiktokapipy kütüphanesi kullanıldı. Örnek olarak yapılan uygulamada Hastag = yeni yıl olduğu için yeni yıl ile ilgili videoları çekti ve bu veoların başlıklarını aldı.
Video limit kısmında kaç tane video çekmesini belirtiyoruz bu uygulamada 15 yazdığımız için 15 tane video geliyor bu sayıyı arttırırsak o kadar video ve başlık alıcaktır.

# Tweetlerin Temizlenmesi ve Lemmatization İşlemi<br/>
Veriseti oluşturulduktan sonra modelin daha iyi çalışması ve başarı oranının daha yüksek olması için başlıkların temizlenmesi gerekmektedir. Başlıkların içerisinde emojiler, noktalama işaretleri, stopwordsler, linkler gibi istenmeyen ve modelin başarısını düşürecek veriler başlıklar içerisinden temizleniyor. Daha sonra lemmatization (kelimelerin köklerinin alınması) işlemi yapılarak temiz ve kelimelerin köklerinden oluşan başlıklar elde ediliyor.
<br/>

# Oluşturulan Tiktok Verileri
tiktok_videos.json dosyası içinde listelenmiştir.

# Oluşturulan Temiz Tiktok Verileri
Clean_tiktok_videos.json dosyası içinde listelenmiştir.
