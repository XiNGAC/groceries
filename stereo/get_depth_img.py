import numpy as np
import cv2
import camera_configs

# cv2.namedWindow("left")
# cv2.namedWindow("right")
# cv2.namedWindow("depth")
# cv2.moveWindow("left", 0, 0)
# cv2.moveWindow("right", 600, 0)
# cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
# cv2.createTrackbar("blockSize", "depth", 5, 255, lambda x: None)
# camera1 = cv2.VideoCapture(0)
# camera2 = cv2.VideoCapture(1)
frame1 = cv2.imread("left.png")
frame2 = cv2.imread("right.png")

# 添加点击事件，打印当前点的距离
# def callbackFunc(e, x, y, f, p):
#     if e == cv2.EVENT_LBUTTONDOWN:
#         print(threeD[y][x])
#
# cv2.setMouseCallback("depth", callbackFunc, None)

while True:
    # ret1, frame1 = camera1.read()
    # ret2, frame2 = camera2.read()
    #
    # if not ret1 or not ret2:
    #     break

    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(frame1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(frame2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)

    # 将图片置为灰度图，为StereoBM作准备
    # imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    # imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("imgL.jpg", imgL)
    # cv2.imwrite("imgR.jpg", imgR)
    imgL = frame1
    imgR = frame2

    # 两个trackbar用来调节不同的参数查看效果
    # num = cv2.getTrackbarPos("num", "depth")
    #     # blockSize = cv2.getTrackbarPos("blockSize", "depth")
    #     # if blockSize % 2 == 0:
    #     #     blockSize += 1
    #     # if blockSize < 5:
    #     #     blockSize = 5
    min_disp = 0
    num_disp = 64 - min_disp
    num = 3
    blockSize = 9
    window_size = 9
    # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
    # stereo = cv2.StereoBM_create(numDisparities=16*num, blockSize=blockSize)
    stereo = cv2.StereoSGBM_create(minDisparity=min_disp, numDisparities=num_disp, blockSize=blockSize,
                                   P1 = 8 * 3 * window_size**2,
                                   P2 = 32 * 3 * window_size**2,
                                   disp12MaxDiff = 1,
                                   uniquenessRatio = 10,
                                   speckleWindowSize = 100,
                                   speckleRange = 32)
    print(1)
    # disparity = stereo.compute(imgL, imgR)
    disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0
    disparity = (disparity - min_disp) / num_disp
    print(2)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    disp = cv2.medianBlur(disp,5)
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    threeD = cv2.reprojectImageTo3D(disparity, camera_configs.Q)
    cv2.imwrite("disp.jpg",disp)
    print(threeD[300][500])
    break
    # print(threeD)

    # cv2.imshow("left", img1_rectified)
    # cv2.imshow("right", img2_rectified)
    # cv2.imshow("depth", disp)
    #
    # key = cv2.waitKey(1)
    # if key == ord("q"):
    #     break
    # elif key == ord("s"):
    #     cv2.imwrite("./snapshot/BM_left.jpg", imgL)
    #     cv2.imwrite("./snapshot/BM_right.jpg", imgR)
    #     cv2.imwrite("./snapshot/BM_depth.jpg", disp)
#
# camera1.release()
# camera2.release()
# cv2.destroyAllWindows()