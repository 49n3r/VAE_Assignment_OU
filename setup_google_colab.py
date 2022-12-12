#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def download_file(url, pyCode):
    print(url, pyCode)
    if os.path.exists(pyCode):
        os.remove(pyCode)
    template = "wget '{}' -O '{}'"
    os.system(template.format(url, pyCode))


def download_github_code(pyCode):
    url = "https://raw.githubusercontent.com/49n3r/VAE_Assignment_OU/main/{}"
    download_file(url.format(pyCode), pyCode)




def load_data_cVAE():
    download_github_code("debugger.py")
    download_github_code("test_data.npz")




def load_data_FaceDetect():
    download_github_code("utils.py")
    download_file("https://catmailohio-my.sharepoint.com/:u:/g/personal/cu884120_ohio_edu/EeAaRwEvGXpClcaSxh7zjKAB1_bPDg_UiJkFPLSZB7nAqQ")
