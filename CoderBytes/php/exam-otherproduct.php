<?php
function otherproduct( array $arr){
    $c = count($arr);
    if (($c<=0)||($c>10)) die('invalid arg');

    $tab = array_fill_keys(range(0, $c-1), 1);
    foreach($arr as $k=>$v){
        foreach($tab as $tc=>$m){
            if ($tc==$k)continue;
            $tab[$tc] *= $v;
        }
    }
    return implode('-', $tab);
}


echo otherproduct([1,2,3,4,5]);