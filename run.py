# main.py
from googleapiclient.discovery import build
from auth_helper import load_token

# Ambil input dari user
video_id = input("Masukkan YouTube Video ID: ").strip()
komentar = input("Masukkan komentar yang ingin dikirim: ").strip()

# Daftar akun (token dari masing-masing akun)
akun_list = [
    {"nama": "akun1", "token_path": "tokens/akun1_token.json"},
    {"nama": "akun2", "token_path": "tokens/akun2_token.json"},
    # Tambah akun lagi di sini
]

# Proses kirim komentar
for akun in akun_list:
    print(f"\n[{akun['nama']}] Mengirim komentar ke video {video_id}...")

    creds = load_token(akun["token_path"])
    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": komentar
                    }
                }
            }
        }
    )

    response = request.execute()
    print(f"[{akun['nama']}] ✅ Komentar dikirim: {response['snippet']['topLevelComment']['snippet']['textDisplay']}")
