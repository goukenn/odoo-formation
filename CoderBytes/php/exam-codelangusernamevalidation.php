<?php
function codelangusernamevalidation(string $str){
    $ln = strlen($str);
    $lastIndex = $ln - 1;

    if (($ln<4) || ($ln> 25) || 
        !preg_match('/^[a-zA-Z]/', $str) || 
        !preg_match('/[0-9a-zA-Z_]/', $str) || 
        !preg_match('/[a-z]/', $str)  ||
        ($str[$lastIndex] == '_')){
        return 'false';
    }
    return 'true';
}

