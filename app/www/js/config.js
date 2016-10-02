angular.module('starter')
.factory("Config",function(){

  var _apiUrl = "http://localhost:9000";
  var configService = {};

  configService.getAPI = function(){
    return _apiUrl;
  }

  return configService;
});
