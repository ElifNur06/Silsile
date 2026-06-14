import os
import random
import hashlib
import time
from steganography import GenomicSteganography

def catastrophic_cellular_decay(genome: str, error_rate: float = 0.12) -> str:
    """
    Hücrenin 10 nesil boyunca bölünmesi sırasında oluşan ağır mutasyonları simüle eder.
    Nokta mutasyonları (Sub) ve özellikle Çerçeve Kayması (Del/Ins) içerir.
    """
    bases = ['A', 'T', 'C', 'G']
    seq = list(genome)
    
    # Optimizasyon: Çok büyük dizilerde while döngüsü yavaş olacağından, 
    # Python'un yeteneklerini zorlayan bir mutasyon motoru kullanıyoruz.
    mutated_seq = []
    for base in seq:
        if random.random() < error_rate:
            op = random.choice(['sub', 'del', 'ins'])
            if op == 'sub':
                mutated_seq.append(random.choice([b for b in bases if b != base]))
            elif op == 'ins':
                mutated_seq.append(base)
                mutated_seq.append(random.choice(bases))
            # 'del' durumunda hiçbir şey eklemiyoruz (baz silindi)
        else:
            mutated_seq.append(base)
            
    return "".join(mutated_seq)

def generate_massive_host_genome(length: int = 1_000_000) -> str:
    """Test için 1 Milyon bazlık devasa bir genom sentezler."""
    print(f"🧫 {length:,} bazlık Devasa Konak Genomu laboratuvarda sentezleniyor (Bu biraz zaman alabilir)...")
    genome = []
    for _ in range(length // 1000):
        if random.random() < 0.70:
            genome.append("".join(random.choices(['A', 'T', 'C', 'G'], weights=[25, 25, 25, 25], k=1000)))
        else:
            genome.append("".join(random.choices(['A', 'T', 'C', 'G'], weights=[45, 45, 5, 5], k=1000)))
    return "".join(genome)[:length]

def run_impossible_steganography_test():
    print("--- ☢️ İMKANSIZ MOLEKÜLER STEGANOGRAFİ: İN VİVO KIYAMET TESTİ ---")
    
    stego = GenomicSteganography()
    PASSWORD = "OMEGA_PROTOCOL_ABSOLUTE_ZERO"
    
    # 1. 15 KB'lık Ağır Bir Veri Bloğu (Kapasite sınırlarını zorluyoruz)
    secret_data = os.urandom(15360) 
    original_hash = hashlib.sha256(secret_data).hexdigest()
    print(f"\n📦 Orijinal Veri Boyutu: {len(secret_data):,} bayt")
    print(f"🔑 Orijinal Hash: {original_hash}")
    
    # 2. Devasa Konak Genomunu Üret
    start_time = time.time()
    host_genome = generate_massive_host_genome(1_000_000)
    
    # 3. Gizli Veriyi Göm
    mutant_genome = stego.camouflage_data(
        host_genome=host_genome, 
        secret_data=secret_data, 
        password=PASSWORD
    )
    
    # 4. YIKIM: Hücreyi 10 nesil boyunca radyasyona ve doğal mutasyona maruz bırak
    print(f"\n☄️ [HÜCRESEL YAŞLANMA BAŞLADI] Melez organizma ağır radyasyona maruz bırakılıyor...")
    print(f"🦠 %12 Çerçeve Kaydırmalı (Frame-Shift) Mutasyon Uygulanıyor...")
    
    destroyed_genome = catastrophic_cellular_decay(mutant_genome, error_rate=0.12)
    print(f"📏 Mutasyon Öncesi Boyut: {len(mutant_genome):,} baz")
    print(f"📏 Mutasyon Sonrası Boyut: {len(destroyed_genome):,} baz (KAYMA MEYDANA GELDİ!)")
    
    # 5. MUCİZE BEKLENTİSİ: Veri Çıkarma
    print("\n⚕️ 1 Milyon bazlık mutasyonlu hücresel enkazın içinde arama kurtarma operasyonu başlatıldı...")
    
    recovered_data = stego.extract_data(
        camouflaged_genome=destroyed_genome, 
        password=PASSWORD, 
        original_size=len(secret_data)
    )
    
    end_time = time.time()
    
    # 6. Kapanış ve Doğrulama
    print(f"\n⏱️ Toplam Operasyon Süresi: {end_time - start_time:.2f} saniye")
    
    if recovered_data:
        recovered_hash = hashlib.sha256(recovered_data).hexdigest()
        print(f"🔓 Kurtarılan Hash: {recovered_hash}")
        
        if original_hash == recovered_hash:
            print("\n👑 TANRISAL MİMARİ KANITLANDI: Sistemin, 1 milyon bazlık bir organizmanın içinde 10 nesil boyunca radyasyona ve %12'lik çerçeve kaymasına maruz kalmasına rağmen 15 KB veriyi %100 kusursuz kurtardı!")
        else:
            print("\n❌ SİSTEM ÇÖKTÜ: Veri bulundu ancak Reed-Solomon zırhı %12'lik hasarı onaramadı (ECC limitleri aşıldı).")
    else:
        print("\n💀 TAMAMEN YIKIM: BLAST algoritması, ağır mutasyonlar nedeniyle primer kilitlerini moleküler enkazın içinde bulamadı.")

if __name__ == "__main__":
    run_impossible_steganography_test()