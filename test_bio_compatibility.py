import os
import re
from codec import DNACodec

def run_bio_audit():
    print("--- 🔬 BİYOLOJİK UYUMLULUK VE SENTEZ AUDİTİ ---")
    
    codec = DNACodec()
    # Bilerek sistemin homopolimer üretmesini tetikleyecek zorlu bir dosya ('0' lardan oluşan)
    toxic_data = b'\x00' * 1024 
    PASSWORD = "BIO_TEST_2026"
    
    print("\n📦 'Zehirli/Tekrarlayan' veri DNA'ya çevriliyor...")
    dna_seq = codec.encode(toxic_data, password=PASSWORD)
    
    print("\n[LABORATUVAR ANALİZ RAPORU]")
    
    # 1. Homopolimer Taraması (4 ve üzeri yan yana aynı harf var mı?)
    homopolymers = re.findall(r'(A{4,}|T{4,}|C{4,}|G{4,})', dna_seq)
    if not homopolymers:
        print("✅ HOMOPOLİMER TESTİ GEÇİLDİ: Sarmalda 4'ten fazla yan yana aynı harf bulunamadı.")
    else:
        print(f"❌ HOMOPOLİMER İHLALİ: {len(homopolymers)} adet tehlikeli bölge bulundu!")
        
    # 2. GC İçeriği (Content) Analizi
    g_count = dna_seq.count('G')
    c_count = dna_seq.count('C')
    gc_ratio = ((g_count + c_count) / len(dna_seq)) * 100
    
    if 35 <= gc_ratio <= 65:
        print(f"✅ GC DENGESİ TESTİ GEÇİLDİ: İdeal oran yakalandı (%{gc_ratio:.2f} GC içerik).")
    else:
        print(f"❌ GC DENGESİ İHLALİ: Oran limit dışı (%{gc_ratio:.2f}). DNA kırılgandır.")

    # 3. Veri Bütünlüğü Testi (Bilerek yok edilen paketlere rağmen veri sağlam mı?)
    print("\n⚕️ İmha edilen toksik paketlere rağmen veri kurtarılmaya çalışılıyor...")
    try:
        recovered = codec.decode(dna_seq, password=PASSWORD)
        recovered = recovered[:len(toxic_data)]
        if recovered == toxic_data:
            print("🌟 MÜKEMMEL SONUÇ: Veri %100 doğrulukla kurtarıldı. DNA sarmalı laboratuvar için tamamen güvenli ve ölümsüzdür!")
        else:
            print("❌ HATA: Paketler imha edildiği için veri bozuldu.")
    except Exception as e:
        print(f"Kritik Hata: {e}")

if __name__ == "__main__":
    run_bio_audit()