ent)
    if event ==cv2.EVENT_LBUTTONDOWN:
        print("left click")
        print(x,y)
    elif event==cv2.EVENT_LBUTTONDBLCLK:
        print("double click")
        print(x,y)
    if event==cv2.EVENT_LBUTTONDOWN:
        print("left click")
        # cv2.circle(frame,(x,y),50,(0,0,255),-1)
        circles.append((x,y))