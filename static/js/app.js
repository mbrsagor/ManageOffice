var app = angular.module('myApp', []);

app.controller('postCtrl', function($scope, $http){

    $scope.titleBar ="Blog all post";
   //  // csrf token
   // $httpProvider.defaults.xsrfCookieName = 'csrftoken';
   // $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // Show data template post reqeust
    $http.get('api/post/').then(function(response){
        $scope.postList = [];
        for(var i = 0; i <response.data.length; i++) {
            var addItem = {};
            addItem.id = response.data[i].id
            addItem.title = response.data[i].title
            addItem.content = response.data[i].content
            addItem.name = response.data[i].name
            addItem.date = response.data[i].date
            $scope.postList.push(addItem)
        }
    });

    // add new post
    $scope.addPost = function(){
      $http({
            method  : 'post',
            url     : 'api/post/',
            data    :{title : $scope.title, content : $scope.content, name: $scope.name},
            headers : { 'Content-Type': 'application/json' }
        }).then(function success(response){
            $scope.postList.push(response.data);
        })
        $scope.title= ""
        $scope.name= ""
        $scope.content= ""
    }

    // post category
    $http.get('api/category/').then(function(response){
        $scope.categoryList = [];
        for(var i = 0; i <response.data.length; i++) {
            var addItem = {};
            addItem.id = response.data[i].id
            addItem.name = response.data[i].name
            $scope.categoryList.push(addItem)
        }
    });


    // add new category
    $scope.addCategory = function(){
      $http({
            method  : 'post',
            url     : 'api/category/',
            data    :{name : $scope.name},
            headers : { 'Content-Type': 'application/json' }
        }).then(function success(response){
            $scope.categoryList.push(response.data);
        })
        $scope.name= ""
    }

});
