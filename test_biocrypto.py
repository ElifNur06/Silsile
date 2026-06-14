import os
import random
from codec import DNACodec

def inject_noise(dna_seq, error_rate=0.08):
    """Biyolojik Mutasyon (Çerçeve kayması dahil) uygular."""
    bases = ['A', 'T', 'C', 'G']
    seq = list(dna_seq)
    i = 0
    while i < len(seq):
        if random.random() < error_rate:
            op = random.choice(['sub', 'del', 'ins'])
            if op == 'sub': seq[i] = random.choice([b for b in bases if b != seq[i]])
            elif op == 'del': 
                seq.pop(i)
                i -= 1 
            elif op == 'ins': 
                seq.insert(i, random.choice(bases))
                i += 1 
        i += 1
    return "".join(seq)

def run_biocrypto_test():
    print("--- 🕵️ MOLEKÜLER CASUSLUK VE KİLİT TESTİ BAŞLIYOR ---")
    
    codec = DNACodec()
    secret_data = b"COK_GIZLI_AJAN_DOSYASI_" * 10 # Gizli metin verisi
    PASSWORD = "OMER_KARATAS_2026"
    
    print("\n📦 Veri şifreleniyor ve 10.000 bazlık Çöp DNA içine gizleniyor...")
    encoded_dna = codec.encode(secret_data, password=PASSWORD)
    
    print(f"📏 Oluşturulan devasa DNA Çorbası uzunluğu: {len(encoded_dna)} baz")
    print(f"🌪️ Laboratuvar ortamı simüle ediliyor (%8 Mutasyon/Gürültü enjekte ediliyor)...")
    
    noisy_dna = inject_noise(encoded_dna, error_rate=0.08)
    
    print("\n[SENARYO 1] YETKİSİZ ERİŞİM DENEMESİ (Yanlış Şifre)")
    try:
        # Kötü niyetli kişi yanlış şifreyle deniyor
        codec.decode(noisy_dna, password="YANLIS_SIFRE_123")
    except Exception as e:
        print(f"🚨 BEKLENEN SONUÇ: {e}")
        
    print("\n[SENARYO 2] YETKİLİ ERİŞİM DENEMESİ (Doğru Şifre)")
    try:
        # Doğru anahtarla PCR işlemi yapılıyor
        recovered_bytes = codec.decode(noisy_dna, password=PASSWORD)
        
        # Padding temizliği
        recovered_bytes = recovered_bytes[:len(secret_data)]
        
        if recovered_bytes == secret_data:
            print("🌟 GÖREV BAŞARILI: Veri devasa çorbanın içinden bulundu, kilit açıldı ve %8'lik hasara rağmen eksiksiz okundu!")
        else:
            print("❌ HATA: Şifre açıldı ama veri bozuk.")
            
    except Exception as e:
        print(f"Kritik Hata: {e}")

if __name__ == "__main__":
    run_biocrypto_test()