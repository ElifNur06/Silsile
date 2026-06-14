import os
import random
import hashlib
from codec import DNACodec
from PIL import Image, ImageDraw

def generate_sample_image(path):
    """Küçük, 200x200 boyutunda basit bir DNA sarmalı resmi oluşturur (~12KB)."""
    print(f"🔄 '{path}' oluşturuluyor...")
    img = Image.new('RGB', (200, 200), color = (30, 30, 30)) # Koyu arka plan
    draw = ImageDraw.Draw(img)
    
    # Basit bir sarmal çizimi (mavi ve yeşil)
    for y in range(0, 200, 5):
        import math
        x1 = 100 + int(30 * math.sin(y / 15))
        x2 = 100 + int(30 * math.sin(y / 15 + math.pi))
        
        # Mavi İplik
        draw.ellipse((x1-3, y-3, x1+3, y+3), fill=(0, 100, 255), outline=None)
        # Yeşil İplik
        draw.ellipse((x2-3, y-3, x2+3, y+3), fill=(0, 255, 100), outline=None)
        # Bağlantılar
        if y % 15 == 0:
            draw.line((x1, y, x2, y), fill=(200, 200, 200), width=1)

    img.save(path, "JPEG")
    print(f"✅ '{path}' başarıyla oluşturuldu ({os.path.getsize(path)} bayt).")

def test_real_image(input_path, output_path):
    print("\n--- 🖼️ GERÇEK GÖRSEL (JPG) DNA TESTİ BAŞLIYOR ---")
    
    # 0. Dosya yoksa oluştur
    if not os.path.exists(input_path):
        generate_sample_image(input_path)

    # 1. Fotoğrafı ikili (binary) formatta oku
    with open(input_path, 'rb') as f:
        original_image = f.read()
    
    original_hash = hashlib.sha256(original_image).hexdigest()
    print(f"📸 Orijinal Fotoğraf Boyutu: {len(original_image)} bayt")
    
    # 2. Kalıcı Bit-Hizalamalı Codec'i Başlat
    codec = DNACodec()
    
    # 3. GÖRSELİ DNA'YA ÇEVİR
    print("🧬 Fotoğraf DNA'ya sentezleniyor... (Bu işlem biraz sürebilir)")
    dna = list(codec.encode(original_image))
    
    # 4. YIKICI SENARYO: %15 SİLİNME
    print("☢️ Laboratuvar hasarı simüle ediliyor (%15 Veri Silinmesi)...")
    for i in range(len(dna)):
        if random.random() < 0.15:
            dna[i] = 'N'
            
    corrupted_dna = "".join(dna)
    
    # 5. DNA'DAN GÖRSELİ KURTAR
    print("⚕️ DNA'dan orijinal fotoğraf kurtarılıyor...")
    recovered_data = codec.decode(corrupted_dna)
    
    # Kırpma (Padding'i temizleme)
    recovered_data = recovered_data[:len(original_image)]
    recovered_hash = hashlib.sha256(recovered_data).hexdigest()
    
    # 6. SONUÇ VE DOSYAYI KAYDETME
    if original_hash == recovered_hash:
        print("\n✅ MUCİZEVİ BAŞARI: Fotoğraf bit-bit aynı şekilde kurtarıldı!")
        
        with open(output_path, 'wb') as f:
            f.write(recovered_data)
            
        print(f"🎉 Kurtarılan fotoğraf klasörüne kaydedildi: {output_path}")
    else:
        print("\n❌ SİSTEM ÇÖKTÜ: Fotoğraf kurtarılamadı (Hash uyuşmazlığı).")

if __name__ == "__main__":
    test_real_image("ornek_foto.jpg", "kurtarilan_foto.jpg")