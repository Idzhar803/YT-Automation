from googleapiclient.discovery import build
from auth_helper import load_token

# Ambil input dari user
video_id = input("Masukkan YouTube Video ID: ").strip()
komentar = input("Masukkan komentar yang ingin dikirim (6x per akun): ").strip()

# Generate daftar akun dari akununtukmasadepan10 sampai 24
akun_list = []
for i in range(1, 25):  # dari 1 sampai 24
    akun_list.append({
        "nama": f"akununtukmasadepan{i}",
        "token_path": f"tokens/akun{i}_token.json"
    })

# Proses kirim komentar
for akun in akun_list:
    print(f"\n[{akun['nama']}] Mengirim 6 komentar ke video {video_id}...")

    creds = load_token(akun["token_path"])
    youtube = build("youtube", "v3", credentials=creds)

    for j in range(6):
        request = youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                    "videoId": video_id,
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": f"{komentar} ({j+1})"
                        }
                    }
                }
            }
        )
        response = request.execute()
        print(f"[{akun['nama']}] ✅ Komentar ke-{j+1} dikirim: {response['snippet']['topLevelComment']['snippet']['textDisplay']}")
