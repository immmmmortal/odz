const countEl = document.getElementById('count')

function updateViewCount() {
    fetch('http://127.0.0.1:8000/')
        .then(res => res.json())
        .then(res => {
            countEl.us
        })
}