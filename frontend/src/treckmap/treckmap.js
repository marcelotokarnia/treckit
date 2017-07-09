angular.module('treckmap', ['appapi', 'uiGmapgoogle-maps']);

angular.module('treckmap').factory('mapRepository', function(AppApi){
	var m = {
		loading: false,
		trecks: [],
		map: { center: { latitude: -22.427386, longitude: -44.796379 }, zoom: 12 },
	};

	angular.extend(m, {
		init: init,
	});

	//navigator.geolocation.watchPosition();
	navigator.geolocation.getCurrentPosition(function(data){
		m.map.center = {latitude: data.coords.latitude, longitude: data.coords.longitude};
		m.me = {coords: angular.copy(m.map.center), key: 'me'};
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