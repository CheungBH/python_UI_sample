import os
import random


class VideoSelector:
    def __init__(self, video_folder):
        self.video_folder = video_folder
        # self.algo_ls = [algo for algo in os.listdir(video_folder) if "DS_Store" not in algo]
        self.video_ls = [video for video in os.listdir(video_folder + "/video1") if "DS_Store" not in video]
        self.video_len = len(self.video_ls)
        self.video_index = 0

    def select(self):
        video_idx = self.video_index
        #video_idx = random.randint(0, self.video_len)
        #import pdb; pdb.set_trace()
        if video_idx >= self.video_len:
             return "", ""
            
        # algo1, algo2 = random.sample(self.algo_len, 2)
        # if  random.randint(0, 10) > 5:
        #     video_path2 = os.path.join('tcl-ours_full-blend_vdm_pcd_shuffle_f3_i1_t2_w50_occu_warpedge_edge0_blur0_relation11_mixup', self.video_ls[video_idx])
        #     video_path1 = os.path.join(self.video_folder, self.algo_ls[algo2], self.video_ls[video_idx])
        # else:
        #     video_path1 = os.path.join('tcl-ours_full-blend_vdm_pcd_shuffle_f3_i1_t2_w50_occu_warpedge_edge0_blur0_relation11_mixup', self.video_ls[video_idx])
        #     video_path2 = os.path.join(self.video_folder, self.algo_ls[algo2], self.video_ls[video_idx])
        video_path1 = os.path.join('videos/video1', self.video_ls[video_idx])
        video_path2 = os.path.join("videos/video2", self.video_ls[video_idx])
        print("Selected video:\n {}\n {}\n\n".format(video_path1, video_path2))
        self.video_index += 1
        return video_path1, video_path2




