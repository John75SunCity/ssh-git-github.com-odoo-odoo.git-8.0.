odoo.define('records_management.map_widget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');
    var core = require('web.core');
    var _t = core._t;

    var MapWidget = AbstractField.extend({
        className: 'map_widget',
        _render: function () {
            // Clear previous content and add map container
            this.$el.html('<div class="map_container"></div>');

            if (!this.recordData || !this.options) {
                this.$('.map_container').html('<span>Invalid configuration: record data or options missing.</span>');
                return;
            }

            var latitude = this.recordData[this.options.latitude_field];
            var longitude = this.recordData[this.options.longitude_field];

            var hasLatitude = !!latitude;
            var hasLongitude = !!longitude;
            var hasGoogle = typeof google !== 'undefined';
            var hasGoogleMaps = hasGoogle && google.maps;

            if (hasLatitude && hasLongitude && hasGoogleMaps) {
                var map = new google.maps.Map(this.$('.map_container')[0], {
                    center: { lat: latitude, lng: longitude },
                    zoom: 15
                });
            } else if (!hasLatitude || !hasLongitude) {
                this.$('.map_container').html('<span>No location set: latitude or longitude missing.</span>');
            } else if (!hasGoogleMaps) {
                this.$('.map_container').html('<span>Google Maps API not loaded.</span>');
            }
        }
    }); // Close the MapWidget definition

    fieldRegistry.add('map_widget', MapWidget);

    return MapWidget;
}); // Close the odoo.define block
