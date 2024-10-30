import os
import subprocess
import re

def kablosuz_hiz_testi():
    try:
        # Ping testi
        print("Ping testi yapılıyor...")
        ping_sonucu = subprocess.run(['ping', '-n', '4', '8.8.8.8'], capture_output=True, text=True)
        ping_degerleri = re.findall(r'Zaman=[0-9]+ms', ping_sonucu.stdout)
        if ping_degerleri:
            ping_ortalama = sum([int(re.search(r'[0-9]+', p).group()) for p in ping_degerleri]) / len(ping_degerleri)
            print(f"Ping: {ping_ortalama:.2f} ms")
        else:
            print("Ping sonucu alınamadı.")

        # İndirme hızı testi
        print("İndirme hızı testi yapılıyor...")
        indir_testi = subprocess.run(['curl', '-o', 'nul', '-s', '-w', '%{speed_download}', 'http://ipv4.download.thinkbroadband.com/10MB.zip'], capture_output=True, text=True)
        indir_hizi = float(indir_testi.stdout.strip().replace('"', '')) / 1_000_000  # Byte cinsinden hızı Mbps'e çeviriyoruz
        print(f"İndirme Hızı: {indir_hizi:.2f} Mbps")

        # Yükleme hızı testi
        print("Yükleme hızı testi yapılıyor...")
        yukle_testi = subprocess.run(['curl', '-s', '-w', '%{speed_upload}', '-F', 'file=@10MB.zip', 'https://httpbin.org/post'], capture_output=True, text=True)
        yukleme_hizi = float(yukle_testi.stdout.strip().replace('"', '')) / 1_000_000  # Byte cinsinden hızı Mbps'e çeviriyoruz
        print(f"Yükleme Hızı: {yukleme_hizi:.2f} Mbps")
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Terminali temizler
    kablosuz_hiz_testi()
