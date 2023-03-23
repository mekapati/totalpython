#/bin/bash

array=(5 2 1 3 0)

for (( i = 0 ; i < $((${#array[@]}-1)) ; i++ )); do

if [ $((${array[$i]}+1)) -ne ${array[$(($i + 1 ))]} ] ;then
    
    #if [ ${array[$(($i + 1 ))]} == "0" ] ;then
        M_NUMBER="$((${array[$i]}-1))"
        break
#fi
fi
done

echo $M_NUMBER
