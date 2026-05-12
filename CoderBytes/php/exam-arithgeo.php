<?php
function arithgeo(array $arr){
    $arith = $geo = true;
    for ($i = 1; $i < count($arr)-1; $i++){
        $arith = $arith && (($arr[$i]-$arr[$i-1]) == ($arr[$i+1]-$arr[$i]));
        $geo = $geo && (($arr[$i]/$arr[$i-1]) == ($arr[$i+1]/$arr[$i]));
    }
    if ($geo)return 'geometric';
    if ($arith)return 'arithmetric';
    return -1;
}

echo arithgeo([2,4,6,8,10])."\n";
echo arithgeo([2,6,18])."\n";
echo arithgeo([2,6,18,5])."\n";
