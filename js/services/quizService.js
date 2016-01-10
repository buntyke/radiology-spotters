angular.module('pictureQuiz')
.service('quizService', function ($http, $q) {
    
    this.getQuizData = function(quizUrl) {
        return $http({
            method: 'GET',
            url: quizUrl
        });
    };   
    
    this.randomizeQuestions = function(questions) {
    /*
        Randomize array element order in-place.
        Using Durstenfeld shuffle algorithm.
    */
        for (var i = questions.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = questions[i];
            questions[i] = questions[j];
            questions[j] = temp;
        }
        return questions;
    }
    
    this.checkAllQuestionsAnswered = function(numQuestions, userCorrect) {
        var deferred = $q.defer();
       
        if (numQuestions === userCorrect.length) {
           deferred.resolve();
        } 
        
        return deferred.promise;
        
    }

});