import os

def delete_dir(dir_name="save_dir"):
    if os.path.exists(dir_name):
        print("'{}'が存在します".format(dir_name))
        os.rmdir(dir_name)
        print("'{}'を消去しました！".format(dir_name))
    else:
        print("'{}'が存在しません(T-T )".format(dir_name))

delete_dir()
