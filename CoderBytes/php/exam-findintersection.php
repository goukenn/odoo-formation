<?php
function findintersection(array $strArr): string{
    $c = [];
    list($first, $second) = $strArr;
    $first = explode(',', $first);
    $second = explode(',', $second);
    foreach($second as $k){
        if (in_array($k, $first)){
            $c[] = $k;
        }
    }
    if ($c){
        return implode(',', $c);
    }
    return 'false';
}


echo findintersection(['2,4,5,8', '4,5'])."\n";