import sys

def main():
    print("Virtual Drag uygulamasına hoş geldiniz!")
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"İşlenecek dosya: {file_path}")
        process_file(file_path)
    else:
        print("Lütfen bir dosya yolu belirtin.")

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Dosya içeriği:\n{content}")
            # Burada dosya içeriğiyle ilgili işlemler yapabilirsiniz
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()