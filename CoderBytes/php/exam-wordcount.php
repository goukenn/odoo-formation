<?php
function wordcount(string $str){

    return count(array_filter(explode(' ', $str)));
}

echo wordcount('hello friend')."\n";


