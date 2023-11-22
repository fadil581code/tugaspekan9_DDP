def kelulusan(nilai):
    if nilai >= 0 and nilai <= 60:
        return "gagal"
    elif nilai <= 70:
        return "baik"
    elif nilai <= 80:
        return "sangat baik"
    elif nilai <= 100:
        return "istimewa"
    else:
        return "nilai tidak valid"
    
print(kelulusan (60))