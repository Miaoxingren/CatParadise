
# -*- coding: utf-8 -*-
#File processing

import os.path
import os


def getimages(name, dir_name=""):
    '''get user information from user.txt'''
    all_img = os.listdir(os.path.join(os.path.dirname(__file__), "static", "images", dir_name))
    imgs = []
    for cur_img in all_img:
        if name in cur_img:
            imgs.append(cur_img)
    return imgs


def getbodyareas():
    '''write user information to user.txt'''
    txt = open(os.path.join(os.path.dirname(__file__), "static/txt/bodyareas.txt"), 'r')
    info = txt.readlines()
    txt.close()
    key = ['url', 'coordinate']
    bodyareas = []
    for line in info:
        if line.find('/') == -1:
            continue
        line = line.rstrip(os.linesep).split('/')
        line[0] = '/soma/'+line[0]
        bodyareas.append(dict(zip(key, line)))
    return bodyareas


def gethotcats():
    '''get hotcats from hotcats.txt'''
    txt = open(os.path.join(os.path.dirname(__file__), "static/txt/hotcats.txt"), 'r')
    info = txt.readlines()
    txt.close()
    key = ['pic', 'name', 'detail', 'link']
    hotcats = []
    for line in info:
        if line.find('$') == -1:
            continue
        line = line.rstrip(os.linesep).split('$')
        line[0] = 'hotcat'+line[0]+'.jpg'
        hotcats.append(dict(zip(key, line)))
    return hotcats


def getbook(name):
    '''book info'''
    txt = open(os.path.join(os.path.dirname(__file__), "static/txt/books.txt"), 'r')
    info = txt.readlines()
    txt.close()
    key = ['img', 'title', 'star', 'detail', 'link']
    for line in info:
        if line.find('$') == -1:
            continue
        line = line.rstrip(os.linesep).split('$')
        if name in line[0]:
            line[0] = line[0]+'.jpg'
            line[2] = int(line[2])
            book = dict(zip(key, line))
            break
    return book

