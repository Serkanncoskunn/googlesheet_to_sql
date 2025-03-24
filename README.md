# googlesheet_to_sql
Google Sheets'ten SQL'e Veri Aktarımı
Google Sheets'ten SQL'e Veri Aktarımı
1 . Adım Google Sheet API etkinleştirmek : 
Google Sheet verilerine hesabınızdan erişim sağlamak için.
https://console.cloud.google.com sayfasından.
API’s Services Kısmına gelerek Google Sheets API yi etkinleştirin.
2. Adım Key Account Oluşturmak :
Hesabınıza python aracılığıyla bağlantı kurmak için key account oluşturmalıyız.
https://console.cloud.google.com > APIs Services > Credentials > Create Credentials > Service Account
Açılan sayfada servis isimi belirtildekten sonra oluşturulur.
https://console.cloud.google.com/ > APIs Services > Credentials Sayfasında oluşturuduğumuz servis hesabının sağ 
tarafında bulunan düzenleme butonuna tıklayalım.
Add key ile json formatında anahtarımızı masaüstüne indirelim(hybrid Skill) adında bir dosya inecektir.
Şimdiye kadar yapmış olduğumuz işlemler Google hesabımız ile haberleşmemizi ve google sheet e köprü oluşturmamızı 
sağlayacaktır.
3. Google Sheet Oluşturmak ve Ayarlamak:
Örnek bir google sheet sayfası oluşturalım . (Tarafımca hazırlanmış market satış datası)
Oluşturulan bu sayfanın paylaş özelliğinde bağlantıya sahip olan herkes olarak seçilmesi gerekmektedir. Bu sayede 
sayfanın sahibi olmasak bile bağlantı url si sayesinde içerisindeki datayı aktarabiliriz.
4. Python Kodu ile Aktarım Sağlamak :
Şimdi Yapay zekadan yardım alarak python kodları hazırlayalım. 
İstediğimiz kod tarzı: Google Sheet URL si ile içerisindeki datayı SQL e belirtilen database içerisinde İlgili tabloya veriyi 
eklemesidir.
Bu sheet içerisindeki kolon başlıklarını otomatik çeksin ve eğer boşluk varsa “ _ “ ekleyerek düzenlesin.
Sheet içerisine yeni bir kolon eklenmesi gibi durumlarda SQL içerisindeki tabloyu delete insert yaparak güncellesin.
Arayüz için Girdiğimiz Bilgileri Hatırla butonu sayesinde tekrar girmemize gerek kalmadan bilgiler otomatik olarak 
gelecektir.
Gerekli Bilgiler : 
Sql Connection Bilgileri (Server Adı, Kullanıcı Adı, Şifre , Veritabanı Adı)
Google Cloud Json Dosya Uzantısı
Google Sheet URL
Python Arayüz kodu : Bu kod ile karşımıza gelecek arayüz içerisine yazacağımız bilgiler ile çalışıp aktarım hakkında bilgiler 
verecektir.
İşleri biraz daha güzelleştirelim .
Python ile yazdığımız arayüz kodundan bir exe oluşturup bu işlemleri python açmamıza gerek kalmadan masaüstünden 
yönetelim.
Bunun için yapmamız gerekenler 
Microsoft Store ya da https://www.python.org/downloads/ sitesinden python ı bilgisayarımıza kuralım .
CMD komut dizini açarak bu 3 kütüphaneyi indirelim
Daha sonra python kodumuzun bulunduğu klasörü yolunu başında cd olacak şekilde ekleyelim.
ve son olarak bu kodu ekleyelim
işlemler tamamlandıktan sonra python kodunun bulunduğu klasörde dist adında bir klasör eklenecektir buranında 
içerisine girerek exe dosyamızı bulabiliriz.
