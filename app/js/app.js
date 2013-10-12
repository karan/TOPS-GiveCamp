    var emailApp = angular.module('emailApp', [
		'ngRoute',
		'emailControllers'
    ]);
     
    emailApp.config(['$routeProvider',
		function($routeProvider) {
			$routeProvider.
			when('/edit', {
				templateUrl: 'partials/email-edit.html',
				controller: 'EmailListCtrl'
			})/*.
			when('/phones/:phoneId', {
				templateUrl: 'partials/phone-detail.html',
				controller: 'PhoneDetailCtrl'
			}).
			otherwise({
				redirectTo: '/phones'
			})*/;
    }]);
