<?php
function fizzbuzz(int $num){
    $t = [];
    for($i = 1; $i<=$num; $i++){
        $ch = '';
        $ch .= (($i%5)==0) ? 'fizz':'';
        $ch .= (($i%3)==0) ? 'buzz':'';
        $t[] = !empty($ch)? $ch : $i;
    }

    return implode(' ', $t);
}

echo fizzbuzz(16)."\n";
