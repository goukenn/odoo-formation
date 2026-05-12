<?php
function lettercount(string $str)
{
    $word = -1;
    $maxCount = 0;
    $tab = explode(' ', $str);
    while (count($tab) > 0) {
        $q = array_shift($tab);
        $c = array_fill_keys($rtab = str_split($q), 0);
        foreach ($rtab as $j) {
            $c[$j]++;
            if ($c[$j] > 1) {
                if ($c[$j] > $maxCount) {
                    $maxCount = $c[$j];
                    $word = $q;
                }
            }
        }
    }
    return $word;
}

echo "checking...." . lettercount('hello my friend apple') . "\n";
echo "checking...." . lettercount('No words') . "\n";
