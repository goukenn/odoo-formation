<?php
function simplesymbol(string $str){
    $arr = str_split($str);
    $ln = count($arr);
    $check = !preg_match('/[a-z]/i', $arr[0]) && !preg_match('/[a-z]/i', $arr[$ln-1]);
    for ($i = 1; $check && ($i < $ln-1); $i++){
        if (preg_match('/[a-z]/i', $arr[$i])){
            $prev = $arr[$i-1];
            $next = $arr[$i+1];
            $check = $check && ($prev == $next) && ($prev == '+');
        }
    }
    return $check ? 'true' : 'false';

}

echo simplesymbol("++d+===+c++==a")."\n";
echo simplesymbol("+d+=3=+s+")."\n";
echo simplesymbol("f++d+")."\n";