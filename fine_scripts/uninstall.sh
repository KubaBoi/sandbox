#!/bin/bash
config="./config"
i_path="/usr/bin/"

while IFS= read -r line
do
	IFS="." read -ra name <<< "$line"
	if [ -f "$i_path${name[0]}" ]
	then
		echo "Removing $i_path${name[0]}"
		rm "$i_path${name[0]}"
	else
		echo "$i_path${name[0]} not found"
	fi
done < "$config"
