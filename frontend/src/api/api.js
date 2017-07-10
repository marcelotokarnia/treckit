angular.module('appapi', ['appajax']);

angular.module('appapi').factory('AppApi', function(AppAjax){
	var api = {
		add: todo,
		login: login,
		logout: logout,
		whoami: whoami,
		list_trails: list_trails,
		get_user_details: get_user_details,
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

	function list_trails(filters){
		return AppAjax.get('/api/list_trails', {filters: angular.toJson(filters)});
	}

	function get_user_details(username){
		return AppAjax.get('/api/get_user_details', {username: username});	
	}

	return api;
});
