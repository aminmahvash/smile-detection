import kagglehub, shutil
path = kagglehub.dataset_download("talhasar/genki4k")
shutil.copytree(path, "data/raw", dirs_exist_ok=True)
print("saved to data/raw")
