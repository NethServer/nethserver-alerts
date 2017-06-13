<?php

echo $view->header()->setAttribute('template', $T('Alerts_Configure_header'));

echo $view->panel()
         ->insert($view->radioButton('AlertsAutoUpdates', 'enabled'))
         ->insert($view->radioButton('AlertsAutoUpdates', 'disabled'))

;

echo $view->buttonList($view::BUTTON_SUBMIT);
