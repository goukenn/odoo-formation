<?php
function numberaddition(string $str)
{
    $r = '';
    $c = 0;
    foreach (str_split($str, 1) as $s) {
        if (is_numeric($s)) {
            $r .= $s;
        } else {
            if ($r) {
                $c += intval($r);
                $r = '';
            }
        }
    }
    if ($r)
        $c += intval($r);
    return $c;
}

echo numberaddition("55dejou5")."\n";
echo numberaddition("5dejou5")."\n";