import numpy as np
from .. import affine
import os
from numpy.testing import assert_array_equal
import nibabel as nib

basepath = os.path.abspath(os.path.dirname(__file__))

realpath = os.path.join(basepath, "..", "..", "..", "data", "ds105")
realpath = os.path.join(realpath, "sub001", "model", "model001")
realpath = os.path.join(realpath, "task001_run001.feat", "filtered_func_data_mni.nii.gz")
dummypath = os.path.join(basepath, "testsub001run001.nii.gz")

# The two tests below are used only when the data is in the
# appropriate place. It will be commented out so that the 
# Travis CI build passes. For Travis CI purposes, the last 
# two tests run with some dummy tests on a small subset of the
# data.

# def test_voxels_to_mm_real():
# 	img = nib.load(realpath)
# 	xyarray = np.array([[100, 150],
# 				 [130, 145],
# 				 [95, 99]])
# 	z = 100
# 	x = affine.voxels_to_mm(img, xyarray, z)
# 	expected = [np.array([-110, 174, 128]),
# 				np.array([-170, 164, 128]),
# 				np.array([-100, 72, 128])]
# 	assert_array_equal(expected, x)

# def test_mm_to_voxels_real():
# 	img = nib.load(realpath)
# 	xyarray = np.array([[100, 150],
# 				 [130, 145],
# 				 [95, 99]])
# 	z = 100
# 	x = affine.voxels_to_mm(img, xyarray, z)	
# 	y = affine.mm_to_voxels(img, x)
# 	expected = [np.array([100, 150, 100]),
# 				np.array([130, 145, 100]),
# 				np.array([95, 99, 100])]
# 	assert_array_equal(expected, y)



def test_voxels_to_mm_dummy():
	img = nib.load(dummypath)
	xyarray = np.array([[1, 2], [3, 4], [5, 6]])
	z = 100
	x = affine.voxels_to_mm(img, xyarray, z)
	expected = [np.array([1, 2, 100]),
				np.array([3, 4, 100]),
				np.array([5, 6, 100])]
	assert_array_equal(expected, x)


def test_mm_to_voxels_dummy():
	img = nib.load(dummypath)
	xyarray = np.array([[1, 2], [3, 4], [5, 6]])
	z = 100
	x = affine.voxels_to_mm(img, xyarray, z)
	y = affine.mm_to_voxels(img, x)
	expected = [np.array([1, 2, 100]),
				np.array([3, 4, 100]),
				np.array([5, 6, 100])]
	assert_array_equal(expected, y)
