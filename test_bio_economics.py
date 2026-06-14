import os
import hashlib
from codec import DNACodec
from time_machine import BioTimeMachine

def run_bio_economics_test():
    print("--- Ω BİYO-ZAMAN MAKİNESİ VE EKONOMİK SİMÜLATÖR ---")
    
    codec = DNACodec()
    time_machine = BioTimeMachine()
    PASSWORD = "NEON_GENESIS_2026"
    
    # 5 KB'lık dijital bir miras dosyası
    print("\n[codebygunes] 📦 Dijital Miras (5 KB) oluşturuluyor...")
    digital_legacy = os.urandom(5120) 
    original_hash = hashlib.sha256(digital_legacy).hexdigest()
    
    print("🧬 Veri DNA'ya dönüştürülüyor (Yedeklilik ve Zırh Ekleniyor)...")
    dna_sequence = codec.encode(digital_legacy, password=PASSWORD)
    seq_length = len(dna_sequence)
    
    print(f"📏 Nihai DNA Sarmalı Uzunluğu: {seq_length:,} baz")
    
    # --- 1. MALİYET HESAPLAMASI ---
    print("\n💰 [TWIST BIOSCIENCE API SİMÜLASYONU] Maliyet Çıkarılıyor...")
    costs = time_machine.calculate_synthesis_cost(seq_length)
    
    print(f"  • Baz Başına Maliyet: ${costs['cost_per_base']:.2f}")
    print(f"  • Sentezleme (Yazma): ${costs['synthesis_total']:,.2f}")
    print(f"  • Havuz/Hazırlık Ücreti: ${costs['setup_fee']:,.2f}")
    print(f"  • Sekanslama (Okuma) Garantisi: ${costs['sequencing_fee']:,.2f}")
    print(f"  => TOPLAM LABORATUVAR FATURASI: ${costs['grand_total']:,.2f}")
    
    if costs['grand_total'] > 100000:
        print("  ⚠️ Uyarı: Ticari sentez için oldukça yüksek bir bütçe. Veri sıkıştırma algoritmaları önerilir.")

    # --- 2. ZAMAN MAKİNESİ (ÇEVRE SİMÜLASYONU) ---
    target_years = 10_000
    temperature = -20.0 # Permafrost (Buzul altı)
    
    print(f"\n❄️ [ÇEVRE SİMÜLATÖRÜ AKTİF] DNA sarmalı {temperature}°C buzul altına gömüldü.")
    print(f"⏳ Zaman hızla ileri sarılıyor: {target_years:,} Yıl...")
    
    aged_dna, damage_stats = time_machine.simulate_aging(
        dna_seq=dna_sequence, 
        years=target_years, 
        temperature_c=temperature
    )
    
    print("\n🔬 [10.000 YIL SONRA] Arkeolojik DNA Analiz Raporu:")
    print(f"  • Orijinal Uzunluk: {seq_length:,} baz")
    print(f"  • Mevcut Uzunluk: {len(aged_dna):,} baz")
    print(f"  • C->T Kayması (Deaminasyon): {damage_stats['deamination']:,} adet")
    print(f"  • Baz Kaybı (Depürinasyon): {damage_stats['depurination']:,} adet")
    print(f"  • İskelet Kırılması (Frame-Shift): {damage_stats['cleavage']:,} adet")
    
    # --- 3. DİRİLTME İŞLEMİ ---
    print("\n⚕️ Laboratuvar kurtarma protokolü (BLAST & Reed-Solomon) başlatılıyor...")
    
    try:
        recovered_data = codec.decode(aged_dna, password=PASSWORD)
        recovered_data = recovered_data[:len(digital_legacy)] # Padding temizliği
        
        if hashlib.sha256(recovered_data).hexdigest() == original_hash:
            print("\n👑 MUCİZE GERÇEKLEŞTİ: Sistem, -20°C'de 10.000 yıllık kimyasal çürümeye ve binlerce mutasyona rağmen veriyi %100 kusursuz diriltti!")
        else:
            print("\n❌ SİSTEM ÇÖKTÜ: DNA çok ağır hasar almış, ECC limitleri aşıldı.")
            
    except Exception as e:
        print(f"\n🚨 KRİTİK HATA: Zaman, kilitleri paramparça etmiş olabilir. Detay: {e}")

if __name__ == "__main__":
    run_bio_economics_test()