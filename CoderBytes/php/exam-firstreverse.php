<?php
function firstreverse(string $str){
    $h = str_split($str);
    $h = array_reverse($h);
    return implode('', $h);
}


echo firstreverse("hello coderbyte")."\n";