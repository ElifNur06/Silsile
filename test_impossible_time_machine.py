import os
import hashlib
from codec import DNACodec
from time_machine import BioTimeMachine

def run_impossible_time_machine():
    print("--- ☢️ İMKANSIZ BİYO-ZAMAN: KOZMİK KIYAMET TESTİ ---")
    
    codec = DNACodec()
    tm = BioTimeMachine()
    PASSWORD = "OMEGA_PROTOCOL_ABSOLUTE_ZERO"
    
    # 50 KB'lık veri (Hata düzeltme ile ~100MB DNA verisi oluşturacak)
    print("\n📦 Kritik Veri Paketi (50 KB) şifreleniyor...")
    data = os.urandom(50 * 1024)
    dna = codec.encode(data, password=PASSWORD)
    
    # Maliyet Analizi
    costs = tm.calculate_synthesis_cost(len(dna))
    print(f"💰 Sentezleme Maliyeti: ${costs['grand_total']:,.2f}")
    
    # Kıyıcı Simülasyon
    print("\n☄️ [KIYAMET SENARYOSU] 10.000 yıl: Buzul Çağı + Kozmik Isınma + Radyasyon...")
    
    # 1. Aşama: 5.000 yıl -20°C
    dna, _ = tm.simulate_aging(dna, 5000, -20.0)
    # 2. Aşama: 100 yıl +45°C (Termal Şok/Erime)
    dna, _ = tm.simulate_aging(dna, 100, 45.0)
    # 3. Aşama: Kalan yıllar radyasyon altında
    dna, stats = tm.simulate_aging(dna, 4900, 10.0)
    
    print(f"🧬 İskelet Kırılması (Total Frame-Shift): {stats['cleavage']:,}")
    
    print("\n⚕️ LABORATUVAR: Kuantum Hata Düzeltme başlatıldı...")
    try:
        recovered = codec.decode(dna, password=PASSWORD)
        recovered = recovered[:len(data)]
        
        if hashlib.sha256(recovered).hexdigest() == hashlib.sha256(data).hexdigest():
            print("\n👑 MİMARİ ZAFER: Kozmik radyasyona ve termal erimeye rağmen 50 KB veri, 10.000 yıl sonra %100 kurtarıldı!")
        else:
            print("\n❌ SİSTEM ÇÖKTÜ: 10.000 yıllık kozmik yıkım, Reed-Solomon zırhını eritti.")
            
    except Exception as e:
        print(f"\n💀 KRİTİK HATA: İnsanlık tarihinin verisi silindi: {e}")

if __name__ == "__main__":
    run_impossible_time_machine()