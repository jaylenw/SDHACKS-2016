angular.module('starter')
.factory("Restaurants",['$resource', 'Config', function($resource, Config){
  return $resource(Config.getAPI() + "/document/Restaurants", {},{
    get:{
      method:"GET",
      params:{},
      isArray: true
    }
  })
}]);
