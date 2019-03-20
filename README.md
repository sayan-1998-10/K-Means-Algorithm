# K-Means-Algorithm

This is the implementation of Andrew Ng's first exercise of K-means in Week 8.In this assignment, the main task was to cluster the different 
data points into 3 clusters following the K-means algorithm.

K-means Algorithm

-->Shuffle the  dataset and pick the intital cluster centers randomly.

-->Centroid assignment-step:
      i)Calculate the minimum Euclidean distance between the datapoints and the intital cluster-centers.
      ii)Assign each datapoint to a cluster based on that minimum distance.
      
-->Move the Centroid/Cluster-Center:
      i)Find out the Mean of the data points assigned to each cluster
      ii)Then that mean will be the new cluster center
      <DO THIS FOR EACH CLUSTER>.
      
-->Repeat the previous two steps for some iterations until the cost reduces.

K-means is a cheap algorithm.So it does not matter whether one is using 10 or 1000 iterations. It does not require a lot of computational
power.

In the K-means.png file, the BLACK stars shows the intial positions of the cluster-centers.The RED stars shows the final position after 
iterations.

      
