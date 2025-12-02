import codecs

# Read the HTML file
with codecs.open('soul_junction.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Brass & Soul with とけていく (handle HTML entities)
content = content.replace('Brass &amp; Soul', 'とけていく')

# Replace the info for this album
content = content.replace('2024 | EP | 6 Tracks', '2025 | EP | 1 Tracks')

# Replace the image and add audio (find the second music-card)
import re

# Find the position of the second music-card (between first and third)
pattern = r'(<div class="music-card">.*?<img src="album_cover\.png" alt="とけていく Album".*?</div>\s*</div>)'
replacement = '''<div class="music-card" id="toketeiku-card">
                <img src="t.jpg" alt="とけていく Album" class="music-card-image">
                <div class="music-card-content">
                    <h3 class="music-card-title">とけていく</h3>
                    <p class="music-card-info">2025 | EP | 1 Tracks</p>
                    <audio id="toketeiku-audio" src="t.wav" preload="metadata"></audio>
                    <a href="#" class="play-button" data-audio="toketeiku-audio">▶ Play</a>
                </div>
            </div>'''

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with codecs.open('soul_junction.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated successfully!")
