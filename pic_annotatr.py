import cv2
import numpy as np

# Load the image
image = cv2.imread('random_frame.png')

# Create a copy for drawing
image_copy = image.copy()

# Global variable to store clicked coordinates
clicked_points = []

def mouse_callback(event, x, y, flags, param):
    """Mouse callback function to capture clicks"""
    if event == cv2.EVENT_LBUTTONDOWN:
        # Store the clicked point
        clicked_points.append((x, y))
        
        # Draw a red circle at the clicked point
        cv2.circle(image_copy, (x, y), 5, (0, 0, 255), -1)
        
        # Draw crosshairs
        cv2.line(image_copy, (x-10, y), (x+10, y), (0, 0, 255), 1)
        cv2.line(image_copy, (x, y-10), (x, y+10), (0, 0, 255), 1)
        
        # Print coordinates
        print(f"Clicked at: x={x}, y={y}")
        
        # Show the updated image
        cv2.imshow('Click to get coordinates', image_copy)

# Display the image
cv2.imshow('Click to get coordinates', image_copy)
cv2.setMouseCallback('Click to get coordinates', mouse_callback)

print("Instructions:")
print("1. Click anywhere on the image to get pixel coordinates")
print("2. Press 'c' to clear all points")
print("3. Press 'q' to quit")

while True:
    key = cv2.waitKey(1) & 0xFF
    
    # Press 'q' to quit
    if key == ord('q'):
        break
    
    # Press 'c' to clear points
    elif key == ord('c'):
        image_copy = image.copy()
        clicked_points = []
        cv2.imshow('Click to get coordinates', image_copy)
        print("All points cleared!")

cv2.destroyAllWindows()

# Print all collected points at the end
if clicked_points:
    print("\n=== All collected points ===")
    for i, (x, y) in enumerate(clicked_points):
        print(f"Point {i+1}: x={x}, y={y}")
else:
    print("\nNo points were clicked.")