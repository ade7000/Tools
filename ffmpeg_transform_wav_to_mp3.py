import os
import subprocess

# Define the folder where the .octet-stream files are located
input_folder = r'D:\path\to\input_folder'  # Replace with your folder path
output_folder = r'D:\path\to\output_folder' # Replace with your folder path

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# Function to convert .octet-stream to .wav using ffmpeg
def convert_to_wav(input_file, output_file):
    try:
        # Command to run ffmpeg to convert the file
        # Change parameter if needed - right now it transform to mono (1 channel),
        # 16000 kHz sample rate and 320kbps bit rate
        command = [
            "ffmpeg", "-i", input_file, "-ac", "1", "-ar", "16000", "-b:a", "256k", output_file
        ]       
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file}: {e}")

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"): # change into the extension that you are working with
        input_file_path = os.path.join(input_folder, filename)
        
        # Create the output file path with .wav extension (same name as input)
        output_filename = f"{os.path.splitext(filename)[0]}.mp3" # change into the extension that you want
        output_file_path = os.path.join(output_folder, output_filename)
        
        # Convert the file to .wav and save it in the same folder
        convert_to_wav(input_file_path, output_file_path)
