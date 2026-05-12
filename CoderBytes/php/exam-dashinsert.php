<?php
function dashinsert(string $str):string{
    $s = '';
    $dash = '-';
    $is_odd =false;
    foreach(str_split($str) as $m){
        $v_odd = (intval($m) % 2) == 1;
        if ($v_odd && $is_odd){
            $s.=$dash;
        } 
        $is_odd = $v_odd;
        $s.=$m; 
    }  
    return $s;
}


echo dashinsert('123794')."\n";
echo dashinsert('99946')."\n";
echo dashinsert('56730')."\n";