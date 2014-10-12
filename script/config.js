var trafficControl = angular.module(
    'trafficControl',
    [
        'controllers',
        'services',
        'directives'
    ]
);

var controllers = angular.module('controllers', []);

var directives = angular.module('directives', []);

var services = angular.module('services', ['ngResource']);