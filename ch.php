<?php
echo "label1";
$client = new \ClickHouse\Client('http://192.168.122.140', 8123);

$isLive = $client->ping();

if (false === $isLive) {	  echo 'сервер запустили?';	}

echo "label2";
?>
