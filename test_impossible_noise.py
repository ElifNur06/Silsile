import os
import hashlib
from codec import DNACodec
import random

def inject_real_noise(dna_seq, error_rate=0.08):
    """Sinsi Laboratuvar Gürültüsü: İndeksleri kaydıran Indel hataları."""
    bases = ['A', 'T', 'C', 'G']
    seq = list(dna_seq)
    
    i = 0
    while i < len(seq):
        if random.random() < error_rate:
            op = random.choice(['sub', 'del', 'ins'])
            if op == 'sub':
                seq[i] = random.choice([b for b in bases if b != seq[i]])
            elif op == 'del':
                seq.pop(i)
                i -= 1 
            elif op == 'ins':
                seq.insert(i, random.choice(bases))
                i += 1 
        i += 1
    return "".join(seq)

def run_impossible_test():
    print("--- ☠️ DNA FİNAL BOSS TESTİ: ÇERÇEVE KAYMASI (FRAME-SHIFT) ---")
    
    codec = DNACodec() # En güçlü ayarlarıyla başlatıyoruz
    
    # 1. 2KB'lık gerçekçi bir dosya verisi oluştur
    original_data = os.urandom(2048)
    original_hash = hashlib.sha256(original_data).hexdigest()
    
    print(f"📦 Orijinal Veri Boyutu: {len(original_data)} bayt")
    
    # 2. Kodlama
    print("🧬 Veri DNA'ya dönüştürülüyor...")
    dna = codec.encode(original_data)
    print(f"📏 Orijinal DNA Uzunluğu: {len(dna)} baz")
    
    # 3. Yıkım: %8 Frame-Shift Gürültüsü
    # (Not: Geleneksel ECC algoritmaları %1'lik kaymada bile tamamen çöker)
    print("🌪️ %8 Oranında Ekleme/Silme/Değiştirme Mutasyonu Uygulanıyor...")
    noisy_dna = inject_real_noise(dna, error_rate=0.08)
    print(f"📏 Mutasyonlu DNA Uzunluğu: {len(noisy_dna)} baz (KAYMA OLDU!)")
    
    # 4. Kurtarma Girişimi
    print("⚕️ Reed-Solomon Kurtarma Protokolü Başlatıldı...")
    recovered_data = codec.decode(noisy_dna)
    recovered_data = recovered_data[:len(original_data)] # Padding temizliği
    
    # 5. Sonuç
    if recovered_data == original_data:
        print("\n✅ İMKANSIZ BAŞARILDI: Veri frame-shift gürültüsünden kurtarıldı!")
    else:
        print("\n❌ SİSTEM ÇÖKTÜ: Çerçeve kayması (Frame-Shift) tüm blokları bozdu.")
        print("   Reed-Solomon, hangi bazın hangi bayta ait olduğunu kaybetti.")

if __name__ == "__main__":
    run_impossible_test()