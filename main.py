import cv2 as cv
import mediapipe as mp

mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

peace=[0,1,1,0,0]
thumbsUp=[1,0,0,0,0]
handsOpen=[1,1,1,1,1]

def rescaleFrame(frame):
  scale=0.5
  width=int(frame.shape[1] * scale)
  height=int(frame.shape[0] * scale)
  dimensions=(width,height)

  return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

video = cv.VideoCapture(0)

hands=mp_hand.Hands(
  static_image_mode=False,       
  max_num_hands=2,              
  min_detection_confidence=0.7, 
  min_tracking_confidence=0.5 
)

while True:
  isTrue, frame=video.read()

  if isTrue == False:
    break

  frame=cv.flip(frame,1)
  frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
  frame.flags.writeable=False
  img=None

  results=hands.process(frame)
  frame.flags.writeable=True

  pattern=[0,0,0,0,0]
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
      thumb_tip=hand_landmarks.landmark[4]
      thumb_joint=hand_landmarks.landmark[2]
      if thumb_tip.x<thumb_joint.x:
        pattern[0]=1

      index_tip=hand_landmarks.landmark[8]
      index_joint=hand_landmarks.landmark[6]
      if index_tip.y<index_joint.y:
        pattern[1]=1

      middle_tip=hand_landmarks.landmark[12]
      middle_joint=hand_landmarks.landmark[10]
      if middle_tip.y<middle_joint.y:
        pattern[2]=1

      ring_tip=hand_landmarks.landmark[16]
      ring_joint=hand_landmarks.landmark[14]
      if ring_tip.y<ring_joint.y:
        pattern[3]=1

      pinky_tip=hand_landmarks.landmark[20]
      pinky_joint=hand_landmarks.landmark[18]
      if pinky_tip.y<pinky_joint.y:
        pattern[4]=1
      mp_draw.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)

  if pattern==peace:
    img=cv.imread('photos/peace.png')
  elif pattern==thumbsUp:
    img=cv.imread('photos/thumbsup.png')
  elif pattern==handsOpen:
    img=cv.imread('photos/handsopen.png')

  if img is not None:
    cv.imshow('Gesture',rescaleFrame(img))

  else:
    if cv.getWindowProperty('Gesture', cv.WND_PROP_VISIBLE)>=1:
      cv.destroyWindow('Gesture')

  frame=cv.cvtColor(frame,cv.COLOR_RGB2BGR)
  cv.imshow('Webcam',frame)
  
  key=cv.waitKey(1)
  if key==ord('q'):
    break

video.release()
cv.destroyAllWindows()