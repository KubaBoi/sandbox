#!/bin/bash
config="./config"
i_path="/usr/bin/"

while IFS= read -r line
do
	IFS="." read -ra name <<< "$line"
	echo "Installing $line as $i_path${name[0]} link"
	ln "$line" "$i_path${name[0]}"
done < "$config"
