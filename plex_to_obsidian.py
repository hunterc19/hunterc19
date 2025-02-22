import os
import subprocess
from datetime import datetime
import time

# Set your video folder path
VIDEO_FOLDER = "//DESKTOP-61I9JEQ/Plex/Movies"  # Change this to your actual folder
OBSIDIAN_VAULT = "C:/Users/Admin/Desktop/obsidian/Plex/Movies"  # Change this to your Obsidian vault path
MOVIE_INDEX_FILE = os.path.join(os.path.dirname(OBSIDIAN_VAULT), "Movie Library.md")

# Ensure the target directory exists
os.makedirs(OBSIDIAN_VAULT, exist_ok=True)

# Supported video formats
VIDEO_EXTENSIONS = (".mp4", ".m4v")

# Function to get video duration using ffprobe
def get_video_duration(file_path):
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        duration = float(result.stdout.strip())
        minutes, seconds = divmod(int(duration), 60)
        return f"{minutes} min {seconds} sec"
    except Exception:
        return "Unknown"

# Get all video files
video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(VIDEO_EXTENSIONS)]

print(f"Total video files found: {len(video_files)}")

# Create individual Markdown files with metadata
movie_links = []
created_files = 0
for video in video_files:
    movie_title = os.path.splitext(video)[0]
    file_path = os.path.join(VIDEO_FOLDER, video)
    md_filename = f"{movie_title}.md"
    md_filepath = os.path.join(OBSIDIAN_VAULT, md_filename)

    try:
        # Extract metadata
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
        creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        duration = get_video_duration(file_path)

        # Write the Markdown file
        with open(md_filepath, "w", encoding="utf-8") as md_file:
            md_file.write(f"""

# {movie_title}

**Size:** {file_size:.2f} MB  
**Created On:** {creation_time}  
**Duration:** {duration}  

[[Movie Library.md]]
""")

        movie_links.append(f"- [{movie_title}]({md_filename})")
        created_files += 1
    except Exception as e:
        print(f"❌ Error processing {video}: {e}")

# Create the master Movies.md file
with open(MOVIE_INDEX_FILE, "w", encoding="utf-8") as index_file:
    index_file.write("# Movie Library\n\n" + "\n".join(movie_links))

print(f"✅ Markdown files created: {created_files} out of {len(video_files)}")
