#!/bin/sh
#Author: law

Folder_A="/Users/law/Desktop/file/opencv/pano"
for file_a in ${Folder_A}/*; do
    # 括号两端必须有空格
    if [ "${file_a##*.}" = "json" ];then
        # echo $file_a
        temp_name=`basename $file_a`
        file_name="${temp_name%.*}"
        # echo $file_name
        python3 /Users/law/Desktop/file/opencv/pano/json_to_dataset.py $file_a -o /Users/law/Desktop/file/opencv/output/${file_name}
    fi
done