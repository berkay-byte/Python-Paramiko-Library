Tabii ki, GitHub'da daha temiz görünmesi için hem Türkçe hem de İngilizce bölümlerini tamamen birbirinden ayırdım. Bu metni doğrudan kopyalayıp README.md dosyana yapıştırabilirsin.
🛡️ Paramiko SSH Command Executor

English | Türkçe
English

This project is a Python-based interactive SSH terminal client that allows you to execute commands on a remote server using the Paramiko library.
🚀 Features

    Interactive Shell: Execute multiple commands in a loop until you type 'quit'.

    Safe Credentials: Asks for username and password at runtime instead of hardcoding them.

    Error Handling: Catches connection errors and authentication failures using try-except blocks.

    Connection Management: Ensures the SSH connection is closed properly after the execution is finished.

🛠️ Requirements

You need to have Python and the Paramiko library installed:
Bash

pip install paramiko

📖 Usage

    Open paramiko1.py and set the ip variable to your target's IP address (Default: 192.168.1.101).

    Run the script:
    Bash

    python3 paramiko1.py

    Enter your SSH credentials when prompted.

    Type any Linux command. Type quit to exit.

Türkçe

Bu proje, Paramiko kütüphanesini kullanarak uzak bir sunucuda komut çalıştırmanızı sağlayan Python tabanlı bir interaktif SSH terminal istemcisidir.
🚀 Özellikler

    İnteraktif Terminal: 'quit' yazana kadar döngü içinde birden fazla komut çalıştırın.

    Güvenli Giriş: Kullanıcı adı ve şifreyi kodun içine yazmak yerine çalışma anında sorar.

    Hata Yönetimi: Bağlantı hatalarını ve kimlik doğrulama sorunlarını try-except blokları ile yakalar.

    Bağlantı Yönetimi: İşlem bittiğinde SSH bağlantısının düzgün bir şekilde kapatılmasını sağlar.

🛠️ Gereksinimler

Sisteminizde Python ve Paramiko kütüphanesinin kurulu olması gerekir:
Bash

pip install paramiko

📖 Kullanım

    paramiko1.py dosyasını açın ve ip değişkenini hedefinizin IP'si ile değiştirin (Varsayılan: 192.168.1.101).

    Script'i çalıştırın:
    Bash

python3 paramiko1.py

Sorulduğunda SSH kullanıcı bilgilerinizi girin.

Herhangi bir Linux komutu yazın. Çıkmak için quit yazın.
