<?php
function vowelcount(string $str){
    return preg_match_all("/[aeiou]/i", $str);
}

echo vowelcount('hello')."\n";