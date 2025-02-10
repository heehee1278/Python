file_names=["file1.py","file2.txt","file3.pptx","file4.doc"]
for file_names in file_names:
    arr=file_names.split(".")
    # print(arr)
    print("%s==> 파일명:%s,확장자:.%s"%(file_names,arr[0],arr[1]))