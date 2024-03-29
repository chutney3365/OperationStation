import numpy as np
import cv2
import pyrealsense2 as rs
from PIL import Image

# Initialize RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()

# Enable depth and color streams
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30) # 640 x 480 image; can adjust frame dimensions
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
# queue = rs.frame_queue(1)
# pipeline.start(config, queue)
pipeline.start(config)

# Create an empty list to store frames
frames_list = []

try:
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    if color_frame:
        color_image = np.asanyarray(color_frame.get_data())
        frames_list.append(color_image)
        cv2.imshow('RealSense', color_image)
        image = Image.fromarray(color_image)
        cv2.imwrite("image.png", color_image) # or image.save("image.png")
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 
    # pipeline.stop()
    # while True:
    #     # Wait for frames
    #     frames = pipeline.wait_for_frames()

    #     # Get color frame
    #     color_frame = frames.get_color_frame()

    #     if not color_frame:
    #         continue

    #     # Convert color frame to numpy array
    #     color_image = np.asanyarray(color_frame.get_data())

    #     # Append the frame to the frames list
    #     frames_list.append(color_image)

    #     # Display the frame
    #     cv2.imshow('RealSense', color_image)
    #     if cv2.waitKey(1) "&" 0xFF == ord('q'):
    #         break

finally:
    # Stop streaming
    pipeline.stop()

    # Convert the frames list to a NumPy array
    frames_array = np.array(frames_list)

    # Print the shape of the frames array
    print("Shape of frames array:", frames_array.shape)