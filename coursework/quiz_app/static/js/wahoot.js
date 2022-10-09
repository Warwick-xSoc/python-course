function startQuestionTimer(game_id, end) {
    countdown(
        function(ts) {
            document.getElementById('time_left').innerHTML = ts.toHTML()
        
            if (ts.minutes === 0 && ts.seconds === 0) {
                window.location.replace('/game/outcome/' + game_id)
            }
        },
        end,
        countdown.MINUTES | countdown.SECONDS
    )
}

function startOutcomeTimer(game_id) {
    setTimeout(function () {
        window.location.replace('/game/play/' + game_id)
    }, 10 * 1000)
}