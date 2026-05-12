<?php
function checknums(int $num1, int $num2){
    if ($num1 == $num2) return '-1';
    if ($num2>$num1)return 'true';
    return 'false';
}

echo checknums(1,6)."\n";