#!/usr/bin/env sh
echo "initialize workspace ..."

folder_list="data model resources tmp util"
for folder_name in ${folder_list}
do
    if [ ! -d ${folder_name} ]; then
        mkdir -p ${folder_name}
    fi
done

echo "complete"