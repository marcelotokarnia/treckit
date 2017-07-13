(function(){
	var deps = [
		'ui.router',
		'apptoolbar',
		'applogin',
		'appadmin',
		'appviewuser',
		'appapi',
		'treckmap',
		'ui-notification',
		'uiGmapgoogle-maps',
		'appajax',
		'track'
	];
	if(APP.USE_TEAMPLE_CACHE){
		deps.push('apptemplates');
	}
	angular.module('app_main', deps);

	angular.module('app_main').config(function($interpolateProvider, $stateProvider, $urlRouterProvider) {
	    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
	    $urlRouterProvider.otherwise('/treckmap');

	    $stateProvider
	        .state('admin', {url: '/admin', template: '<appadmin></appadmin>'})
	        .state('treckmap', {url: '/treckmap', template: '<treckmap></treckmap>'})
	        .state('login', {url: '/login', template: '<applogin></applogin>'})
	        .state('viewuser', {url: '/user/:login', template: '<appviewuser></appviewuser>', controller: 'ViewUserStateCtrl'})
			.state('track', {url: '/track/:tid', template: '<track></track>', controller: 'TrackStateCtrl'})
	});

	angular.module('app_main').config(function(uiGmapGoogleMapApiProvider) {
		uiGmapGoogleMapApiProvider.configure({
			china: true
		});
	});


	angular.module('app_main').controller('AppMainCtrl', function($scope, AppAuth){
	});

	angular.module('app_main').run(function(AppAjax, Notification, $state){
		AppAjax.set_error_handler(function(response){
			if(response.status == 401 && response.data.not_authenticated){
				Notification.error({message:'Voce não está logado. Faça login pra ter acesso a esta funcionalidade'});
				$state.go('login');
			}
		})
	})
})();
