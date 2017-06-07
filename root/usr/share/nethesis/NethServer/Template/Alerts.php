<?php

echo $view->header('Alerts')->setAttribute('template', $T('Alerts_header'));

echo $view->buttonList($view::BUTTON_HELP)
    ->insert($view->button('Update_Alerts', $view::BUTTON_SUBMIT));
