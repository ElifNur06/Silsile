import os
import random
from codec import DNACodec

def simulate_10000_years(dna_seq):
    """DNA'yı 10.000 yıl boyunca buzul altında yaşlandırır."""
    aged_dna = []
    
    for base in dna_seq:
        # 1. DEAMİNASYON: Antik DNA'da en sık görülen hasar. C'ler zamanla T'ye dönüşür.
        if base == 'C' and random.random() < 0.15: 
            aged_dna.append('T')
            
        # 2. DEPÜRİNASYON: Harf tamamen kopar ve sarmal kısalır (%8 oranında)
        elif random.random() < 0.08:
            continue 
            
        # 3. YABANCI MADDE (KONTAMİNASYON): Araya topraktan yabancı baz karışır
        elif random.random() < 0.03:
            aged_dna.append(base)
            aged_dna.append(random.choice(['A', 'T', 'C', 'G']))
            
        # Sağlam kalanlar
        else:
            aged_dna.append(base)
            
    return "".join(aged_dna)

def run_bio_time_machine():
    print("--- 🕰️ BİYO-ZAMAN MAKİNESİ: 10.000 YILLIK ANTİK DNA TESTİ ---")
    
    codec = DNACodec()
    # 1 KB'lık önemli bir dijital miras
    ancient_data = os.urandom(1024) 
    PASSWORD = "MİRAS_2026"
    
    print("\n📦 Dijital Miras paketleniyor, şifreleniyor ve DNA'ya dönüştürülüyor...")
    fresh_dna = codec.encode(ancient_data, password=PASSWORD)
    print(f"📏 Taze DNA Uzunluğu: {len(fresh_dna)} baz")
    
    print("\n🧊 DNA bir tüpe konuldu ve buzulların derinliklerine gömüldü...")
    print("⏳ Zaman hızla akıyor: 1.000 yıl... 5.000 yıl... 10.000 Yıl!")
    
    aged_dna = simulate_10000_years(fresh_dna)
    print(f"📏 Çürümüş Antik DNA Uzunluğu: {len(aged_dna)} baz (Deaminasyon ve Çürüme tespit edildi)")
    
    print("\n[GELECEKTEKİ ARKEOLOJİ LABORATUVARINDA DİRİLTME İŞLEMİ]")
    try:
        # Arkeologlar doğru şifreyle o çürümüş enkazı tarıyor
        recovered = codec.decode(aged_dna, password=PASSWORD)
        recovered = recovered[:len(ancient_data)]
        
        if recovered == ancient_data:
            print("\n🌟 MUCİZE GERÇEKLEŞTİ! 10.000 yıllık kimyasal çürümeye, C->T kaymalarına ve silinmelere rağmen veri %100 doğrulukla diriltildi!")
            print("Sistemin 'Tanrısal Mimarisi' resmen ölümsüzlüğü kanıtladı.")
        else:
            print("\n❌ HATA: Zaman, Reed-Solomon zırhını mağlup etti.")
            
    except Exception as e:
        print(f"\n🚨 Kritik Çökme: {e}")

if __name__ == "__main__":
    run_bio_time_machine()