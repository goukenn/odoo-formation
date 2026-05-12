<?php
function divisionstringified($num1, $num2){
    $a = round($num1/$num2);
    $str = ''.$a;
    $o = '';
    $ch = '';
    while(strlen($str)>0){
        $o = substr($str, -3).$ch.$o;
        $str = substr($str, 0,-3);
        $ch = ',';
    }
    return $o;

}

echo divisionstringified(123456789,10000). "\n";
echo divisionstringified(5, 2). "\n";
echo divisionstringified(6874, 67). "\n";