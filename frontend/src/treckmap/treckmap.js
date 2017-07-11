angular.module('treckmap', ['appapi', 'uiGmapgoogle-maps']);

angular.module('treckmap').factory('mapRepository', function(AppApi){
	var m = {
		loading: false,
		trecks: [],
		map: { center: { latitude: -22.427386, longitude: -44.796379 }, zoom: 12 },
	};

	angular.extend(m, {
		init: init,
		clickMarker: clickMarker,
		closeClick: closeClick
	});

	//navigator.geolocation.watchPosition();
	navigator.geolocation.getCurrentPosition(function(data){
		m.map.center = {latitude: data.coords.latitude, longitude: data.coords.longitude};
		m.me = {coords: angular.copy(m.map.center), key: 'me', options: {icon: '/static/icons/map_markers/bluedot.png'}};
	});

	function clickMarker(trail){
		trail.windowOptions.visible = !trail.windowOptions.visible;
	}

	function closeClick(trail){
		trail.windowOptions.visible = false;
	}

	function init(){
		m.loading = true;
		AppApi.list_trails().then(function(result){
			m.trails = result.data.map(function(trail){
				trail.windowOptions = {visible: false};
				trail.options = {icon: '/static/icons/map_markers/treckgreen.png'};
				return trail;
			});
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