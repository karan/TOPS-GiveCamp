'use strict';

/* Controllers */

var phonecatApp = angular.module('phonecatApp', []);

phonecatApp.controller('PhoneListCtrl', ['$scope', '$http'],
	function PhoneListCtrl($scope) {
			alert('here');
			$http.get('../svc.json').success(function(data) {
				alert(data);
				$scope.phones = data;
		});
/*
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
*/
});
/*
    var phonecatControllers = angular.module('phonecatControllers', []);
 
    phonecatControllers.controller('PhoneListCtrl', ['$scope', '$http',
		function PhoneListCtrl($scope, $http) {
			$http.get('../svc.json').success(function(data) {
			$scope.phones = data;
		});
    }]);
     
    phonecatControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams',
		function($scope, $routeParams) {
		$scope.phoneId = $routeParams.phoneId;
    }]);
*/
