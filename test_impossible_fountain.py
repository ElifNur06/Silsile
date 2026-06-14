import os
import hashlib
from omega_codec import OmegaCodec
from time_machine import BioTimeMachine
import time

def run_fountain_apocalypse():
    print("--- Ω KUANTUM ÇEŞME KODLARI: KOZMİK KIYAMET RÖVANŞI ---")
    print("    [Mimari: Nano-Droplet Bipartite Graph Peeling]")
    
    codec = OmegaCodec()
    tm = BioTimeMachine()
    PASSWORD = "OMEGA_PROTOCOL_ABSOLUTE_ZERO"
    
    print("\n📦 Kritik Veri Paketi (50 KB) şifreleniyor...")
    data = os.urandom(50 * 1024)
    original_hash = hashlib.sha256(data).hexdigest()
    
    start_encode = time.time()
    # Yedeklilik 5.0x (Damla boyutu küçüldüğü için maliyet stabil kalacaktır)
    dna = codec.encode(data, password=PASSWORD, drop_multiplier=5.0)
    
    # Yeni blok hesaplaması: chunk_size artık 12
    k_value = len(data) // 12 if len(data) % 12 == 0 else (len(data) // 12) + 1
    
    costs = tm.calculate_synthesis_cost(len(dna))
    print(f"📏 Yeni DNA Uzunluğu: {len(dna):,} baz")
    print(f"💰 Yeni Sentezleme Maliyeti: ${costs['grand_total']:,.2f}")
    
    print("\n☄️ [KIYAMET SENARYOSU] 10.000 Yıllık Dehşet: Buzul Çağı + 5 Yıllık Güneş Patlaması...")
    
    dna, _ = tm.simulate_aging(dna, 5000, -20.0)
    dna, _ = tm.simulate_aging(dna, 5, 45.0)
    dna, stats = tm.simulate_aging(dna, 4995, -20.0)
    
    print(f"🧬 İskelet Kırılması (Total Frame-Shift): {stats['cleavage']:,}")
    
    print("\n⚕️ LABORATUVAR: Dekoder çalıştırılıyor...")
    
    start_decode = time.time()
    try:
        recovered = codec.decode(dna, k=k_value, password=PASSWORD)
        recovered = recovered[:len(data)]
        
        print(f"⏱️ Kod Çözme Süresi: {time.time() - start_decode:.2f} saniye")
        
        if hashlib.sha256(recovered).hexdigest() == original_hash:
            print(f"🔓 Kurtarılan Hash: {original_hash}")
            print("\n👑 MİMARİ ZAFER: Nano-Damlacıklar çerçeve kaymalarından kurtuldu. SİSTEM BAŞARILI!")
        else:
            print("\n❌ SİSTEM ÇÖKTÜ: Hash uyumsuzluğu.")
            
    except Exception as e:
        print(f"\n💀 KRİTİK HATA: {e}")

if __name__ == "__main__":
    run_fountain_apocalypse()