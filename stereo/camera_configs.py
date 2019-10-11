import cv2
import numpy as np

left_camera_matrix = np.array([[9.597910e+02, 0.000000e+00, 6.960217e+02],
                                         [0.000000e+00, 9.569251e+02, 2.241806e+02],
                                         [0.000000e+00, 0.000000e+00, 1.000000e+00]])

left_distortion = np.array([[-3.691481e-01, 1.968681e-01, 1.353473e-03, 5.677587e-04, -6.770705e-02]])



right_camera_matrix = np.array([[9.037596e+02, 0.000000e+00, 6.957519e+02],
                                          [0.000000e+00, 9.019653e+02, 2.242509e+02],
                                          [0.000000e+00, 0.000000e+00, 1.000000e+00]])

right_distortion = np.array([[-3.639558e-01, 1.788651e-01, 6.029694e-04, -3.922424e-04, -5.382460e-02]])

# om = np.array([0.01911, 0.03125, -0.00960]) # 旋转关系向量
# R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
# print(R)
R2 = np.array([[9.993513e-01, 1.860866e-02, -3.083487e-02],
                           [-1.887662e-02, 9.997863e-01, -8.421873e-03],
                           [3.067156e-02, 8.998467e-03, 9.994890e-01]])
R3 = np.array([[9.993513e-01, 1.860866e-02, -3.083487e-02],
                           [-1.887662e-02, 9.997863e-01, -8.421873e-03],
                           [3.067156e-02, 8.998467e-03, 9.994890e-01]])
# R = np.array([[9.993513e-01, 1.860866e-02, -3.083487e-02],
#                            [-1.887662e-02, 9.997863e-01, -8.421873e-03],
#                            [3.067156e-02, 8.998467e-03, 9.994890e-01]])
R = np.multiply(np.linalg.inv(R2), R3)

T2 = np.array([-5.370000e-01, 4.822061e-03, -1.252488e-02])
T3 = np.array([-5.370000e-01, 4.822061e-03, -1.252488e-02])
T = T2 - T3 # 平移关系向量

size = (1392, 512) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)
print(left_map1,left_map2,right_map1,right_map2)
