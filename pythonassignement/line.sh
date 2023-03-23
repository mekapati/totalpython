#/bin/bash

array=(3 2 1 5 6)

for (( i = 0 ; i < $((${#array[@]}-1)) ; i++ )); do
if [ $((${array[$i]}+1)) -ne ${array[$(($i + 1 ))]} ] ;then
     M_NUMBER="$((${array[$i]}+1))"
     break
fi
done

echo $M_NUMBER






