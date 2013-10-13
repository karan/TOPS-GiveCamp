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
			}).
			when('/upload', {
				templateUrl: 'partials/csv-upload.html',
				controller: 'UploadCtrl'
			}).
			when('/login', {
				templateUrl: 'partials/login.html',
				controller: 'loginCtrl'
			}).
			otherwise({
				redirectTo: '/login'
			});
    }]);
