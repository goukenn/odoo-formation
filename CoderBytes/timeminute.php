<?php


function timeminutes(string $str){    
    $tab = explode('-', $str, 2);
    list($h1, $h2) = array_map(function($a){
        $t = substr($a,-2);
        list($h, $m) = array_map('intval', explode(':', substr($a, 0,-2)));
        $l = 0;
        $mid = ($h==12);
        if ($t=='pm'){
            if (!$mid)
                $l= 12;
        } elseif($mid){            
            $l=-12;            
        }     
        return ((intval($h) + $l) * 60) + intval($m); 
    }, $tab);
    $T = $h2 - $h1;
    if ($T<0){
        $T+=(24 *60);
    }
    return $T;
}


foreach([
    '2:00am-1:00am'=>1440-60,
    '9:00am-10:00am'=>60,
    '11:00am-1:00pm'=>120,
    '12:00am-01:00am'=>60,
    '1:00pm-11:00am'=>1320,
    '12:30am-1:00am'=>30
]as $str=>$v){
    $p = timeminutes($str);
    echo sprintf('%s : %s %-15s', $str, $p, $p==$v? 'ok':'bad'). "\n";
}
