
/* Controllers */

var emailControllers = angular.module('emailControllers', []);

emailControllers.controller('EmailListCtrl', ['$scope', '$http', 
	function EmailListCtrl($scope, $http) {
		$http.get('svc.json').success(function(data) {
			/*alert(typeof(data))
			for (entry in data) {
				entry.Body = entry.Body.replace('Â', '');
			}*/
			$scope.offers = data;
		}).error(function(data) {
			$scope.errors.innerHTML = "Error: " + data;
			$scope.offers = [];
		});

		var convertCSV = function() {
			$http.get('svc.csv').success(function(data) {
				csvObjects = CSV.parse(data);
				jsonText = JSON.stringify(csvObjects, null, '\t');
				alert( jsonText );
			}).error(function(data) {
				$scope.errors = "Error: " + data;
				$scope.offers = [];
			});
		};
	}
]);

emailControllers.controller('UploadCtrl', ['$scope',
	function UploadCtrl($scope) {
		$scope.testVar = "hello world";
	}
]);

emailControllers.controller('loginCtrl', ['$scope',
	function loginCtrl($scope) {
		$scope.testVar = "hello world";
	}
]);

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
});
*/
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
