#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

#####################################
#       切换gitconfig 配置
#####################################


# 获取当前用户工作目录
# for linux : home_path = os.path.expandvars('$HOME')
home_path = os.path.expandvars('%USERPROFILE%')

print('[HOME_PATH: %s]' % home_path)
# 当前git配置
current_git = '.gitconfig'
# 公司git配置
office_git_path = '.gitconfig.office'
# 自用git配置
home_git_path = '.gitconfig.home'


# 判断当前配置
def witch_git_now():
    with open(home_path + os.sep + current_git, 'r') as f:
        for line in f:
            if line.find('melodyfff') != -1:
                print("current git config is : [%s] , change to [%s]" % (home_git_path, office_git_path))
                return office_git_path
        print("current git config is : [%s] , change to [%s]" % (office_git_path, home_git_path))
        return home_git_path


def change_git(file_name):
    with open(home_path + os.sep + current_git, 'w+') as file_open:
        with open(home_path + os.sep + file_name, 'r') as file_new:
            for line in file_new:
                file_open.write(line)
    print("current git config is : [%s]" % file_name)


# 切换配置
change_git(witch_git_now())
