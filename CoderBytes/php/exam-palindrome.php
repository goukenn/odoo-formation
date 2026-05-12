<?php
function palindrome(string $str){
    $g = str_split($str,1);    
    $t = array_reverse($g);
    return $g == $t ? 'true' : 'false';
}

echo palindrome('racecar')."\n";