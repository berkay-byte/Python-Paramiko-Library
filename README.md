🛡️ Paramiko SSH Command Executor

This project is a Python-based interactive SSH terminal client that allows you to execute commands on a remote server (like Metasploitable) using the Paramiko library.

Bu proje, Paramiko kütüphanesini kullanarak uzak bir sunucuda (Metasploitable gibi) komut çalıştırmanızı sağlayan Python tabanlı bir interaktif SSH terminal istemcisidir.
🚀 Features / Özellikler

    Interactive Shell: Execute multiple commands in a loop until you type 'quit'.

    Safe Credentials: Asks for username and password at runtime instead of hardcoding them.

    Error Handling: Catches connection errors and authentication failures.

    Output Decoding: Automatically decodes byte outputs from the server to readable text.

    İnteraktif Terminal: 'quit' yazana kadar döngü içinde birden fazla komut çalıştırın.

    Güvenli Giriş: Kullanıcı adı ve şifreyi kodun içine yazmak yerine çalışma anında sorar.

    Hata Yönetimi: Bağlantı hatalarını ve kimlik doğrulama sorunlarını yakalar.

    Çıktı Çözümleme: Sunucudan gelen byte verilerini okunabilir metne dönüştürür.

🛠️ Requirements / Gereksinimler

You need to have Python and the Paramiko library installed. Python ve Paramiko kütüphanesinin kurulu olması gerekir.
Bash

pip install paramiko

📖 Usage / Kullanım

    Set the Target IP: Open paramiko1.py and change the ip variable to your target's IP address (Default is 192.168.1.101). Hedef IP'yi Ayarlayın: paramiko1.py dosyasını açın ve ip değişkenini hedefinizin IP'si ile değiştirin.

    Run the Script: Script'i Çalıştırın:
    Bash

    python3 paramiko1.py

    Login: Enter your SSH credentials when prompted. Giriş: Sorulduğunda SSH kimlik bilgilerinizi girin.

    Execute: Type any Linux command. Type quit to exit. Çalıştır: Herhangi bir Linux komutu yazın. Çıkmak için quit yazın.

📝 Code Overview / Kod Hakkında Notlar
Part / Bölüm	Description / Açıklama
AutoAddPolicy()	Automatically adds the server's host key to the 'known_hosts'. / Sunucu anahtarını otomatik olarak 'known_hosts' listesine ekler.
exec_command()	Sends the command to the remote server. / Komutu uzak sunucuya gönderir.
decode()	Converts server output from bytes to string. / Sunucu çıktısını byte formatından metne çevirir.
⚖️ License / Lisans

This project is for educational purposes (Cybersecurity testing). Use it responsibly. Bu proje eğitim amaçlıdır (Siber güvenlik testleri). Lütfen sorumlu bir şekilde kullanın.
