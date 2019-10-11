import cv2
import numpy as np

left_camera_matrix = np.array([[1.7194144252155763e+03, 0., 9.7396489099720088e+02],
                                         [0., 1.7246889040992207e+03, 7.2576405550055301e+02],
                                         [0., 0., 1.]])

left_distortion = np.array([[-3.2711698432703697e-02, 3.0201589505434645e-01, 1.6164832687546133e-03, -1.5307103949639481e-03, -6.5702545723666506e-01 ]])



right_camera_matrix = np.array([[1.7168908152154356e+03, 0., 1.0331466361439373e+03],
                                          [0., 1.7231083606687728e+03, 6.9119005559789980e+02],
                                          [0., 0., 1.]])

right_distortion = np.array([[6.1121002128546979e-03, 4.5640248780657124e-02, -1.1521856958691723e-04, 3.9286522313315160e-04, -1.5110418136803452e-01]])

# om = np.array([0.01911, 0.03125, -0.00960]) # 旋转关系向量
# R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
# print(R)
R = np.array([[9.9982555748461588e-01, 6.9424710407812562e-04, -1.8664742739603710e-02],
                           [-5.1500594643885927e-04, 9.9995372594119614e-01, 9.6062867537008659e-03],
                           [1.8670548182960316e-02, -9.5949985553764033e-03, 9.9977964903936212e-01]])

T = np.array([-70.59612, -2.60704, 18.87635]) # 平移关系向量

size = (640, 480) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)
# print(left_map1,left_map2,right_map1,right_map2)
