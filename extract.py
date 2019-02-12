import os,zipfile,json,sys
path=sys.argv[1]

for file_name in os.listdir(path): 
    if file_name.endswith(".lqm"):
        abs_file_path = os.path.join(path, file_name)

        parent_path = os.path.split(abs_file_path)[0]
        output_folder_name = os.path.splitext(abs_file_path)[0]
        output_path = os.path.join(parent_path, output_folder_name)

        zip_obj = zipfile.ZipFile(abs_file_path, 'r')
        zip_obj.extractall(output_path)
        zip_obj.close()
        print('#####        '+file_name+'          #####')
        print('Text:')
        print(json.load(open( output_path+'/memoinfo.jlqm') )['MemoObjectList'][0]['DescRaw'])  
        print('')
        print('')
