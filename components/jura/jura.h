#pragma once

#include "esphome.h"
#include "esphome/core/log.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"

// For component schema definitions
#include "esphome/core/components.h"
#include "esphome/core/defines.h"

namespace esphome {
namespace jura {

class JuraComponent : public PollingComponent,
                      public uart::UARTDevice,
                      public api::CustomAPIDevice {
 public:
  JuraComponent() = default;
  void loop() override;
  float get_setup_priority() const override;
  void dump_config() override;
  void setup() override;
  void update() override;

  // Setters for each sensor
  void set_espresso_sensor(sensor::Sensor *espresso_sensor);
  void set_coffee_sensor(sensor::Sensor *coffee_sensor);
  void set_double_coffee_sensor(sensor::Sensor *double_coffee_sensor);
  void set_powder_coffee_sensor(sensor::Sensor *decaff_coffee_sensor);
  void set_water_sensor(sensor::Sensor *water_sensor);
  void set_cleaning_sensor(sensor::Sensor *cleaning_sensor);
  void set_water_filter_sensor(sensor::Sensor *water_filter_sensor);
  void set_power_sensor(sensor::Sensor *power_sensor);
  void set_rinsing_sensor(sensor::Sensor *rinsing_sensor);
  void set_tray_sensor(sensor::Sensor *tray_sensor);
  void set_water_tank_sensor(sensor::Sensor *water_tank_sensor);
  void set_coffee_ground_sensor(sensor::Sensor *coffee_ground_sensor);

  // Remote‐control services
  void on_turnoff();
  void on_press_espresso();
  void on_press_coffee();
  void on_press_hotwater();
  void on_press_flush();

 protected:
  void parse_data_();
  void send_command_(uint8_t parseMode, std::string command);
  uint16_t get_16bit_uint(uint8_t position);
  bool check_response_();
  void decode_response();

  // Raw buffers
  uint8_t data_[1024];
  uint16_t data_index_{0};
  uint8_t decoded_data_[256];
  uint16_t decoded_index_;
  uint32_t last_update_{0}, last_transmission_{0}, update_interval_{0};
  uint8_t parse_mode;

  // Sensor pointers
  sensor::Sensor *sensor_espresso{nullptr};
  sensor::Sensor *sensor_coffee{nullptr};
  sensor::Sensor *sensor_double_coffee{nullptr};
  sensor::Sensor *sensor_decaff_coffee{nullptr};
  sensor::Sensor *sensor_cleaning{nullptr};
  sensor::Sensor *sensor_filter{nullptr};
  sensor::Sensor *status_power{nullptr};
  sensor::Sensor *status_rinsing{nullptr};
  sensor::Sensor *error_tray{nullptr};
  sensor::Sensor *error_tank{nullptr};
  sensor::Sensor *error_grounds{nullptr};
};

// —— CONFIG_SCHEMA ——
// This tells ESPHome what options "jura:" can take in YAML,
// and maps each YAML key to the corresponding setter above.
static const auto JURA_SCHEMA = esphome::ComponentSchema("jura")
  .AddOptional<&JuraComponent::set_espresso_sensor>("espresso_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_coffee_sensor>("coffee_sensor",   sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_double_coffee_sensor>("double_coffee_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_powder_coffee_sensor>("decaff_coffee_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_water_sensor>("water_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_cleaning_sensor>("cleaning_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_water_filter_sensor>("water_filter_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_power_sensor>("power_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_rinsing_sensor>("rinsing_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_tray_sensor>("tray_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_water_tank_sensor>("water_tank_sensor", sensor::SensorSchema())
  .AddOptional<&JuraComponent::set_coffee_ground_sensor>("coffee_ground_sensor", sensor::SensorSchema())
  .Extend();

ESPHOME_DEFINE_COMPONENT(JuraComponent, JURA_SCHEMA);

}  // namespace jura
}  // namespace esphome
