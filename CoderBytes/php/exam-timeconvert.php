<?php
function timeconvert(int $time){
    $h = floor($time / 60);
    $min = $time % 60;

    return implode(':', [$h,$min]);
}

echo timeconvert(63)."\n";

