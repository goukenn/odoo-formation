<?php
function swapcase(string $str):string{
    return implode('', array_map(function($a){
        return preg_match('/[a-z]/', $a)? strtoupper($a) : strtolower($a);
    }, str_split($str)));
}


echo swapcase('hEllo DaDy')."\n";