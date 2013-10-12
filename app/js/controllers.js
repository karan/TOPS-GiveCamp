'use strict';

/* Controllers */

var phonecatApp = angular.module('phonecatApp', []);

phonecatApp.controller('PhoneListCtrl', function PhoneListCtrl($scope) {
  $scope.phones = [
    {'name': 'Nexus S',
     'snippet': 'Fast just got faster with Nexus S.',
	 'community': 'Seattle'
	},
    {'name': '(Fake Seattle) Motorola XOOM™ with Wi-Fi',
     'snippet': 'The Next, Next Generation tablet.',
	 'community': 'Vashon'},
    {'name': 'MOTOROLA XOOM™',
     'snippet': 'The Next, Next Generation tablet.',
	 'community': 'Eastside'},
    {'name': 'XOOM™',
     'snippet': 'The Next, Next Generation tablet.',
	 'community': 'Other'}
  ];
});
