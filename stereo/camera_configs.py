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
R2 = np.array([[9.998817e-01, 1.511453e-02, -2.841595e-03],
                           [-1.511724e-02, 9.998853e-01, -9.338510e-04],
                           [2.827154e-03, 9.766976e-04, 9.999955e-01]])
R3 = np.array([[9.995599e-01, 1.699522e-02, -2.431313e-02],
                           [-1.704422e-02, 9.998531e-01, -1.809756e-03],
                           [2.427880e-02, 2.223358e-03, 9.997028e-01]])
# R = np.array([[9.993513e-01, 1.860866e-02, -3.083487e-02],
#                            [-1.887662e-02, 9.997863e-01, -8.421873e-03],
#                            [3.067156e-02, 8.998467e-03, 9.994890e-01]])
R = np.multiply(np.linalg.inv(R2), R3)

T2 = np.array([5.956621e-02, 2.900141e-04, 2.577209e-03])
T3 = np.array([-4.731050e-01, 5.551470e-03, -5.250882e-03])
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
