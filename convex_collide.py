import numpy as np
import math
import cv2


def dist(p1,p2):

    return np.linalg.norm(p1 - p2)




def full_rotate(points,angle):
    points = points.transpose()

    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    rot = np.array(((c, -s), (s, c)))

    pts_r = np.dot(rot, points)
    return pts_r.transpose().astype(int)





def collide(pts1,pts2):
    
    
    for i in range(-1,len(pts1)-1):
        p1 = pts1[i]
        p2 = pts1[i+1]

        theta = 1.57079 - np.arctan2(p2[1]-p1[1],p2[0]-p1[0])
        c, s = np.cos(theta), np.sin(theta)
        rot = np.array(((c, -s), (s, c)))
        ###################################
        rpts1 = np.dot(rot, pts1.transpose()).transpose()
        rpts2 = np.dot(rot, pts2.transpose()).transpose()
        ###################################
        ma = np.min(rpts1[:,0])
        Ma = np.max(rpts1[:,0])
        mb = np.min(rpts2[:,0])
        Mb = np.max(rpts2[:,0])
        f = (Mb-ma)*(Ma-mb)
        if f < 0:
            return False

    for i in range(-1,len(pts2)-1):
        p1 = pts2[i]
        p2 = pts2[i+1]

        theta = 1.57079 - np.arctan2(p2[1]-p1[1],p2[0]-p1[0])
        c, s = np.cos(theta), np.sin(theta)
        rot = np.array(((c, -s), (s, c)))
        ###################################
        rpts1 = np.dot(rot, pts1.transpose()).transpose()
        rpts2 = np.dot(rot, pts2.transpose()).transpose()
        ###################################
        ma = np.min(rpts1[:,0])
        Ma = np.max(rpts1[:,0])
        mb = np.min(rpts2[:,0])
        Mb = np.max(rpts2[:,0])
        f = (Mb-ma)*(Ma-mb)
        if f < 0:
            return False  
    return True              
    


