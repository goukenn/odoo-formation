<?php
function poweroftwo(int $num):string{
    while(($num>=2) && (($num %2) ==0)){
        $num = floor($num/2);
    }
    return $num == 1? 'true':'false';
}

echo poweroftwo(22)."\n";
// echo poweroftwo(16)."\n";
// echo poweroftwo(256)."\n";
// echo poweroftwo(66)."\n";
// echo poweroftwo(7)."\n";