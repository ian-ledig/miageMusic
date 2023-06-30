import subprocess
import os
import sys
import shutil

def execute_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()

def main(youtube_link):
    if os.path.exists('youtube'):
        shutil.rmtree('youtube')
    if os.path.exists('youtube.mp3'):
        os.remove('youtube.mp3')
    if os.path.exists('output.wav'):
        os.remove('output.wav')

    conda_activate_cmd = f'conda activate miage && '
    subprocess.run(conda_activate_cmd + f'python youtubeDownloader.py {youtube_link}', shell=True)
    subprocess.run(conda_activate_cmd + 'cd spleeter && spleeter separate -p spleeter:2stems -o ../ ../youtube.mp3', shell=True)
    conda_activate_cmd = f'conda activate so-vits-svc-fork && '
    subprocess.run(conda_activate_cmd + 'cd so-vits-svc-fork && svc infer --model-path ../G_laylow.pth --config-path ../config.json --output-path ../output.wav ../youtube/vocals.wav', shell=True)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Veuillez fournir le lien YouTube en tant qu'argument de ligne de commande.")
    else:
        youtube_link = sys.argv[1]
        main(youtube_link)
