import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart

from esphome.const import (
    CONF_POWER,
    CONF_ID,
    CONF_UPDATE_INTERVAL,
    CONF_TYPE,
    ICON_COUNTER,
    UNIT_EMPTY,
    DEVICE_CLASS_PROBLEM,
    DEVICE_CLASS_EMPTY,
    STATE_CLASS_TOTAL_INCREASING,
    STATE_CLASS_NONE,
)

DEPENDENCIES = ["uart"]

jura_ns = cg.esphome_ns.namespace("jura")
JuraComponent = jura_ns.class_("JuraComponent", uart.UARTDevice, cg.Component)

CONF_ESPRESSO = "espresso"
CONF_COFFEE = "coffee"
CONF_DOUBLE_COFFEE = "double_coffee"
CONF_DECAFF_COFFEE = "decaff_coffee"
CONF_WATER = "water"
CONF_CLEANING = "cleaning"
CONF_WATER_FILTER = "water_filter"
CONF_RINSING = "rinsing"
CONF_TRAY = "tray"
CONF_WATER_TANK = "water_tank"
CONF_COFFEE_GROUND = "coffee_ground"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(JuraComponent),
            cv.Optional(CONF_ESPRESSO): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_COFFEE): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_DOUBLE_COFFEE): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_DECAFF_COFFEE): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_WATER): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_CLEANING): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_WATER_FILTER): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_POWER): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_PROBLEM,
                state_class=STATE_CLASS_NONE,
            ),
            cv.Optional(CONF_RINSING): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_PROBLEM,
                state_class=STATE_CLASS_NONE,
            ),
            cv.Optional(CONF_TRAY): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_PROBLEM,
                state_class=STATE_CLASS_NONE,
            ),
            cv.Optional(CONF_WATER_TANK): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_PROBLEM,
                state_class=STATE_CLASS_NONE,
            ),
            cv.Optional(CONF_COFFEE_GROUND): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_COUNTER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_PROBLEM,
                state_class=STATE_CLASS_NONE,
            ),
            cv.Optional(CONF_UPDATE_INTERVAL, default="60s"): cv.update_interval,
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_ESPRESSO in config:
        sens = await sensor.new_sensor(config[CONF_ESPRESSO])
        cg.add(var.set_espresso_sensor(sens))

    if CONF_COFFEE in config:
        sens = await sensor.new_sensor(config[CONF_COFFEE])
        cg.add(var.set_coffee_sensor(sens))

    if CONF_DOUBLE_COFFEE in config:
        sens = await sensor.new_sensor(config[CONF_DOUBLE_COFFEE])
        cg.add(var.set_double_coffee_sensor(sens))

    if CONF_DECAFF_COFFEE in config:
        sens = await sensor.new_sensor(config[CONF_DECAFF_COFFEE])
        cg.add(var.set_powder_coffee_sensor(sens))

    if CONF_WATER in config:
        sens = await sensor.new_sensor(config[CONF_WATER])
        cg.add(var.set_water_sensor(sens))

    if CONF_CLEANING in config:
        sens = await sensor.new_sensor(config[CONF_CLEANING])
        cg.add(var.set_cleaning_sensor(sens))

    if CONF_WATER_FILTER in config:
        sens = await sensor.new_sensor(config[CONF_WATER_FILTER])
        cg.add(var.set_water_filter_sensor(sens))

    if CONF_POWER in config:
        sens = await sensor.new_sensor(config[CONF_POWER])
        cg.add(var.set_power_sensor(sens))

    if CONF_RINSING in config:
        sens = await sensor.new_sensor(config[CONF_RINSING])
        cg.add(var.set_rinsing_sensor(sens))

    if CONF_TRAY in config:
        sens = await sensor.new_sensor(config[CONF_TRAY])
        cg.add(var.set_tray_sensor(sens))

    if CONF_WATER_TANK in config:
        sens = await sensor.new_sensor(config[CONF_WATER_TANK])
        cg.add(var.set_water_tank_sensor(sens))

    if CONF_COFFEE_GROUND in config:
        sens = await sensor.new_sensor(config[CONF_COFFEE_GROUND])
        cg.add(var.set_coffee_ground_sensor(sens))
