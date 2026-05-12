<?php
function lettercapitalize(string $str){
    return implode(' ', array_map('ucfirst', explode(' ', strtolower($str))));
}


echo lettercapitalize('hello my friend')."\n";