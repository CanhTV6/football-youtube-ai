"""
Auto Video Builder for Bible Storytelling Episodes (1080p YouTube MP4)
Supports both small storyboards (12 images) and full cinematic episodes (79+ images)
without hitting Windows command-line length or RAM limits.

Usage:
    python build_video.py 01_ong_apraham
    python build_video.py 01_ong_apraham --bgm path/to/ambient.mp3 --bgm-db -25

Expects inside output/bible_stories/<episode>/:
    - <episode>.mp3 (or any *.mp3 file, excluding *_preview.mp3)
    - images/scenes/*.jpg|png|webp (preferred, e.g. AB01-01.jpg .. AB18-03.jpg)
      OR images/*.jpg|png|webp (fallback if images/scenes/ is empty/absent)
Outputs:
    - output/bible_stories/<episode>/<episode>.mp4 (1920x1080, 24fps, smooth Ken Burns + fades)
"""
import argparse
import math
import pathlib
import shutil
import subprocess
import sys
import tempfile


def get_duration(media_path: pathlib.Path) -> float:
    res = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(media_path),
        ],
        capture_output=True, text=True, check=True,
    )
    return float(res.stdout.strip())


def find_scene_images(ep_dir: pathlib.Path) -> tuple[pathlib.Path, list[pathlib.Path]]:
    scenes_dir = ep_dir / "images" / "scenes"
    exts = ("*.jpg", "*.jpeg", "*.png", "*.webp")
    if scenes_dir.is_dir():
        imgs = sorted(p for ext in exts for p in scenes_dir.glob(ext))
        if imgs:
            return scenes_dir, imgs
    img_dir = ep_dir / "images"
    imgs = sorted(p for ext in exts for p in img_dir.glob(ext))
    return img_dir, imgs


def render_single_clip(
    img_path: pathlib.Path,
    out_clip: pathlib.Path,
    seg_dur: float,
    fade_dur: float,
    idx: int,
    total: int,
    fps: int,
):
    frames = int(math.ceil(seg_dur * fps))
    # Gentle 5% alternating zoom-in / zoom-out
    if idx % 2 == 0:
        z_expr = f"1+0.05*on/{frames}"
    else:
        z_expr = f"1.05-0.05*on/{frames}"

    vf_parts = [
        "scale=2160:-1:force_original_aspect_ratio=increase",
        "crop=2160:1215",
        f"zoompan=z='{z_expr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1920x1080:fps={fps}",
        "format=yuv420p",
        "setsar=1",
    ]
    if fade_dur > 0:
        fade_half = fade_dur / 2.0
        if idx > 0:
            vf_parts.append(f"fade=t=in:st=0:d={fade_half:.2f}")
        if idx < total - 1:
            fade_out_st = max(0.0, seg_dur - fade_half)
            vf_parts.append(f"fade=t=out:st={fade_out_st:.2f}:d={fade_half:.2f}")

    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-t", f"{seg_dur:.3f}", "-i", str(img_path),
        "-vf", ",".join(vf_parts),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-an", str(out_clip),
    ]
    subprocess.run(cmd, check=True)


def build_episode_video(
    ep_dir: pathlib.Path,
    bgm_path: pathlib.Path | None,
    bgm_db: float,
    fps: int = 24,
    fade_dur: float = 1.0,
):
    mp3s = [f for f in sorted(ep_dir.glob("*.mp3")) if not f.stem.endswith("_preview")]
    if not mp3s:
        raise FileNotFoundError(
            f"Chưa tìm thấy file .mp3 trong {ep_dir} (hãy bỏ file .mp3 xuất từ Colab vào thư mục này)."
        )
    audio_path = mp3s[0]

    src_dir, imgs = find_scene_images(ep_dir)
    if not imgs:
        raise FileNotFoundError(f"Chưa tìm thấy ảnh nào trong {ep_dir / 'images' / 'scenes'} hoặc {ep_dir / 'images'}")

    total_dur = get_duration(audio_path)
    n = len(imgs)
    seg_dur = total_dur / n
    out_mp4 = ep_dir / f"{ep_dir.name}.mp4"

    print(f">> Tập: {ep_dir.name}")
    print(f">> Nguồn ảnh: {src_dir.relative_to(ep_dir)} ({n} ảnh, ~{seg_dur:.1f}s/ảnh)")
    print(f">> Audio: {audio_path.name} ({total_dur/60:.1f} phút)")

    tmp_dir = pathlib.Path(tempfile.mkdtemp(prefix=f"vid_{ep_dir.name}_"))
    try:
        concat_list = tmp_dir / "clips.txt"
        clip_lines = []
        for idx, img in enumerate(imgs):
            clip_path = tmp_dir / f"clip_{idx:04d}.mp4"
            print(f"   [{idx+1}/{n}] Render {img.name}...", end="\r", flush=True)
            render_single_clip(img, clip_path, seg_dur, fade_dur, idx, n, fps)
            safe_path = str(clip_path).replace("\\", "/").replace("'", "'\\''")
            clip_lines.append(f"file '{safe_path}'")
        print(f"\n>> Đã render xong {n}/{n} phân đoạn. Đang ghép video + audio hoàn chỉnh...")
        concat_list.write_text("\n".join(clip_lines), encoding="utf-8")

        cmd = [
            "ffmpeg", "-y", "-loglevel", "warning", "-stats",
            "-f", "concat", "-safe", "0", "-i", str(concat_list),
            "-i", str(audio_path),
        ]
        if bgm_path:
            cmd += [
                "-stream_loop", "-1", "-i", str(bgm_path),
                "-filter_complex",
                f"[2:a]volume={bgm_db}dB[bgm];[1:a][bgm]amix=inputs=2:duration=first:dropout_transition=3[aout]",
                "-map", "0:v", "-map", "[aout]",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                str(out_mp4),
            ]
        else:
            cmd += [
                "-map", "0:v", "-map", "1:a",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                str(out_mp4),
            ]

        subprocess.run(cmd, check=True)
        print(f"✅ Hoàn tất video: {out_mp4} ({out_mp4.stat().st_size / (1024*1024):.1f} MB)")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", help="Tên thư mục tập, ví dụ: 01_ong_apraham")
    ap.add_argument("--bgm", type=pathlib.Path, default=None, help="File nhạc nền không lời (.mp3/.wav)")
    ap.add_argument("--bgm-db", type=float, default=-25.0, help="Âm lượng nhạc nền theo dB (mặc định -25)")
    ap.add_argument("--fade", type=float, default=1.0, help="Thời lượng chuyển cảnh mờ dần (giây, mặc định 1.0)")
    args = ap.parse_args()

    base = pathlib.Path(__file__).resolve().parent
    ep_dir = base / args.episode
    if not ep_dir.is_dir():
        sys.exit(f"Không tìm thấy thư mục: {ep_dir}")
    build_episode_video(ep_dir, args.bgm, args.bgm_db, fade_dur=args.fade)
