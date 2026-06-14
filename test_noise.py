import random

# Eğer simulation klasöründe bu fonksiyonun yoksa, doğrudan buraya ekledik.
def inject_noise(dna_seq, error_rate=0.10):
    """
    DNA dizisine 'error_rate' olasılıkla Substitution, Deletion veya Insertion uygular.
    """
    bases = ['A', 'T', 'C', 'G']
    seq = list(dna_seq)
    stats = {'sub': 0, 'del': 0, 'ins': 0}
    
    i = 0
    while i < len(seq):
        if random.random() < error_rate:
            op = random.choice(['sub', 'del', 'ins'])
            if op == 'sub':
                # Farklı bir baz ile değiştir
                current = seq[i]
                choices = [b for b in bases if b != current]
                seq[i] = random.choice(choices)
                stats['sub'] += 1
            elif op == 'del':
                # Bazı sil
                seq.pop(i)
                stats['del'] += 1
                i -= 1 # Silindiği için indexi geri al
            elif op == 'ins':
                # Araya rastgele baz ekle
                seq.insert(i, random.choice(bases))
                stats['ins'] += 1
                i += 1 # Eklendiği için indexi atla
        i += 1
        
    return "".join(seq), stats

def run_noise_test():
    print("--- 🔬 DNA GÜRÜLTÜ ENJEKSİYONU (MUTASYON) TESTİ ---")
    
    # 50 Bazlık orijinal bir dizi
    original_dna = "ATGCGTACGTAGCTAGCTAGCGATCGATCGATGCGTACGTAGCTAGCTAG"
    error_rate = 0.15 # %15 Hata Oranı
    
    random.seed(42) # Çıktının her çalışmada aynı olması için (kaldırabilirsin)
    
    noisy_dna, stats = inject_noise(original_dna, error_rate)
    
    print(f"\nOrijinal Uzunluk: {len(original_dna)}")
    print(f"Bozulmuş Uzunluk: {len(noisy_dna)}")
    
    print(f"\n[ORİJİNAL] : {original_dna}")
    print(f"[MUTASYON] : {noisy_dna}")
    
    print("\n📊 Mutasyon İstatistikleri:")
    print(f"  - Yer Değiştirme (Substitution) : {stats['sub']} adet")
    print(f"  - Silinme (Deletion)          : {stats['del']} adet")
    print(f"  - Ekleme (Insertion)          : {stats['ins']} adet")
    print(f"  - Toplam Mutasyon             : {stats['sub'] + stats['del'] + stats['ins']} adet")

if __name__ == "__main__":
    run_noise_test()