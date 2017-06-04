angular.module('treckmap', ['appapi']);

angular.module('treckmap').factory('mapRepository', function(AppApi){
	var m = {
		loading: false,
		trecks: [],
		map: { center: { latitude: 45, longitude: -73 }, zoom: 8 }
	};

	angular.extend(m, {
		init: init,
	});


	function init(){
		m.loading = true;
		AppApi.list_trecks().then(function(result){
			m.trecks = result.data;
		}).finally(function(){
			m.loading = false;
		});
	}

	return m;
});

angular.module('treckmap').directive('treckmap', function(){
	return {
		restrict: 'E',
		replace: true,
		scope: {},
		templateUrl: APP.BASE_URL+'treckmap/treckmap.html',
		controller: function($scope, mapRepository){
			mapRepository.init();
			$scope.repo = mapRepository;
		},
	};
});