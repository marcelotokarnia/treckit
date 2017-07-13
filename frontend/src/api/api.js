angular.module('appapi', ['appajax']);

angular.module('appapi').factory('AppApi', function(AppAjax){
	var api = {
		add: todo,
		login: login,
		logout: logout,
		whoami: whoami,
		list_tracks: list_tracks,
		get_user_details: get_user_details,
		get_track_details: get_track_details
	};

	function todo(){}

	function login(username, password){
		return AppAjax.post('/api/login', {username: username, password: password});
	}

	function logout(){
		return AppAjax.get('/api/logout');
	}

	function whoami(){
		return AppAjax.get('/api/whoami');
	}

	function list_tracks(filters){
		return AppAjax.get('/api/list_tracks', {filters: angular.toJson(filters)});
	}

	function get_user_details(username){
		return AppAjax.get('/api/get_user_details', {username: username});	
	}

	function get_track_details(track_id){
		return AppAjax.get('/api/get_track_details', {track_id: track_id});
	}

	return api;
});
