import cv2
import time
import serial


ardu = serial.Serial('COM3',9600, timeout=.1)






# Font to write text overlay
font = cv2.FONT_HERSHEY_SIMPLEX

# Create lists that holds the thresholds
hsvMin = (0, 139, 177)
hsvMax = (94, 255, 255)

# Adjust detection parameters
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 100

# Filter by Area
params.filterByArea = True
params.minArea = 400
params.maxArea = 20000

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.5

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.5

# Get the camera for video capture
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

filling = False

while True:
    # Get a video frame
    _, frame = cap.read()

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply HSV thresholds
    mask = cv2.inRange(hsv, hsvMin, hsvMax)

    # Erode and dilate
    mask = cv2.erode(mask, None, iterations=3)
    mask = cv2.dilate(mask, None, iterations=3)

    # Detect blobs
    detector = cv2.SimpleBlobDetector_create(params)

    # Invert the mask
    reversemask = 255 - mask

    # Run blob detection
    keypoints = detector.detect(reversemask)

    # Get the number of blobs found
    blobCount = len(keypoints)

    # Write the number of blobs found
    text = "Count=" + str(blobCount)
    cv2.putText(frame, text, (5, 25), font, 1, (0, 255, 0), 2)

    # read filling condition from arduino

    if filling == False:
        if blobCount == 0:
            print("TURN LEFT")
            ardu.write(b'L')
        else:
            # Write X position of first blob
            blob_x = keypoints[0].pt[0]
            text2 = "X=" + "{:.2f}".format(blob_x)
            cv2.putText(frame, text2, (5, 50), font, 1, (0, 255, 0), 2)

            # Write Y position of first blob
            blob_y = keypoints[0].pt[1]
            text3 = "Y=" + "{:.2f}".format(blob_y)
            cv2.putText(frame, text3, (5, 75), font, 1, (0, 255, 0), 2)

            # Write Size of first blob
            blob_size = keypoints[0].size
            text4 = "S=" + "{:.2f}".format(blob_size)
            cv2.putText(frame, text4, (5, 100), font, 1, (0, 255, 0), 2)

            # Draw circle to indicate the blob
            cv2.circle(frame, (int(blob_x), int(blob_y)), int(blob_size / 2), (0, 255, 0), 2)

            if blob_y < 320:

                if blob_x >= 340:
                    print("TURN LEFT")
                    ardu.write(b'L')
                elif 320 < blob_x < 340:
                    print("MOVE STRAIGHT")
                    ardu.write(b'F')
                elif blob_x <= 320:
                    print("TURN RIGHT")
                    ardu.write(b'R')
                #break

            else:
                if 320 < blob_x < 340:
                    print("STOP")
                    ardu.write(b'S')
                    time.sleep(2)
                    print("FILL THE HOLE")
                    ardu.write(b'H')
                    time.sleep(2)
                    ardu.write(b'I')
                    filling = True
                else:
                    print("ERROR")
                    print("STOP")
                    ardu.write(b'S')
                    filling = True
                #break
    #else:
    #    filling = False
    C = str(ardu.readline().decode().replace("\r\n", ""))
    print(C)
    if C == "DONE":
        filling = False


    # Show image
    cv2.imshow("Blob detection", frame)
    key = cv2.waitKey(10)
    if key == ord('q') or key == 27:
        break
