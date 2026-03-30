
## 🌐 Languages

- [🇬🇧 English](#-video-transcriber-tool)
- [🇯🇵 日本語](#-動画文字起こしツール)

# 🎬 Video Transcriber Tool

A simple and lightweight tool to transcribe video and audio files into text using OpenAI Whisper (via faster-whisper).

---

## ✨ Features

- Supports multiple file selection
- Automatic transcription with timestamps
- Clean `.txt` output
- Works on any PC (CPU mode)
- Optional GPU acceleration (NVIDIA CUDA)

---

## 📦 How to Use

1. Launch the executable:
    Transcriber.exe

2. Select one or more video/audio files when prompted

3. Wait for the transcription to complete

4. A `.txt` file will be created next to each original file

---

## ⚙️ Performance Notes

### 🐢 CPU Mode (Default)

- Works on any machine
- Slower processing time (especially for long videos)

### ⚡ GPU Mode (Advanced)

If you have an NVIDIA GPU, you can significantly speed up transcription.

Requirements:

- NVIDIA GPU
- CUDA-compatible drivers installed

This tool can be recompiled to use GPU acceleration.

If you are unsure how to set this up, I’m more than happy to help!

---

## 🌠 Special Note

This build was created specifically for **Hina (藤依ひな)**.

At the moment, it is configured to run on CPU for maximum compatibility.  
This means it may be slower, especially for longer videos.

If you have an NVIDIA GPU, we can enable a much faster version together.

Feel free to reach out to me anytime — I’ll gladly help you set everything up!

---

## 🛠 Technical Details

- Model: Whisper (faster-whisper)
- Default configuration:
- Model size: `small`
- Device: `CPU`
- Compute type: `int8`
- Chunk-based processing for memory stability

---

## 📁 Output

Each processed file will generate:
    filename.txt

With content like:
    [00:00:05] Example transcription line

---

## ⚠️ Notes

- Transcription quality depends on audio clarity
- CPU mode prioritizes compatibility over speed
- GPU mode requires proper CUDA setup

---

## 💫 Support

If you need help or want to improve performance:

- Contact me directly
- I’ll assist you step by step

---

## 🚀 Future Improvements

- GPU auto-detection
- Progress bar
- Translation support
- GUI enhancements

---

Made with ⚡ by NiYu

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

-----------------------------------------------------------------------------------------------------

# 🎬 動画文字起こしツール

OpenAI Whisper（faster-whisper）を使用して、動画や音声ファイルをテキスト化するシンプルなツールです。

---

## ✨ 主な機能

- 複数ファイルの同時選択
- タイムスタンプ付き文字起こし
- シンプルな `.txt` 出力
- CPU環境でも動作可能
- NVIDIA GPUによる高速化（オプション）

---

## 📦 使い方

1. 実行ファイルを起動します：
    Transcriber.exe

2. 文字起こししたいファイルを選択します

3. 処理が完了するまで待ちます

4. 元ファイルと同じ場所に `.txt` ファイルが作成されます

---

## ⚙️ パフォーマンスについて

### 🐢 CPUモード（デフォルト）

- どのPCでも動作可能
- 動画が長い場合、処理に時間がかかります

### ⚡ GPUモード（上級者向け）

NVIDIA製のGPUをお持ちの場合、処理速度を大幅に向上させることができます。

必要条件：

- NVIDIA GPU
- CUDA対応ドライバ

GPU版への切り替えも可能です。

設定方法がわからない場合は、お気軽にご相談ください！

---

## 🌠 特別なご案内

このツールは **藤依ひなさん** のために特別に作成されました。

現在は互換性を重視し、CPUで動作するように設定されています。  
そのため、長い動画では処理に時間がかかる場合があります。

もしNVIDIA GPUをお持ちであれば、より高速な設定に変更することも可能です。

必要であれば、いつでもサポートしますので、お気軽にご連絡ください！

---

## 🛠 技術情報

- モデル：Whisper（faster-whisper）
- 設定：
- モデルサイズ：`small`
- デバイス：CPU
- 計算方式：`int8`
- メモリ安定化のための分割処理あり

---

## 📁 出力形式

各ファイルに対して：
    filename.txt

内容例：
    [00:00:05] サンプルテキスト

---

## ⚠️ 注意事項

- 音声品質によって精度が変わります
- CPUモードは安定性重視のため低速です
- GPU利用にはCUDA設定が必要です

---

## 💫 サポート

設定や高速化について：

- 直接ご連絡ください
- 丁寧にサポートします

---

## 🚀 今後の予定

- GPU自動検出
- 進捗表示
- 翻訳機能
- GUI改善

---

NiYuより ⚡

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
