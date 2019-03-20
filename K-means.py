""" K-means clustering """
import numpy as np
import scipy.io as sio
from matplotlib import pyplot as plt 
import matplotlib


x_centroid1 = np.zeros((300,1))
x_centroid2 = np.zeros((300,1))
x_centroid3 = np.zeros((300,1))
c = np.zeros((300,1))

def assign_centroid(X,centroids):
   

    for i in range(len(X)):
        #calculate the L2 norm
        dist_cent1 = ( (X[i][1]-centroids[0][1])**2+(X[i][0]-centroids[0][0])**2)
        dist_cent2 = ( (X[i][1]-centroids[1][1])**2+(X[i][0]-centroids[1][0])**2)
        dist_cent3 = ( (X[i][1]-centroids[2][1])**2+(X[i][0]-centroids[2][0])**2)
        
        minimum = min(dist_cent1,dist_cent2,dist_cent3)
        if (minimum == dist_cent1):
            c[i] = 1
            
        elif (minimum == dist_cent2):
            c[i] = 2
            
        else:
            c[i] = 3
            
    
    return c
        
def position_ofCentroid(X,c):
    for i in range(len(c)):
        if  (c[i]==1):
            x_centroid1[i] = i
        elif (c[i]==2):
            x_centroid2[i] = i
        else:
            x_centroid3[i]= i
            
   
    new_centroidPosition = np.zeros((3,2))
    
    cluster1_points=(x_centroid1[x_centroid1!=0])
    cluster2_points=(x_centroid2[x_centroid2!=0])
    cluster3_points=(x_centroid3[x_centroid3!=0])
    
    #calc the average
    new_pos1=np.array([0.0,0.0])
    new_pos2=np.array([0.0,0.0])
    new_pos3=np.array([0.0,0.0])
    for i in range(len(cluster1_points)):
        new_pos1+=X[int(cluster1_points[i])]
        
    for i in range(len(cluster2_points)):
        new_pos2+=X[int(cluster2_points[i])]
        
    for i in range(len(cluster3_points)):
        new_pos3+=X[int(cluster3_points[i])]
    
    new_pos1 = new_pos1/len(cluster1_points)
    new_pos2 = new_pos2/len(cluster2_points)
    new_pos3 = new_pos3/len(cluster3_points)
    
    new_centroidPosition[0] = new_pos1
    new_centroidPosition[1] = new_pos2
    new_centroidPosition[2] = new_pos3
    
#    print(new_centroidPosition)
    return new_centroidPosition    

def init_Centroid(X):
    randindx = np.random.permutation(300)
    centroids = X[randindx[0:3],:]
    return centroids
def plot(X,c,centroids):
#    print(c)
    plt.scatter(X[:,0],X[:,1],c=c[:].ravel(),cmap='viridis',s=100*np.random.rand(10),alpha=0.3)
    plt.scatter(centroids[:,0],centroids[:,1],c='red',s=300,alpha=1,marker='*')
    
        
def main():
    data=sio.loadmat("C:/Users/europ/Desktop/ML_FOLDER/machine-learning-ex7/ex7/ex7data2.mat")
    X = data['X'].flatten().reshape(300,2)
    centroids = init_Centroid(X)
    plt.scatter(centroids[:,0],centroids[:,1],c="black",s=300*np.random.rand(10),alpha=0.9,marker='*')
    for i in range(700):

        c=assign_centroid(X,centroids)
        
        centroids=position_ofCentroid(X,c)
        

    plot(X,c,centroids)
    
if __name__== '__main__':
    main()