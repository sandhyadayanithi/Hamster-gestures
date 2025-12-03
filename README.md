# 🐹 Hamster Gesture Recognition

A fun and interactive hand gesture recognition system that rewards your gestures with adorable hamster reactions! Using your webcam and MediaPipe, this project detects three hand gestures and displays cute hamster images performing the same gesture.

## ✨ What It Does

Hold your hand up to the webcam and watch as the hamsters respond:
- ✌️ **Peace Sign** → See a hamster making peace!
- 👍 **Thumbs Up** → Get an encouraging thumbs up from a hamster!
- 🖐️ **Open Hand** → A hamster waves back at you!

## 🎯 Features

- Real-time hand gesture detection using MediaPipe
- Supports detection of 2 hands simultaneously
- Smooth webcam feed with gesture overlay
- Instant hamster feedback when gestures are recognized
- Simple and intuitive - just show your hand!

## 🛠️ Requirements

```bash
pip install opencv-python mediapipe
```

## 📁 Project Structure

```
project/
│
├── main.py
└── photos/
    ├── peace.png       # Hamster doing peace sign
    ├── thumbsup.png    # Hamster giving thumbs up
    └── handsopen.png   # Hamster with open paws
```

## 🚀 How to Run

1. Make sure you have the required images in the `photos/` folder
2. Run the script:
   ```bash
   python main.py
   ```
3. Show your gestures to the webcam!
4. Press 'q' to quit

## 🎮 Recognized Gestures

| Gesture | Pattern | Hamster Response |
|---------|---------|------------------|
| Peace Sign ✌️ | Index & middle fingers up | peace.png |
| Thumbs Up 👍 | Only thumb extended | thumbsup.png |
| Open Hand 🖐️ | All fingers extended | handsopen.png |

## 💡 How It Works

The system uses MediaPipe's hand landmark detection to track 21 points on your hand. It checks the position of your fingertips relative to their joints to determine which fingers are extended, then matches the pattern to one of the three gestures. When a match is found, the corresponding hamster image pops up to mirror your gesture!

## 🎨 Customization

Want to add more gestures? Simply:
1. Add a new pattern list (e.g., `fist=[0,0,0,0,0]`)
2. Add the comparison in the gesture detection section
3. Create a new hamster image for that gesture
4. Watch your hamster collection grow!

## 🐛 Troubleshooting

- **No hamster appearing?** Make sure your fingers are clearly visible and the gesture is held steady
- **Wrong gesture detected?** Try adjusting the lighting or camera angle
- **Images not loading?** Verify the `photos/` folder path and image filenames

---

**Made with Python** | Have fun interacting with your hamster friends!
