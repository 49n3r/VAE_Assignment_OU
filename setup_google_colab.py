#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def download_file(url, file_path):
    print(url, file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
    template = "wget '{}' -O '{}'"
    os.system(template.format(url, file_path))


def download_github_code(path):
    url = 'https://raw.githubusercontent.com/49n3r/VAE_Assignment_OU/main/{}'
    file_path = path.rsplit("/")[-1]
    download_file(url.format(path), file_path)




def load_data_cVAE():
    download_github_code("debugger.py")
    download_github_code("test_data.npz")




# def load_data_FaceDetect():
#     download_github_code("utils.py")
#     download_file(
#         "https://github.com/hse-aml/bayesian-methods-for-ml/"
#         "releases/download/v0.1/CelebA_VAE_small_8.h5",
#         "CelebA_VAE_small_8.h5"
#     )
