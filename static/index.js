function getQuote() {
    location.reload();
}

function shareTwitter() {
    var textToTweet = $("p").text() + " from https://brianwordgen.herokuapp.com";
    var twtLink = 'http://twitter.com/home?status=' +
        encodeURIComponent(textToTweet);
    window.open(twtLink, '_blank');
}
