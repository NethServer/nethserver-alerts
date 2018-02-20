<?php

echo $view->header('header')->setAttribute('template', $T('Alerts_header',array($view['Url'])));

echo "<div style='float: right'>".$T('last_update_label').": ".$view['updated']."</div>";
echo "<div style='font-size: 120%; margin: 10px; padding: 10px'>".$T('Intro_label',array($view['Url']))."</div>";
echo "<div style='font-size: 120%; margin: 10px; padding: 10px'>".$T('Download_label',array($view['Url']))."</div>";

require __DIR__ . '/../../Nethgui/Template/Table/Read.php';
