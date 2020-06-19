import numpy as np
import pca as pca
import matplotlib.pyplot as plt
import compress as c

TRAINING_DATA = "C:/Users/suagrawa/source/Pytorch-DeepLearning/data/PCA/Train"
TEST_DATA = "C:/Users/suagrawa/source/Pytorch-DeepLearning/data/PCA/Test/"

X = c.load_data(TRAINING_DATA)
x = np.array(X)
"""
Shape of the image is 60*48
"""
print(x[1,0].shape)

faces = []
filenames = []
for face in X:
    filenames.append(face[1])
    faces.append(face[2])
# we convert each image to a feature (column)
faces = np.asarray(faces)
faces = np.transpose(faces)
# pca processes
# Standardize the values. Subtract the mean and divide by standard deviation

Z = pca.compute_Z(faces)

COV = pca.compute_covariance_matrix(Z)

L, PCS = pca.find_pcs(COV)
Z_star = pca.project_data(Z, PCS, L, k, 0)
# we use components for compressing files, we need to reduce component count
component_matrix = np.delete(PCS, range(k, PCS.shape[1]), axis=1)
Ut = component_matrix.T
X_compressed = np.dot(Z_star, Ut)
# write all images
for ftr_ind in range(faces.shape[1]):
    # we need to reshape the feature as image.
    img = np.reshape(X_compressed[:,ftr_ind], (60, 48))
    plt.imsave("Output" + "/" + filenames[ftr_ind] + "_img.jpg", img, cmap="gray")
print()

c.compress_images(X, 100)


