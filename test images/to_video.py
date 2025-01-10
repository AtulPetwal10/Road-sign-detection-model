import cv2
import os

def create_video_from_images(image_folder, output_video, frame_rate):
    # Get list of all image files in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    
    if not images:
        print("No images found in the specified folder.")
        return

    # Sort images to maintain the correct order
    images.sort()

    # Read the first image to determine frame size
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, _ = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for .mp4 files
    video = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)

        if frame is None:
            print(f"Warning: Could not read {image_name}, skipping.")
            continue

        video.write(frame)  # Write frame to video

    # Release the VideoWriter
    video.release()
    print(f"Video created successfully: {output_video}")

# Parameters
image_folder = "./"  # Replace with the path to your folder containing images
output_video = "output_video.mp4"          # Desired output video file name
frame_rate = 30                            # Frames per second

# Create the video
create_video_from_images(image_folder, output_video, frame_rate)