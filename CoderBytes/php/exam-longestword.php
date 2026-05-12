<?php
function longestword(string $str){
    $wordCount = 0;
    $word = '';
    foreach(explode(" ", $str) as $c){
        if (preg_match("/^[a-zA-Z0-9]+$/",$c)){
            $wlen = strlen($c);
            if ($wlen >$wordCount){
                $wordCount = $wlen;
                $word = $c; 
            }
        }
    }
    return $word;
}


echo longestword("fun!!& time")."\n";  // time
echo longestword("I love dogs")."\n";  // love