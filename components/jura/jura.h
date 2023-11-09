#pragma once
#include "esphome.h"
#include "esphome/core/component.h"
#include "esphome/core/log.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"

namespace esphome
{
  namespace jura
  {

    class JuraComponent : public PollingComponent, public uart::UARTDevice, public api::CustomAPIDevice {
      public:
        JuraComponent() = default;
        void loop() override;
        float get_setup_priority() const override;
        void dump_config() override;
        void setup() override;
        void update() override;

        void set_espresso_sensor(sensor::Sensor *espresso_sensor);
        void set_coffee_sensor(sensor::Sensor *coffee_sensor);
        void set_powder_coffee_sensor(sensor::Sensor *decaff_coffee_sensor);
        void set_water_sensor(sensor::Sensor *water_sensor);
        void set_cleaning_sensor(sensor::Sensor *cleaning_sensor);
        void set_water_filter_sensor(sensor::Sensor *water_filter_sensor);
        void set_power_sensor(sensor::Sensor *power_sensor);
        void set_rinsing_sensor(sensor::Sensor *rinsing_sensor);
        void set_tray_sensor(sensor::Sensor *tray_sensor);
        void set_water_tank_sensor(sensor::Sensor *water_tank_sensor);
        void set_coffee_ground_sensor(sensor::Sensor *coffee_ground_sensor);

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

        uint8_t data_[1024];
        uint16_t data_index_{0};
        uint8_t decoded_data_[256];
        uint16_t decoded_index_;
        uint32_t last_update_{0};
        uint32_t last_transmission_{0};
        uint32_t update_interval_{0};
        uint8_t parse_mode;

        // "Brews"
        sensor::Sensor *sensor_espresso{nullptr};
        sensor::Sensor *sensor_coffee{nullptr};
        sensor::Sensor *sensor_double_coffee{nullptr};
        sensor::Sensor *sensor_decaff_coffee{nullptr};

        // Cleaning routines
        sensor::Sensor *sensor_cleaning{nullptr};
        sensor::Sensor *sensor_filter{nullptr};

        sensor::Sensor *status_power{nullptr};
        sensor::Sensor *status_rinsing{nullptr};
        sensor::Sensor *error_tray{nullptr};
        sensor::Sensor *error_tank{nullptr};
        sensor::Sensor *error_grounds{nullptr};
    };
  }
}