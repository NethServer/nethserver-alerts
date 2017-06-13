<?php

echo $view->header('Alerts')->setAttribute('template', $T('Alerts_header'));

echo "<div style='float: right'>".$T('last_update_label').": ".$view['updated']."</div>";

require __DIR__ . '/../../Nethgui/Template/Table/Read.php';
