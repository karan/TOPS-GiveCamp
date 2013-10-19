/* Controllers */

var emailControllers = angular.module('emailControllers', []);

emailControllers.controller('EmailListCtrl', ['$scope', '$http',
	function EmailListCtrl($scope, $http) {
		"use strict";
		var servicesFile = "uploads/servicesFile.json";
		$scope.numResults = 500;  // if this is omitted, the select input shows a blank by default

		$http.get(servicesFile).success(function(data) {
			/*alert(typeof(data))
			for (entry in data) {
				entry.Body = entry.Body.replace('Â', '');
			}*/
			$scope.offers = data;
		}).error(function(data) {
			$scope.errors = data;
			$scope.offers = {};
		});

		var convertCSV = function() {
			$http.get(servicesFile).success(function(data) {
				csvObjects = CSV.parse(data);
				jsonText = JSON.stringify(csvObjects, null, '\t');
				alert( jsonText );
			}).error(function(data) {
				$scope.errors = data;
				$scope.offers = [];
			});
		};
	}
]);

emailControllers.controller('UploadCtrl', ['$scope', '$http',
	function UploadCtrl($scope, $http) {
		"use strict";
		$scope.formData = {};
		$scope.didSubmit = false;
		$scope.url = "/upload";

		$scope.change = function() {
			//names = [ 'communityFile', 'memberFile', 'servicesFile' ];
			names = [ 'servicesFile' ];
			for (var i = 0; i < names.length; i++) {
				var name = names[i];
				var el  = document.getElementById(name);
				alert(JSON.stringify(el));
				$scope.formData[name] = JSON.parse(el);
			}
		};

		$scope.showLoading = function() {
			$scope.didSubmit = true;
			$scope.alertType = "alert-success";
			$scope.submitAlert = "Loading...";
		};

		$scope.submit = function() {
			$scope.didSubmit = true;
			$scope.alertType = "alert-success";
			//$scope.change();
			var el  = document.getElementById('servicesFile');
			$scope.formData = el;

			//$scope.formData.communityFile = 'hello';
			$scope.submitAlert = JSON.stringify($scope.formData);

			$http.post({
				url: $scope.url,
				data: $scope.formData,
				headers: {'Content-Type': 'multipart/form-data'}
			}).success(function(data) {
				$scope.didSubmit = true;
				$scope.alertType = "alert-success";
				$scope.submitAlert = data;
			}).error(function(data) {
				$scope.didSubmit = true;
				$scope.alertType = "alert-error";
				$scope.submitAlert = data;
			});
		};
	}
]);

emailControllers.controller('loginCtrl', ['$scope',
	function loginCtrl($scope) {
		$scope.testVar = "hello world";
	}
]);
