<?php
function secondgreatlow(array $arr){
    sort($arr);
    $arr= array_values(array_unique($arr));
    $c = count($arr);
    if (2 == $c){
        return implode(' ', [$arr[1], $arr[0]]);
    }
    return implode(' ', [$arr[1], $arr[$c-2]]);
}
echo secondgreatlow([7,7,12,98,106])."\n";