import cv2
def survey_bike(bikes):
### the idea here it's to give an option to open the camera and then the user will take pictures of the product(bike) or make a video of the bike
#the type of pic is side, front, wheels, id and model.
#the video needs show full body bike
#has a limit time to make the survey
#the user couldn't open the gallery and take old pictures of the bike
#to verify this option we will probably use IA using deeplearning with TensorFlow Object Detection: Detection Models, but we need a big bike database
    # define image and video capture objects
    #This is a prototype of what we what to include
    cap = cv2.VideoCapture(0) # use the default camera
    img_counter = 0
    vid_counter = 0

    # define maximum survey time
    survey_time = 60 # in seconds

    # initialize image and video names
    img_names = ['side', 'front', 'wheels', 'id', 'model']
    vid_name = 'full_body'

    # loop until maximum survey time is reached
    start_time = cv2.getTickCount()
    while True:
        # check if survey time is exceeded
        current_time = cv2.getTickCount()
        if (current_time - start_time) / cv2.getTickFrequency() > survey_time:
            break

        # read image from camera
        ret, frame = cap.read()

        # display image
        cv2.imshow('frame', frame)

        # check for keypresses
        k = cv2.waitKey(1)
        if k == 27: # ESC key to exit
            break
        elif k == 32: # space key to capture image
            if img_counter < len(img_names):
                img_name = 'imgtaken/{}.jpg'.format(img_names[img_counter])
                cv2.imwrite(img_name, frame)
                img_names.append(img_name)
                img_counter += 1
        elif k == ord('v'): # 'v' key to start recording video
            vid_name = 'videotaken/full_body.avi'
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(vid_name, fourcc, 20.0, (640, 480))
        elif k == ord('r'): # 'r' key to stop recording video
            out.release()
            vid_counter += 1

    # release image and video capture objects
    cap.release()
    cv2.destroyAllWindows()

    # run object detection on captured images
    # use TensorFlow Object Detection API

    # return results
    return img_names, vid_name
