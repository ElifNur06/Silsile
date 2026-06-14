import os
import random
import hashlib
from steganography import GenomicSteganography

def generate_mock_ecoli_genome(length=4_600_000):
    """
    Test için ~4.6 Milyon bazlık devasa bir E. Coli genomu simüle eder.
    Biyolojik gerçekçilik için aralara AT-zengin çöp bölgeler serpiştirir.
    """
    print(f"🧫 {length} bazlık E. Coli Genomu laboratuvarda sentezleniyor...")
    genome = []
    # %80 Gen bölgesi (Dengeli GC), %20 Çöp bölge (Yüksek AT)
    for _ in range(length // 1000):
        if random.random() < 0.80:
            genome.append("".join(random.choices(['A', 'T', 'C', 'G'], weights=[25, 25, 25, 25], k=1000)))
        else:
            genome.append("".join(random.choices(['A', 'T', 'C', 'G'], weights=[40, 40, 10, 10], k=1000)))
            
    return "".join(genome)[:length]

def run_steganography_test():
    print("--- 🦠 MOLEKÜLER STEGANOGRAFİ: E.COLI KAMUFLAJ TESTİ ---")
    
    stego = GenomicSteganography()
    PASSWORD = "NEON_NOIR_PROTOCOL_2026"
    
    # 1. Aşama: Gizli Fotoğrafı Oluştur (Sanal bir JPEG)
    secret_image_data = os.urandom(5120) # 5KB'lık gizli bir fotoğraf/dosya
    original_hash = hashlib.sha256(secret_image_data).hexdigest()
    print(f"📸 Orijinal Fotoğraf Boyutu: {len(secret_image_data)} bayt (Hash: {original_hash[:8]}...)")
    
    # 2. Aşama: Konak Canlıyı Hazırla
    ecoli_genome = generate_mock_ecoli_genome(100_000) # Test hızlı bitsin diye 100K kullanıyoruz
    
    # 3. Aşama: Kamuflajı Uygula
    mutant_ecoli_genome = stego.camouflage_data(
        host_genome=ecoli_genome, 
        secret_data=secret_image_data, 
        password=PASSWORD
    )
    
    # 4. Aşama: Otoriteleri Kandırma (Opsiyonel Gürültü/Mutasyon Testi eklenebilir)
    # Dışarıdan bakan biri sadece normal bir mutant E. Coli görür.
    
    # 5. Aşama: Ajanın Veriyi Çıkarması
    recovered_data = stego.extract_data(
        camouflaged_genome=mutant_ecoli_genome, 
        password=PASSWORD, 
        original_size=len(secret_image_data)
    )
    
    # Doğrulama
    if recovered_data:
        recovered_hash = hashlib.sha256(recovered_data).hexdigest()
        if original_hash == recovered_hash:
            print("✅ KUSURSUZ DOĞRULAMA: Fotoğrafın tek bir pikseli bile bozulmadan bakterinin içinden çıkarıldı!")
        else:
            print("❌ VERİ BOZUKLUĞU: Hash değerleri uyuşmuyor.")
    else:
        print("❌ SİSTEM BAŞARISIZ: Veri bulunamadı.")

if __name__ == "__main__":
    run_steganography_test()