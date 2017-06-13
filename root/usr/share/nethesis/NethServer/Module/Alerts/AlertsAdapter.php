<?php
namespace NethServer\Module\Alerts;

/*
 * Copyright (C) 2017 Nethesis Srl
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * Alerts table adapter
 *
 */
class AlertsAdapter extends \Nethgui\Adapter\LazyLoaderAdapter
{
    /**
     *
     * @var \Nethgui\System\PlatformInterface
     */
    private $platform;

    public function __construct(\Nethgui\System\PlatformInterface $platform)
    {
        $this->platform = $platform;
        parent::__construct(array($this, 'readAlerts'));
    }

    public function flush()
    {
        $this->data = NULL;
        return $this;
    }

    public function readAlerts()
    {
        $alerts = array();

        $adb = $this->platform->getDatabase('alerts');
        $data = new \ArrayObject();

        foreach ($adb->getAll() as $key => $alert) {
            $instance = '-';
            $type = '-';
            $threshold = '-';
            if (isset($alert['PluginType'])) {
                $type = $alert['PluginType'];
            } else {
                $type = $alert['type'];
            }

            if (isset($alert['Instance'])) {
               $instance = $alert['Instance'];
            } else if (isset($alert['TypeInstance'])) {
               $instance = $alert['TypeInstance'];
            }

            $row = array(
                'Type' => $type,
                'Instance' => $instance,
                'Threshold' => $threshold,
                'FailureMax' => isset($alert['FailureMax']) ? $alert['FailureMax'] : '-',
                'FailureMin' => isset($alert['FailureMin']) ? $alert['FailureMin'] : '-',
                'WarningMax' => isset($alert['WarningMax']) ? $alert['WarningMax'] : '-',
                'WarningMin' => isset($alert['WarningMin']) ? $alert['WarningMin'] : '-',
            );

            $data[$key] = $row;
        }

        return $data;
    }


}
