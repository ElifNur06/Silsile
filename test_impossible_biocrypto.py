import os
import random
from codec import DNACodec

def inject_noise(dna_seq, error_rate=0.10):
    """Gerçekçi Laboratuvar Yıkımı: %10 Çerçeve Kaydırmalı Mutasyon."""
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

def generate_phage_genome_mock(length=5386):
    """
    Bakteriyofaj Phi X 174 (DNA'sı dizilenen ilk canlı) genomuna 
    benzer gerçekçi bir 'background' (arka plan) DNA simülasyonu üretir.
    (Homopolimerler ve karmaşık GC oranları içerir).
    """
    seq = ""
    # Gerçek biyolojik diziler rastgele değildir, kısa tekrarlar içerir
    motifs = ["ATGC", "CCGG", "TATA", "GATC", "AAAA", "TTTT", "CGCG"]
    while len(seq) < length:
        if random.random() < 0.2:
            seq += random.choice(motifs)
        else:
            seq += random.choice(['A', 'T', 'C', 'G'])
    return seq[:length]

def run_impossible_biocrypto():
    print("--- 🦠 FİNAL CASUSLUK BOSS'U: CANLI GENOMU (İN VİVO) KAMUFLAJ TESTİ ---")
    
    codec = DNACodec()
    # 2KB'lık çok gizli bir veri yığını
    secret_data = os.urandom(2048) 
    PASSWORD = "OMER_KARATAS_2026"
    
    print("\n📦 Aşama 1: Veri paketleniyor ve PCR Primer'larıyla (Şifre) kilitleniyor...")
    # Sadece kodlama kısmını kullan (Çöp DNA'yı kendimiz ekleyeceğiz)
    raw_encoded_dna = codec.encode(secret_data) 
    
    # Şifrelerimizi üretiyoruz
    f_primer, r_primer = codec._generate_primers(PASSWORD)
    secured_payload = f_primer + raw_encoded_dna + r_primer
    
    print(f"🔬 Aşama 2: Şifreli Veri ({len(secured_payload)} baz), gerçek bir 'Bakteriyofaj' genomunun içine gömülüyor (İn Vivo Saklama)...")
    
    # Verimizi devasa ve karmaşık bir canlının DNA'sının tam ortasına enjekte ediyoruz!
    host_genome_start = generate_phage_genome_mock(50000) # 50.000 baz başa
    host_genome_end = generate_phage_genome_mock(50000)   # 50.000 baz sona
    
    hybrid_organism_dna = host_genome_start + secured_payload + host_genome_end
    print(f"📏 Melez Organizma Genom Uzunluğu: {len(hybrid_organism_dna)} baz")
    
    print(f"🌪️ Aşama 3: Organizma mutasyona uğratılıyor (%10 Yıkıcı Frame-Shift)...")
    mutated_organism_dna = inject_noise(hybrid_organism_dna, error_rate=0.10)
    print(f"📏 Mutasyon Sonrası Uzunluk: {len(mutated_organism_dna)} baz")
    
    print("\n[HÜCRESEL ANALİZ VE VERİ ÇIKARMA İŞLEMİ BAŞLATILDI]")
    try:
        # Kodumuzu, bu kaotik melez canlı genomu ile besliyoruz
        recovered_bytes = codec.decode(mutated_organism_dna, password=PASSWORD)
        
        # Orijinal boyuta kırp
        recovered_bytes = recovered_bytes[:len(secret_data)]
        
        if recovered_bytes == secret_data:
            print("\n🌟 İMKANSIZ BAŞARILDI (MOLEKÜLER ZAFER)!")
            print("Sistem, devasa bir canlı genomunun içinde saklanan, üzerine %10 ölümcül mutasyon eklenmiş veriyi buldu, şifresini kırdı ve %100 doğrulukla geri çıkardı.")
        else:
            print("\n❌ HATA: Şifre açıldı ama veri bozuldu (ECC limitleri aşıldı).")
            
    except Exception as e:
        print(f"\n🚨 Kritik Çökme: {e}")

if __name__ == "__main__":
    run_impossible_biocrypto()