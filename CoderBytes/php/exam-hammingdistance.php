<?php


function hammingDistance(array $strArr){
    $ln = count($strArr);
    if ($ln!=2) die('invalid arg');
    $sln = strlen($strArr[0]);
    for($i=0; $i < $sln; $i++){
        if ($strArr[0][$i] != $strArr[1][$i]){
            return $sln-$i;
        }
    }
    return 0;
}


echo hammingDistance(["coder","codec"]). "\n";
echo hammingDistance(["10011","10100"]). "\n";