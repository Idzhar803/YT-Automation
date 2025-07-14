# main.py
from googleapiclient.discovery import build
from auth_helper import load_token

akun_list = [
    {"nama": "akun1", "token_path": "tokens/akun1_token.json"},
    {"nama": "akun2", "token_path": "tokens/akun2_token.json"},
    # Tambahkan akun lagi di sini
]

video_id = "VIDEO_ID_KAMU"
komentar = "Komentar otomatis dari bot 🔥"

for akun in akun_list:
    print(f"[{akun['nama']}] Mengirim komentar...")

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
