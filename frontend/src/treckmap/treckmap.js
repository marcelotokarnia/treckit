angular.module('treckmap', ['appapi', 'uiGmapgoogle-maps']);

angular.module('treckmap').factory('mapRepository', function(AppApi, $state){
	var m = {
		loading: false,
		tracks: [],
		map: {
			center: { latitude: -22.427386, longitude: -44.796379 },
			zoom: 12,
		},
	};

	angular.extend(m, {
		init: init,
		clickMarker: clickMarker,
		closeClick: closeClick,
		trackWindowUrl: trackWindowUrl
	});

	function trackWindowUrl(){
		return APP.BASE_URL+'treckmap/track_infowindow.html';
	}

	//navigator.geolocation.watchPosition();
	navigator.geolocation.getCurrentPosition(function(data){
		m.map.center = {latitude: data.coords.latitude, longitude: data.coords.longitude};
		m.me = {windowOptions: {visible: false}, coords: angular.copy(m.map.center), key: 'me', options: {icon: '/static/icons/map_markers/bluedot.png'}};
	});

	function clickMarker(marker){
		marker.windowOptions.visible = !marker.windowOptions.visible;
	}

	function closeClick(marker){
		marker.windowOptions.visible = false;
	}

	function init(){
		m.loading = true;
		AppApi.list_tracks().then(function(result){
			m.tracks = result.data.map(function(track){
				track.windowOptions = {visible: false};
				track.options = {icon: '/static/icons/map_markers/treckgreen.png'};
				return track;
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