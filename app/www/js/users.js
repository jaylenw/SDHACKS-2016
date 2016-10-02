angular.module('starter')
.factory("User",['$resource', 'Config', function($resource, Config){
  return $resource(Config.getAPI(), {},{
    login:{
      method:"POST",
      params:{},
      isArray: false,
      url: Config.getAPI() + "/login"
    },
    register:{
      method:"POST",
      params:{},
      isArray: false,
      url: Config.getAPI() + "/user"
    },
    logout:{
      method:"POST",
      params:{},
      isArray: false,
      url: Config.getAPI() + "/logout"
    }
  })
}]);
