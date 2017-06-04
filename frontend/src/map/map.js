angular.module('map', ['appapi']);

angular.module('map').factory('mapRepository', function(AppApi){
	var m = {
		loading: false,
		trecks: [],
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

angular.module('map').directive('map', function(){
	return {
		restrict: 'E',
		replace: true,
		scope: {},
		templateUrl: APP.BASE_URL+'map/map.html',
		controller: function($scope, mapRepository){
			mapRepository.init();
			$scope.repo = mapRepository;
		},
	};
});