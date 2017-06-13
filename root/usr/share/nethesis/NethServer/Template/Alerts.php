<?php

echo $view->header('Alerts')->setAttribute('template', $T('Alerts_header'));

echo "<div style='float: right'>".$T('last_update_label').": ".$view['updated']."</div>";
echo "<div style='font-size: 120%; margin: 10px; padding: 10px'>".$T('Intro_label')."</div>";
echo "<div style='font-size: 120%; margin: 10px; padding: 10px'>".$T('Download_label')."</div>";

require __DIR__ . '/../../Nethgui/Template/Table/Read.php';
