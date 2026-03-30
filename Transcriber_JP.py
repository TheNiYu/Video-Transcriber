from faster_whisper import WhisperModel
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


# =========================
# CONFIG
# =========================
MODEL_SIZE = "small" # "large-v3"
DEVICE = "cpu" # "cuda"
COMPUTE_TYPE = "int8" # "float16"
BEAM_SIZE = 5


# =========================
# UTILS
# =========================
def format_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def clean_text(text: str) -> str:
    return (text or "").strip()


# =========================
# FILE PICKER
# =========================
def select_files():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="文字起こしするファイルを選択してください",
        filetypes=[
            ("動画 / 音声ファイル", "*.mp4 *.mkv *.mp3 *.wav"),
            ("すべてのファイル", "*.*")
        ]
    )

    return list(file_paths)


# =========================
# CORE
# =========================
def transcribe_video(file_path: str, model):
    video = Path(file_path)

    if not video.exists():
        print(f"❌ ファイルが見つかりません: {video}")
        return

    output_path = video.with_suffix(".txt")

    print(f"\n🎬 文字起こし中: {video.name}\n")

    segments, info = model.transcribe(
        str(video),
        beam_size=BEAM_SIZE,
        vad_filter=True,
        chunk_length=10
    )

    lines_written = 0

    with open(output_path, "w", encoding="utf-8") as f:
        for seg in segments:
            text = clean_text(seg.text)

            if not text:
                continue

            if hasattr(seg, "no_speech_prob") and seg.no_speech_prob > 0.6:
                continue
            if hasattr(seg, "avg_logprob") and seg.avg_logprob < -1.0:
                continue

            timestamp = format_timestamp(seg.start)
            line = f"[{timestamp}] {text}"

            print(line)
            f.write(line + "\n")

            lines_written += 1

    print("\n==============================")
    print(f"✅ 文字起こしが完了しました")
    print(f"📝 出力行数: {lines_written}")
    print(f"📁 保存ファイル: {output_path}")
    print("==============================\n")


# =========================
# ENTRYPOINT
# =========================
if __name__ == "__main__":
    print("📂 文字起こしするファイルを選択してください...")

    files = select_files()

    if not files:
        print("❌ ファイルが選択されていません")
        exit()

    print(f"\n📂 {len(files)} 件のファイルが選択されました")

    print("\n🚀 Whisperモデルを読み込み中...")
    model = WhisperModel(
        MODEL_SIZE,
        device=DEVICE,
        compute_type=COMPUTE_TYPE
    )

    for i, file in enumerate(files, start=1):
        print(f"\n===== [{i}/{len(files)}] =========================")
        transcribe_video(file, model)