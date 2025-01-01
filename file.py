import os
import shutil
directory = 'D:\\aleks\\Desktop\\py'
os.chdir(directory)
# def fold():
    # a = 0
    # while a < 10:
#         a += 1
#         if os.path.isdir (f'{a}.Folder'):
#             shutil.rmtree (f'{a}.Folder')
#         else:
#             os.makedirs (f'{a}.Folder/{a}.Folder')
# fold()
# #     # print(os.chdir(os.path.join(os.getcwd(), 'Desktop', 'py')))
# #     # print(os.getcwd())
# a = 0
def inc ():
    a = 0
    while a < 10:
        a += 1
        # fold ()
        def fold ():
            if os.path.isdir (f'{a}.Folder'):
                    shutil.rmtree (f'{a}.Folder')
            else:
                os.makedirs (f'{a}.Folder/{a}.Folder')
        fold ()

# a = 0
inc()