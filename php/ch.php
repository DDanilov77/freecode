<?php
// if check
echo "metka label 1";

$client = new \ClickHouse\Client('http://192.168.11.140', 8123);

$isLive = $client->ping();

if (false === $isLive) {	  echo 'сервер запустили?';	}

echo "metka label 2";

?>
