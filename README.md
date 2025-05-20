# 🔵 Blue Object Tracking System

<img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python">
<img src="https://img.shields.io/badge/OpenCV-4.5+-orange?logo=opencv" alt="OpenCV">
<img src="https://img.shields.io/badge/License-MIT-green" alt="License">

Real-time blue object detection and tracking using HSV color space in OpenCV.


## ✨ Features
- Real-time object tracking
- Adjustable HSV color thresholds
- Noise filtering by contour area
- Webcam integration
- Simple green bounding box visualization


## 🚀 Quick Start

### Prerequisites
```bash
pip install opencv-python numpy
```
### Usage
```bash
python blue_tracker.py
```
### Controls
Press Q to quit the application

Adjust HSV values in code for different colors

## 🛠 Customization
Modify these values in the code:
```python
# HSV Range for detection (Blue by default)
blue_lower = np.array([100, 50, 50])    # Lower HSV threshold
blue_upper = np.array([140, 255, 255])  # Upper HSV threshold

# Minimum contour area (adjust for sensitivity)
if area > 100:  # Increase for larger objects
```

## 📚 Technical Details
1.Converts BGR → HSV color space

2.Creates mask using HSV range

3.Finds contours in the mask

4.Filters small contours by area

5.Draws bounding boxes around detected objects


## 🧪 Testing with Different Colors
Use this HSV color range reference:
## 🎨 HSV Color Ranges Reference

| Color       | Lower HSV Range | Upper HSV Range | Visual Example |
|-------------|-----------------|-----------------|----------------|
| **Red**     | `[0, 70, 50]`   | `[10, 255, 255]` | 🔴             |
| **Green**   | `[40, 70, 50]`  | `[80, 255, 255]` | 🟢             |
| **Blue**    | `[100, 50, 50]` | `[140, 255, 255]`| 🔵             |

### 💡 Usage Tips:
1. **Hue Values**: 
   - Red area is split (0-10 and 170-180)
   ```python
   # For full red detection:
   lower_red1 = np.array([0, 70, 50])
   upper_red1 = np.array([10, 255, 255])
   lower_red2 = np.array([170, 70, 50])
   upper_red2 = np.array([180, 255, 255])
   ```
  2. **Sensitivity Adjustment**:

 Increase saturation (2nd value) for more vivid colors

Decrease value (3rd number) for darker environments

3.**Test Colors**:

```python
def test_hsv_range(lower, upper):
    test_color = np.uint8([[[lower[0], 255, 255]]])
    bgr_color = cv2.cvtColor(test_color, cv2.COLOR_HSV2BGR)
    print(f"Preview Color: {bgr_color[0][0]}")
```
