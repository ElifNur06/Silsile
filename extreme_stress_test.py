import os
import hashlib
import random
from codec import DNACodec

def extreme_stress_test():
    print("--- ☢️ DNA İMKANSIZ STRES TESTİ (KALICI BİT-HİZALAMALI ÇÖZÜM) ---")
    
    codec = DNACodec()
    original = os.urandom(1024) 
    
    dna = list(codec.encode(original))
    
    # Tam %20 Yıkıcı Veri Kaybı!
    for i in range(len(dna)):
        if random.random() < 0.20:
            dna[i] = 'N'
            
    corrupted_dna = "".join(dna)
    
    recovered = codec.decode(corrupted_dna)
    
    # Padding eklendiği için orijinal boyuta göre kırpıyoruz
    recovered = recovered[:len(original)]
    
    if hashlib.sha256(original).hexdigest() == hashlib.sha256(recovered).hexdigest():
        print("✅ MUCİZEVİ BAŞARI: Veri, bit kayması engellenerek tam %20 kayıpla kurtarıldı!")
    else:
        print("❌ SİSTEM ÇÖKTÜ.")

if __name__ == "__main__":
    extreme_stress_test()