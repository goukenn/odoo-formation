<?php
function alphabetsoup(string $str){
    $tab = array_map('ord', str_split($str));
    sort($tab);
    return implode('', array_map('chr', $tab));
}

echo 'alphabesoup : '.alphabetsoup('hello')."\n";
