<?php

function triBubbleSort(array $arr){
    $ln = count($arr);

    for ($i = 0; $i < $ln; $i++){
        $sorted  =false;
        for ($j = 0; $j < $ln-$i-1; $j++){
            if ($arr[$j]>$arr[$j+1]){
                $a = $arr[$j];
                $arr[$j] = $arr[$j+1];
                $arr[$j+1] = $a;
                $sorted = true;
            }
        }
        if (!$sorted)break;
    }
    return $arr;
}

echo json_encode(triBubbleSort([64, 34, 25, 12, 22, 11, 90])) . "\n";