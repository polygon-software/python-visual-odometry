import numpy as np
from scipy.spatial.distance import cdist
def task(h, patch_radius, left_img, right_img, height, width, min_disparity, max_disparity):
    arr = []
    for w in range(patch_radius+max_disparity,width-patch_radius-1):
        # MANUAL disparity
        """
        distance = float("inf")
        disparity = 0
        for x in range(w,max(patch_radius+1,w-max_disparity),-1):
            disp = w-x;
            patch_left = left_img[h - patch_radius : h + patch_radius, w - patch_radius : w + patch_radius].reshape(-1);
            patch_right = right_img[h - patch_radius : h + patch_radius, x - patch_radius : x + patch_radius].reshape(-1);
            d = cdist([patch_left], [patch_right], 'sqeuclidean');
            
            if (d < distance):
                disparity = disp;
                distance = d;
            # set disparity outside of disparity range to 0  
        """
        # Vectorized
        
        patch_left = left_img[h - patch_radius : h + patch_radius, w - patch_radius : w + patch_radius].reshape(-1);
        vec_r = []
        for x in range(w,max(patch_radius+1,w-max_disparity),-1):
            # get patched and make them 1-d
            patch_right = right_img[h - patch_radius : h + patch_radius, x - patch_radius : x + patch_radius].reshape(-1);
            vec_r.append(patch_right)
        #print(vec_r.shape)

        pdist = cdist([patch_left], vec_r, 'sqeuclidean')
        arg_min = np.argmin(pdist)
        print("arg_min", arg_min)

        disparity = arg_min
        
        if (disparity < min_disparity or disparity > max_disparity):
            disparity = 0;
        print(disparity)
        arr.append([h, w, disparity])
    return arr
