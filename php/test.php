<?php

$name = "Sha nta u";
$new = "";
for($i = 0; $i < strlen($name); $i++) {
	if ($name[$i] == " ") {
		$new = $new . "_";
	}
	else {
		$new = $new . $name[$i];
	}
}
echo $new . "\n"

?>
