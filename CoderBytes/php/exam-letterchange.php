<?php
function letterchange(string $str)
{
    $s = '';
    foreach (str_split($str) as $c) {
        $ch = $c;
        if (preg_match('/[a-z]/i', $ch)) {
            if ($ch=='z')
                $ch = 'a';
            else if ($ch=='Z')
                $ch = 'A';
            else 
                $ch = chr(ord($c)+1);
            if (strpos('aeiou', $ch) !== false) {
                $ch = strtoupper($ch);
            }
        }
        $s .= $ch;
    }
    return $s;
}

echo letterchange("bonjour")."\n";
echo letterchange("hello*3")."\n";
