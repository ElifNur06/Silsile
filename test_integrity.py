import hashlib
import os
from codec import DNACodec
from simulation.synthesizer import SynthesisSimulator

def run_suite():
    print("--- 🧪 DNA Depolama Kapsamlı Test Protokolü ---")
    
    # 1. Dosya oluştur (Test verisi)
    test_file = "test_data.bin"
    with open(test_file, "wb") as f:
        f.write(os.urandom(1024)) # 1KB rastgele veri
    
    with open(test_file, "rb") as f:
        original = f.read()
    
    # 2. Pipeline Testi
    codec = DNACodec(ecc_symbols=64)
    sim = SynthesisSimulator(error_rate=0.005) # %0.5 hata oranı
    
    # Encode -> Noise -> Decode
    dna = codec.encode(original)
    noisy_dna = sim.simulate_lab_process(dna)
    recovered = codec.decode(noisy_dna)
    
    # 3. Validasyon
    orig_hash = hashlib.sha256(original).hexdigest()
    rec_hash = hashlib.sha256(recovered).hexdigest()
    
    print(f"Orijinal Hash: {orig_hash}")
    print(f"Kurtarılan Hash: {rec_hash}")
    
    if orig_hash == rec_hash:
        print("✅ TEST BAŞARILI: Veri bütünlüğü doğrulandı.")
    else:
        print("❌ TEST BAŞARISIZ: Veri bozulmuş.")

if __name__ == "__main__":
    run_suite()