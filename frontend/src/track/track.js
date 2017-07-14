angular.module('track', ['appapi']);

angular.module('track').factory('TrackModel', function(AppApi){
	var m = {
		loading: false,
		track: null,
		load: load,
		map: {
			zoom: 12,
			options: {mapTypeId: google.maps.MapTypeId.SATELLITE },
		}
	};

	function load(track_id){
		m.loading = true;
		m.map.kmlopt = {url: "/api/get_track_kml?track_id=" + track_id};
		AppApi.get_track_details(track_id).then(function(result){
			m.track = result.data;
			m.map.center = m.track.coords;
		}).finally(function(){
			m.loading = false;
		});
	}

	return m;
});

angular.module('track').controller('TrackStateCtrl', function($scope, $stateParams, TrackModel){
	var track_id = $stateParams.tid;
	TrackModel.load(track_id);
});

angular.module('track').directive('track', function(){
	return {
		restrict: 'E',
		replace: true,
		scope: {},
		templateUrl: APP.BASE_URL+'track/track.html',
		controller: function($scope, TrackModel){
			$scope.m = TrackModel;
		},
	};
});