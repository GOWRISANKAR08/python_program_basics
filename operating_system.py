import os
# print(os.getcwd()) #returns current working path
# help(os.getcwd)
path= "C:\samle_test"
folder_name = "create_folder_testing"
whole_path = os.path.join(path,folder_name) 
# os.mkdir(whole_path)
# os.mrdir(whole_path)
os.makedirs("C:\samle_test\sample1\sample2")
